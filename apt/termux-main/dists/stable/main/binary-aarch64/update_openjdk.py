import re

with open('Packages', 'r') as f:
    blocks = f.read().split('\n\n')

new_blocks = []
for b in blocks:
    if 'Package: openjdk-21\n' in b:
        b = re.sub(r'^Size: .*', 'Size: 103151148', b, flags=re.MULTILINE)
        b = re.sub(r'^MD5sum: .*', 'MD5sum: 49ce6e904ebd16ac81e40d6d7ca6ea49', b, flags=re.MULTILINE)
        b = re.sub(r'^SHA1: .*', 'SHA1: a3446ca000b8d3374d6d432e79ba8283d8d36f61', b, flags=re.MULTILINE)
        b = re.sub(r'^SHA256: .*', 'SHA256: 0e29185216f77ca1f151cb2a13ccd5498c606d1304e2bca2ecc70b66c5b1235b', b, flags=re.MULTILINE)
    new_blocks.append(b)

with open('Packages', 'w') as f:
    f.write('\n\n'.join(new_blocks))
