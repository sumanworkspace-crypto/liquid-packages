import hashlib
import os

def hash_file(path):
    with open(path, 'rb') as f:
        data = f.read()
    md5 = hashlib.md5(data).hexdigest()
    sha256 = hashlib.sha256(data).hexdigest()
    size = len(data)
    return md5, sha256, size

files = [
    "main/binary-aarch64/Packages",
    "main/binary-aarch64/Packages.gz",
    "main/binary-aarch64/Packages.xz",
    "main/binary-all/Packages",
    "main/binary-all/Packages.gz",
    "main/binary-all/Packages.xz"
]

md5_lines = []
sha256_lines = []

for f in files:
    if os.path.exists(f):
        md5, sha256, size = hash_file(f)
        md5_lines.append(f" {md5} {size:16} {f}")
        sha256_lines.append(f" {sha256} {size:16} {f}")

release_content = f"""Codename: stable
Components: main
Architectures: aarch64 all
MD5Sum:
{chr(10).join(md5_lines)}
SHA256:
{chr(10).join(sha256_lines)}
"""

with open("Release", "w") as f:
    f.write(release_content)
