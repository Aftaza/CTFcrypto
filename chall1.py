
from Crypto.Util.number import getPrime, bytes_to_long
from math import gcd
from secret import FLAG


def check(a, b):
    if b == 0:
        return a != 1
    else:
        return check(b, a % b)


def main():
    p = getPrime(1024)
    q = getPrime(1024)
    n = p * p * q
    e = 0x10001
    m = bytes_to_long(FLAG)
    c = pow(m, e, p*q)
    z = sum(check(i, n) for i in range(n))
    print(f'{n = }\n{z = }\n{c = }')


main()
