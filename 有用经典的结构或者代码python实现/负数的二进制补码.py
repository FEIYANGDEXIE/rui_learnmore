def bindigits(n, bits):
    s = bin(n & int("1" * bits, 2))[2:]
    return ("{0:0>%s}" % (bits)).format(s)
print(bindigits(-1,32))
a=bindigits(-1,32)
a=list(str(a))
a=list(map(int,a))
print(sum(a))