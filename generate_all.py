import sys


def main():
    start = int(sys.argv[1])
    end = int(sys.argv[2])
    with open('0008_all_{}_{}.txt'.format(start, end), 'w') as f:
        f.write('\n'.join(['all:{}-{}'.format(i, i+999)
                           for i in range(start, end, 1000)]))

if __name__ == '__main__':
    main()

