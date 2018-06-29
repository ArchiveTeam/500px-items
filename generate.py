import os
import sys


data = [[]]
filenum = int(sys.argv[2])

with open('processed_ids.txt', 'r') as f:
    processed_ids = {l.strip() for l in f}

def create_file(i, d):
    with open('{}_photos.txt'.format(str(i).zfill(4)), 'w') as f:
        f.write('\n'.join(['photos:{}'.format(';'.join(l)) for l in d]))

with open(sys.argv[1], 'r') as f:
    for line in f:
        line = line.strip()
        if line in processed_ids:
            continue
        processed_ids.add(line)
        if len(data[-1]) == 10:
            if len(data) == 50000:
                create_file(filenum, data)
                filenum += 1
                data = []
            data.append([])
        data[-1].append(line)

create_file(filenum, data)

with open('processed_ids.txt', 'w') as f:
    f.write('\n'.join(processed_ids))

