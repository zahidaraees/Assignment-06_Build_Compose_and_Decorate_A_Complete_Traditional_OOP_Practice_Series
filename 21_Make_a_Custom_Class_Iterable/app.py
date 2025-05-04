class CountdownIterator:
    def __init__(self, start):
        self.current = start

    def __next__(self):
        if self.current < 0:
            raise StopIteration
        number = self.current
        self.current -= 1
        return number

class Countdown:
    def __init__(self, start):
        self.start = start

    def __iter__(self):
        return CountdownIterator(self.start)

# Using the Countdown class
countdown = Countdown(10)

for num in countdown:
    print(num)