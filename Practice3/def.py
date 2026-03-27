l = [1,2,3,4,5,"a","b",-1,-2]


l1 = list(filter(lambda x: isinstance(x,int) and x % 2 == 1, l))
print(l1)