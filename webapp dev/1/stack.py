class Stack:
    def __init__(self,maxSize):
        self.my_stack = []
        self.maxSize = maxSize

    def push(self,data):

        if(len(self.my_stack)<self.maxSize):
            self.my_stack.append(data)
        else:
            print(f'yo i can only handle so much, max stack size is {self.maxSize}')

    def pop(self):
        if(len(self.my_stack)>0):

            return self.my_stack.pop()

        else:
            print('I dont have more')

    def displayStack(self):
        for data in self.my_stack:
            print(data)



lak = Stack(5)

lak.push("yo1")
lak.push(("yo2"))

lak.push("yo3")

lak.push("yo4")
lak.push("yo5")

lak.push("yo6")

lak.displayStack()

lak.pop()
lak.pop()
lak.pop()
lak.pop()
lak.pop()
lak.pop()
lak.pop()
lak.pop()



