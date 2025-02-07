#               Lambda Functions Tips

#     LIST :
list1 = [10, 23, 52, 123, 43, 233, 8080]

#=========================================

#def menosum(m):    
#    return m - 1

#=========================================

#res = map(lambda m: m - 1, list1)

#=========================================

print(list(map(lambda m: m-1, list1)))
