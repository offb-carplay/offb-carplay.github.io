"""Create flat APT indexes directly from real DEB control files."""
import argparse
import bz2
from datetime import datetime, timezone
from email.utils import format_datetime
import gzip
import hashlib
import io
import json
from pathlib import Path
import re
import tarfile


def ar_members(data):
    if data[:8] != b'!<arch>\n':
        raise ValueError('Not a Debian ar archive')
    offset = 8
    result = {}
    while offset < len(data):
        header = data[offset:offset + 60]
        if len(header) != 60 or header[-2:] != b'`\n':
            raise ValueError('Invalid ar member')
        size = int(header[48:58])
        if size < 0 or offset + 60 + size > len(data):
            raise ValueError('Truncated ar archive')
        name = header[:16].decode('ascii').strip().rstrip('/')
        if name in result:
            raise ValueError('Duplicate ar member')
        result[name] = data[offset + 60:offset + 60 + size]
        offset += 60 + size + size % 2
    if result.get('debian-binary') != b'2.0\n':
        raise ValueError('Unsupported Debian format')
    return result


def control_fields(data):
    members = ar_members(data)
    controls = [v for k, v in members.items() if k.startswith('control.tar.') or k == 'control.tar']
    if len(controls) != 1:
        raise ValueError('Expected one control archive')
    with tarfile.open(fileobj=io.BytesIO(controls[0]), mode='r:*') as archive:
        matches = [m for m in archive.getmembers() if m.name.removeprefix('./') == 'control' and m.isfile()]
        if len(matches) != 1 or matches[0].size > 65536:
            raise ValueError('Invalid control file')
        text = archive.extractfile(matches[0]).read().decode('utf-8')
    result = {}
    current = None
    for line in text.splitlines():
        if line.startswith((' ', '\t')) and current:
            result[current] += '\n' + line
        elif line:
            current, value = line.split(':', 1)
            if current in result or not re.fullmatch(r'[A-Za-z][A-Za-z0-9-]*', current):
                raise ValueError('Invalid or duplicate control field')
            result[current] = value.strip()
    for key in ['Package', 'Version', 'Architecture', 'Description']:
        if not result.get(key):
            raise ValueError('Missing ' + key)
    return result


def build(root):
    root = Path(root).resolve()
    entries = []
    architectures = set()
    reports = []
    identities = set()
    for deb in sorted((root / 'debs').glob('*.deb')):
        if deb.is_symlink() or not re.fullmatch(r'[A-Za-z0-9.+_~-]+\.deb', deb.name):
            raise ValueError('Unsafe DEB filename')
        data = deb.read_bytes()
        fields = control_fields(data)
        identity = tuple(fields[k] for k in ['Package', 'Version', 'Architecture'])
        if identity in identities:
            raise ValueError('Duplicate package/version/architecture')
        identities.add(identity)
        architectures.add(fields['Architecture'])
        for generated in ['Filename', 'Size', 'MD5sum', 'SHA1', 'SHA256', 'SHA512']:
            fields.pop(generated, None)
        fields.update(Filename='debs/' + deb.name, Size=str(len(data)),
            MD5sum=hashlib.md5(data).hexdigest(), SHA256=hashlib.sha256(data).hexdigest(), SHA512=hashlib.sha512(data).hexdigest())
        entries.append('\n'.join(f'{k}: {v}' for k, v in fields.items()) + '\n\n')
        reports.append({k: fields[k] for k in ['Package', 'Version', 'Architecture', 'Filename', 'Size', 'SHA256']})
    packages = ''.join(entries).encode('utf-8')
    indexes = {'Packages': packages, 'Packages.gz': gzip.compress(packages, mtime=0), 'Packages.bz2': bz2.compress(packages)}
    for filename, content in indexes.items():
        (root / filename).write_bytes(content)
    lines = ['Origin: OFFB CarPlay', 'Label: OFFB CarPlay — Experimental', 'Suite: stable', 'Codename: offb',
        'Date: ' + format_datetime(datetime.now(timezone.utc), usegmt=True),
        'Architectures: ' + ' '.join(sorted(architectures)), 'Components: main',
        'Description: OFFB CarPlay experimental package repository']
    for title, algorithm in [('MD5Sum', 'md5'), ('SHA256', 'sha256'), ('SHA512', 'sha512')]:
        lines.append(title + ':')
        lines.extend(f' {hashlib.new(algorithm, content).hexdigest()} {len(content):16} {filename}' for filename, content in indexes.items())
    (root / 'Release').write_text('\n'.join(lines) + '\n', encoding='utf-8', newline='\n')
    (root / 'packages-report.json').write_text(json.dumps(reports, indent=2) + '\n', encoding='utf-8')
    (root / '.nojekyll').touch()
    return reports


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    print(json.dumps(build(args.root), indent=2))
