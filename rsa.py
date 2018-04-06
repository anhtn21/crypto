def fermat_factor(n):
    assert n % 2 != 0
    a = gmpy2.isqrt(n)
    b2 = gmpy2.square(a) - n
    while not gmpy2.is_square(b2):
        a += 1
        b2 = gmpy2.square(a) - n
    p = a + gmpy2.isqrt(b2)
    q = a - gmpy2.isqrt(b2)
    return int(p), int(q)
	
def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    g, y, x = egcd(b%a,a)
    return (g, x - (b//a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('No modular inverse')
    return x%m