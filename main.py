# import sys
#
# n = 0
# m = 0
# if sys.argv[1] is not None:
#     n = int(sys.argv[1])
# if sys.argv[2] is not None:
#     m = int(sys.argv[2])
#
# print(n + m)
#
# ------

# f = open('input.txt', 'r')
# lines = f.readlines()
# count = int(lines[0])
# array = lines[1].split()
# x = int(lines[2])
# result = 0
# for el in array:
#     if int(el) < x:
#         result = result + 1
#
# print(result, count-result)
# ================
import random

f = open('input.txt', 'r')
lines = f.readlines()

count = int(lines[0])
array = [int(x) for x in lines[1].split()]

x_ind =random.randint(0, count)
print(x)

def partition(l, r):
    pivot = a[random(l...r - 1)]
    pivot = a[random.randint(l, r-1)]
    m = l
    for i = l...r - 1:
        if a[i] < pivot:
            swap(a[i], a[m])
            m + +
    return m

