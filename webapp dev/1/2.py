set_a = {1, 2, 3, 4, 5, 6}
set_b = {2, 4, 6, 8}

set_b.add("orange")

print(set_b)

set_b.pop()

print(set_b)


class Car:
    def __repr__(self):
        return 'this is the repr function of class car'

    def __str__(self):
        return 'this is the str method of class car'

honda = Car()



print((honda))