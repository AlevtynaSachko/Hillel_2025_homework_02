class ReverseIterator:
    def __init__(self, data):
        self.data = data
        self.index = len(data) # починати з кінця

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index -= 1
        return self.data[self.index]


# наприклад 
nums = [10, 25, 30, 144]
for x in ReverseIterator(nums):
    print(x, end=" ")