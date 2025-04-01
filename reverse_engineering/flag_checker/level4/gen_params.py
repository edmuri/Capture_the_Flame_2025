import struct
from random import seed, randint

seed(1)

P = 4294967087
flag = struct.unpack("11I", b"Cra\x01cki\x01ngD\x01isc\x01ret\x01eLo\x01gs4\x01The\x01Fun\x01&Lu\x01lz\x01\x01")

test_pt = [randint(0, P) for _ in range(12) ]

exponents = []
while len(exponents) < 12:
	e = randint(0, P)
	try:
		d = pow(e, -1, P-1)
		exponents.append(e)
	except:
		continue

test_ct = [pow(p, e, P) for p,e in zip(test_pt, exponents)]

flag_enc = [pow(f, pow(e, -1, P-1), P) for f, e in zip(flag, exponents)]
assert all([pow(f_enc, e, P) == f for f_enc, e, f in zip(flag_enc, exponents, flag) ])


print("exponents: ", exponents )
print("test_pt:", test_pt)
print("test_ct:", test_ct)
print("flag_enc:", flag_enc)


print("const uint32_t test_pt[12] = {%s};" % ",".join(map(str, test_pt)))
print("const uint32_t test_ct[12] = {%s};" % ",".join(map(str, test_ct)))
print("const uint32_t flag_enc[12] = {%s};" % ",".join(map(str, flag_enc)))
for e in exponents:
	print(e)
