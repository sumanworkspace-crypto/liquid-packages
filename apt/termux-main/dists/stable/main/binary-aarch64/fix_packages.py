with open('Packages', 'r') as f:
    content = f.read()

blocks = content.split('\n\n')
new_blocks = []
seen_openjdk = False

for b in blocks:
    if 'Package: openjdk-21\n' in b:
        if '105872208' in b:
            continue # skip the old one
    new_blocks.append(b)

with open('Packages', 'w') as f:
    f.write('\n\n'.join(new_blocks))
