#def somar(x):
#    fun2 = lambda x: x + 2
#    return fun2(x) * 4
#print(somar(1))

#x = "biel"
#print(x.encode())
#
#h = hex(85)
#print(h)

list1 = [10, 23, 52, 123, 43, 233, 8080]

def menosum(x):
    
    return x - 1

#res = map(menosum, list1)
#print(list(res))

tntfz = map(menosum, list1)
print(list(tntfz))