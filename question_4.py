
import sys
for line in sys.stdin:
    list1_str, list2_str=line.strip().split('|')
    list1_int=list(map(int, list1_str.strip().split()))
    list2_int=list(map(int, list2_str.strip().split()))
    print(" ".join(str(a*b)for a, b in zip(list1_int,list2_int)))
