#A Stack is a type of list where instead of accessing
#any item in the list at any time, you can only add
#or remove items from the top of the Stack.
#
#Adding a new item to the stack is called "pushing"
#the item onto the stack. Removing the top item on
#the stack is called "popping" the item off the stack.
#When an item is "popped" off the stack, it is removed
#from the list altogether.
#
#Write a class called Stack. Stack should have the
#following methods:
#
# - An __init__ method that initializes the empty list
#   that is the stack's contents.
# - A stack_push() method that takes one parameter (in
#   addition to self): an item to push onto the top
#   of the stack.
# - A stack_pop() method that returns the current top
#   item on the stack and removes it from the underlying
#   list. If the list is already empty, this returns
#   None.
#
#For example, the following code would print the
#numbers 3, 2, and 1 (in that order). Note that this
#is the opposite order of how they are pushed: the
#pop method will always return the elements in the
#reverse order that they were added in.
#
#new_stack = Stack()
#new_stack.stack_push(1)
#new_stack.stack_push(2)
#new_stack.stack_push(3)
#print(new_stack.stack_pop())
#print(new_stack.stack_pop())
#print(new_stack.stack_pop())

#Add your class here!
class Stack:
    def __init__(self):
        self.lst = []
        
    def stack_push(self, item):
        self.lst.append(item)
        return self.lst
        
    def stack_pop(self):
        if len(self.lst) == 0:
            return None
        else:
            top_item = self.lst[-1]
            del self.lst[-1]
            return top_item


#The following lines of code will test your class.
#If it works correctly, it will print 3, 2, and 1
#in that order, each on their own line.
new_stack = Stack()
new_stack.stack_push(1)
new_stack.stack_push(2)
new_stack.stack_push(3)
print(new_stack.stack_pop())
print(new_stack.stack_pop())
print(new_stack.stack_pop())
