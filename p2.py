class StringIterator:
    def __init__(self, string):
        self.string = string
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.string):
            result = self.string[self.index]
            self.index += 1
            return result
        else:
            raise StopIteration

my_string = "SAMI"
my_iterator = StringIterator(my_string)

try:
    while True:
        char = next(my_iterator)
        print(char)
except StopIteration:
    pass
