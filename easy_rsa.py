import math
import binascii

def getModInverse(a, m):
    if math.gcd(a, m) != 1:
        return None
    u1, u2, u3 = 1, 0, a
    v1, v2, v3 = 0, 1, m

    while v3 != 0:
        q = u3 // v3
        v1, v2, v3, u1, u2, u3 = (
            u1 - q * v1), (u2 - q * v2), (u3 - q * v3), v1, v2, v3
    return u1 % m

def main():
    p = int(input('p: ').strip())
    q = int(input('q: ').strip())
    e = int(input('e: ').strip())
    ct = int(input('ct (as hex): ').strip(), 16)

    n = p*q

    # compute n
    n = p * q

    # Compute phi(n)
    phi = (p - 1) * (q - 1)

    # Compute modular inverse of e
    d = getModInverse(e, phi)

    print("n:  " + str(d))

    # Decrypt ciphertext
    pt = pow(ct, d, n)
    print()  # separate IO
    print("pt (as hex): " + hex(pt)[2:])
    print("pt (as string): " + binascii.unhexlify(hex(pt)[2:]).decode())

if __name__ == "__main__":
    main()
