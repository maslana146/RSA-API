from math import sqrt, gcd
import random


def is_prime(n):
    """is_prime fun. checks that number n in prime number"""
    if n == 2:
        return True
    if n % 2 == 0 or n <= 1:
        return False

    sqr = int(sqrt(n)) + 1

    for divisor in range(3, sqr, 2):
        if n % divisor == 0:
            return False
    return True

def gen_primes(start=0, end=1000):
    """Generate prime numbers from start(0) to end(1000)"""
    primes = [i for i in range(start, end) if is_prime(i)]
    return random.sample(primes, 2)

def euler_fun(p, q):
    """Carmichael's totient function."""
    p, q = p - 1, q - 1
    return abs(p * q) // gcd(p, q)

def mod_inverse(a, m):
    """Modular multiplicative inverse fun."""
    for x in range(1, m):
        if (((a % m) * (x % m)) % m == 1):
            return x
    return -1

def gen_key():
    """Main key generation"""
    p, q = gen_primes()
    n = p * q
    euler_n = euler_fun(p, q)
    e_numbers = [i for i in range(1, euler_n) if gcd(i, euler_n) == 1]
    e = random.choice(e_numbers)
    d = mod_inverse(e, euler_n)
    pub_key = (n, e)
    priv_key = (n, d)
    return pub_key, priv_key

def encrypt_rsa(data, pub_key):
    """Encrypt text with pub_key"""
    n, e = pub_key
    result = []
    for letter in data:
        result.append(ord(letter) ** e % n)
    return result

def decode_rsa(data, priv_key):
    """Decode text with priv_key"""
    result = ""
    n, d = priv_key
    for i in data:
        result += chr(int(i) ** d % n)
    return result
