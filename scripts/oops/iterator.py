# Use iterators when you require complex, object-oriented behaviors, such as needing specific class attributes,
# custom methods, or shared object state across multiple parts of your application.
class CounterIterator:
    def __init__(self, low, high):
        self.current = low
        self.high = high

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.high:
            raise StopIteration  # Must manually tell the loop when to stop
        else:
            self.current += 1
            return self.current - 1
