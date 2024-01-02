class PrimeNumberIterator:
    def __init__(self, max_value):
        self.max_value = max_value
        self.current = 2

    def __iter__(self):
        return self

    def is_prime(self, num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    def __next__(self):
        while self.current <= self.max_value:
            if self.is_prime(self.current):
                result = self.current
                self.current += 1
                return result
            else:
                self.current += 1

        raise StopIteration

max_range = 20
prime_iterator = PrimeNumberIterator(max_range)

for prime_number in prime_iterator:
    print(prime_number)