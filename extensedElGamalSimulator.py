from math import gcd
import random

def primRoots(modulo):
    coprime_set = {num for num in range(1, modulo) if gcd(num, modulo) == 1}
    return [g for g in range(1, modulo) if coprime_set == {pow(g, powers, modulo)
            for powers in range(1, modulo)}]


def ElGamal_Key_Generation():
    #p = 11
    #d = 3
    d = random.randrange(1, p-2)
    Primitive_root = primRoots(p)
    e1 = random.choice(Primitive_root)
    e2 = e1**d % p
    Public_key = [e1, e2, p]
    Private_key = d
    return Public_key, Private_key


def ElGamal_Encryption(e1, e2, p, P):
    #r = 4
    r = random.randint(1, p-2)
    c1 = e1**r % p
    c2 = P*e2**r % p
    return c1, c2


def ElGamal_Decryption(d, p, c1, c2):
    P = c2*c1**(p-1-d) % p
    return P


Plaintext = int(input("input Plaintext : "))
print("Plaintext : ", Plaintext)

p = int(input("input p : "))

Public_key, Private_key = ElGamal_Key_Generation()
c1, c2 = ElGamal_Encryption(Public_key[0], Public_key[1], Public_key[2], Plaintext)
print("Ciphertext : (", c1, ", ", c2, ")")

p = ElGamal_Decryption(Private_key, Public_key[2], c1, c2)
print("Plaintext : ", p)
