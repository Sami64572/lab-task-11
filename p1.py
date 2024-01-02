class CountdownIterator:
    def __init__(self, start):
        self.start = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.start < 0:
            raise StopIteration
        else:
            self.start -= 1
            return self.start + 1

try:
    start_value = int(input("Enter the starting point for the countdown: "))
except ValueError:
    print("Invalid input. Please enter a valid integer.")
    exit()

countdown = CountdownIterator(start_value)

for number in countdown:
    print(number)