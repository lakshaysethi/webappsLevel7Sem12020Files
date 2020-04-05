class Stack:

    def __repr__(self):
        print('this is lakshay\'s Stack ')


    def __init__(self):
        self.my_stack = []

    def push(self, data):

            self.my_stack.append(data)

    def pop(self):
        return self.my_stack.pop()

    def displayStack(self):
        for data in self.my_stack:
            print(data)

    def length(self):

        return len(self.my_stack)

lak = Stack()

lak.push("yo1")
lak.push(("yo2"))

lak.push("yo3")

lak.push("yo4")
lak.push("yo5")

lak.push("yo6")

lak.displayStack()

print(lak.pop())

print(lak.pop())
print(lak.pop())
print(lak.pop())
