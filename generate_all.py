import sys


def main():
    start = 0
    end = 265000000
    with open('0009_all_{}_{}_100_ids.txt'.format(start, end), 'w') as f:
        f.write('\n'.join(['all:{}-{}'.format(i, i+99)
                           for i in range(start, end, 100)]))

if __name__ == '__main__':
    main()

