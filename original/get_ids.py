import json
import os
import re
import sys


def main():
    ids = set()
    for name in os.listdir(sys.argv[1]):
        path = os.path.join(sys.argv[1], name)
        if not os.path.isfile(path):
            continue
        print(path)
        with open(path, 'r') as f:
            data = json.loads(re.search(r'(\{.+\})', f.read()).group(1))
            ids |= {p['url'].split('/')[2] for p in data['photos']}
    with open('{}_ids.txt'.format(sys.argv[1]), 'w') as f:
        f.write('\n'.join(sorted(ids)))

if __name__ == '__main__':
    main()

