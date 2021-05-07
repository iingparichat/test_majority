from collections import Counter
import sys

def majority(arr, n):
    print('Input')
    print(n)
    print(arr)
    count = Counter(arr)
    for k, v in count.items():
        print('Output')
        if v > n/2:
            print(k)
            return k
        else:
            print(-1)
            return -1

if __name__ == '__main__':
    arr = str(sys.argv[2])
    arr = [int(i) for i in arr.split(' ')]
    n = int(sys.argv[1])
    majority(arr, n)