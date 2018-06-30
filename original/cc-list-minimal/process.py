import re


def main():
    ids = set()
    with open('cc-list-minimal', 'r') as f:
        for line in f:
            m = re.search('/photo/([0-9]+)', line)
            if m:
                ids.add(m.group(1))
    with open('results', 'w') as f:
        f.write('\n'.join(sorted(ids)))

if __name__ == '__main__':
    main()

