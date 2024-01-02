class PowerOfTwoIterator:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.end:
            result = 2 ** self.current
            self.current += 1
            return result
        else:
            raise StopIteration

start_range = 0
end_range = 5
power_of_two_iterator = PowerOfTwoIterator(start_range, end_range)

for value in power_of_two_iterator:
    print(value)