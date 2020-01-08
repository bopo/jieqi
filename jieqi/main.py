import sys
from glob import glob

from config import *


def main(y = '1900', n = '0'):
    nums = str(n).zfill(2)
    file = "data/{}.dat".format(nums)
    line = open(file, 'r').readlines()

    for x in line:
        if y in x:
            print(x)
            print(jieqiming(n))
            print(detailjieqi[int(n)])

if __name__ == '__main__':
	main(sys.argv[1], sys.argv[2])
