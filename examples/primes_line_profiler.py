from line_profiler import profile

@profile
def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

@profile 
def find_primes(size):
    """Find all prime numbers up to a given size."""
    primes = []
    for num in range(2, size + 1):
        if is_prime(num):
            primes.append(num)
    return primes

@profile
def main():
    print("Starts")
    primes = find_primes(100000)
    print("Primes found:", len(primes))

if __name__ == "__main__":
    main()
