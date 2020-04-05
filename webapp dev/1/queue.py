class Queue:
    def __init__(self):
        self.my_queue = []

    def add(self, data):
        self.my_queue.append(data)

    def remove(self):
        try:
           return self.my_queue.pop(0)
        except:
            print('no more  in the queueeeeee')


    def displayQueue(self):
        for data in self.my_queue:
            print(data)

    def length(self):
        return len(self.my_queue)




lak = Queue()

lak.add("yo1")
lak.add(("yo2"))

lak.add("yo3")

lak.add("yo4")
lak.add("yo5")

lak.add("yo6")

lak.displayQueue()

print(lak.remove())

print(lak.remove())
print(lak.remove())
print(lak.remove())
print(lak.remove())
print(lak.remove())
print(lak.remove())
print(lak.remove())
print(lak.remove())
print(lak.remove())