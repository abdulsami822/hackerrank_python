def average(array):
    sett=set(array)
    return sum(sett)/len(sett)
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
