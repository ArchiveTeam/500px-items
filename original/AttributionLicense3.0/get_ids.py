import json
import os
import re


def main():
    ids = set()
    for name in os.listdir('AttributionLicense3-API-Sever-Responses'):
        path = os.path.join('AttributionLicense3-API-Sever-Responses', name)
        if not os.path.isfile(path):
            continue
        print(path)
        with open(path, 'r') as f:
            data = json.loads(re.search(r'(\{.+\})', f.read()).group(1))
            ids |= {p['url'].split('/')[2] for p in data['photos']}
    with open('ids.txt', 'w') as f:
        f.write('\n'.join(sorted(ids)))

if __name__ == '__main__':
    main()

