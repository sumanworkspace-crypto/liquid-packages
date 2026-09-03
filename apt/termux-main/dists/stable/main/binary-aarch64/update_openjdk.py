import re

with open('Packages', 'r') as f:
    blocks = f.read().split('\n\n')

new_blocks = []
for b in blocks:
    if 'Package: openjdk-21\n' in b:
        # Replace Size, MD5sum, SHA1, SHA256
        b = re.sub(r'^Size: .*', 'Size: 103140952', b, flags=re.MULTILINE)
        b = re.sub(r'^MD5sum: .*', 'MD5sum: e20090c0a0ea58770ca1c44c32e2d01c', b, flags=re.MULTILINE)
        b = re.sub(r'^SHA1: .*', 'SHA1: 7e3599401c23bd953245757964248d6b7b366333', b, flags=re.MULTILINE)
        b = re.sub(r'^SHA256: .*', 'SHA256: 5b7a8836f792a27d1511013b88d64454149c375cc90e05a8478dd8736e40e0c0', b, flags=re.MULTILINE)
    new_blocks.append(b)

with open('Packages', 'w') as f:
    f.write('\n\n'.join(new_blocks))
