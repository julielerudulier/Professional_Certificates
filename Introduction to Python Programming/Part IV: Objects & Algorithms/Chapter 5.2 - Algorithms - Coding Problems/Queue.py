#A Queue is a type of list where instead of accessing
#any item in the list at any time, you can only add
#items to the end of the list, and you can only access
#items from the start of a list (sort of like a line at
#a store: whoever gets in line first gets to the front
#of the line first).
#
#Adding a new item to the queue is called "enqueueing"
#the item into the queue. Removing an item from the
#queue is called "dequeueing" the item from the queue.
#When an item is "dequeued" from the queue, it is
#removed from the list altogether.
#
#Write a class called Queue. Queue should have the
#following methods:
#
# - An __init__ method that initializes the empty list
#   that is the queue's contents.
# - A enqueue() method that takes one parameter
#   (in addition to self): an item to add to the end of
#   the queue.
# - A dequeue() method that returns the first item
#   (that is, the one added first) from the queue and
#   removes it from the underlying list. If the list is
#   already empty, this returns None.
#
#For example, the following code would print the
#numbers 1, 2, and 3 (in that order). Items are printed
#in the same order in which they are added.
#
#new_queue = Queue()
#new_queue.enqueue(1)
#new_queue.enqueue(2)
#new_queue.enqueue(3)
#print(new_queue.dequeue())
#print(new_queue.dequeue())
#print(new_queue.dequeue())

#Add your class here!
class Queue:
    def __init__(self):
        self.lst = []
        
    def enqueue(self, item):
        self.lst.append(item)
        
    def dequeue(self):
        if len(self.lst) == 0:
            return None
        else:
            first_item = self.lst[0]
            del self.lst[0]
            return first_item


#The following lines of code will test your class.
#If it works correctly, it will print 1, 2, and 3
#in that order, each on their own line.
new_queue = Queue()
new_queue.enqueue(1)
new_queue.enqueue(2)
new_queue.enqueue(3)
print(new_queue.dequeue())
print(new_queue.dequeue())
print(new_queue.dequeue())
