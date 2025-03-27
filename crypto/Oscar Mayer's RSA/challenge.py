# vulnerable_rsa.py
import random
from math import gcd
from Crypto.Util.number import getPrime, inverse

def generate_vulnerable_rsa(bits=512):
    while True:
        p = getPrime(bits)
        q = getPrime(bits)
        n = p * q
        phi = (p - 1) * (q - 1)
        
        # Choose small d to make it vulnerable to Wiener's attack
        d = random.randint(1, pow(n, 0.25) // 3)
        
        try:
            e = inverse(d, phi)
            if gcd(e, phi) == 1:
                return n, e, d
        except ValueError:
            continue

def encrypt_flag(flag, e, n):
    m = int.from_bytes(flag.encode(), 'big')
    c = pow(m, e, n)
    return c

if __name__ == "__main__":
    flag = "flame{I_l0v3_h0t_d0g5}"
    n, e, d = generate_vulnerable_rsa()
    ciphertext = encrypt_flag(flag, e, n)

    with open("output.txt", "w") as f:
        f.write(f"n = {n}\n")
        f.write(f"e = {e}\n")
        f.write(f"ciphertext = {ciphertext}\n")