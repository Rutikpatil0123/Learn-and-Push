class Counter:
    overall_totoal = 0
    def __init__(self):
        self.my_totoal = 0
    def increment(self):
        self.__class__.overall_totoal += 1
        self.my_totoal += 1

    
c1 = Counter()
c2 = Counter()
c1.increment()
c2.increment()
c2.increment()
print(c1.my_totoal)
print(c1.overall_totoal)
print(c2.my_totoal)
print(c2.overall_totoal)