# wiener_attack.py
from fractions import Fraction
from math import isqrt

def continued_fraction(n, d):
    while d:
        a = n // d
        yield a
        n, d = d, n - a * d

def convergents(cf):
    convs = []
    h1, h2 = 1, 0
    k1, k2 = 0, 1

    for a in cf:
        h = a * h1 + h2
        k = a * k1 + k2
        convs.append((h, k))
        h2, h1 = h1, h
        k2, k1 = k1, k

    return convs

def is_perfect_square(n):
    h = n & 0xF
    if h > 9:
        return False
    t = isqrt(n)
    return t * t == n

def wiener_attack(e, n):
    cf = list(continued_fraction(e, n))
    for k, d in convergents(cf):
        if k == 0:
            continue
        phi_candidate = (e * d - 1) // k
        s = n - phi_candidate + 1
        discriminant = s * s - 4 * n
        if discriminant >= 0 and is_perfect_square(discriminant):
            return d
    return None

def decrypt_flag(c, d, n):
    m = pow(c, d, n)
    flag_bytes = m.to_bytes((m.bit_length() + 7) // 8, 'big')
    return flag_bytes.decode()

def read_values_from_file(filename="output.txt"):
    with open(filename, "r") as f:
        lines = f.readlines()
        n = int(lines[0].split(" = ")[1].strip())
        e = int(lines[1].split(" = ")[1].strip())
        ciphertext = int(lines[2].split(" = ")[1].strip())
    return n, e, ciphertext

if __name__ == "__main__":
    n, e, ciphertext = read_values_from_file()

    d = wiener_attack(e, n)
    if d:
        print(f"Recovered d = {d}")
        flag = decrypt_flag(ciphertext, d, n)
        print(f"Recovered flag: {flag}")
    else:
        print("Wiener's attack failed.")