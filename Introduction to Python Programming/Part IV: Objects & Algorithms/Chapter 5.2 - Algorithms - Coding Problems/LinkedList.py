#In Python we deal with data structures like lists,
#but we don't talk much about how lists are implemented
#by Python itself.
#
#One way in which lists can be implemented is with what
#is called a Linked List. In a Linked List, a list is
#made of a series of items. Each item contains two
#elements: its own value (node.value), and a pointer to
#where to find the next element in the list
#(node.next_node). So, you can't jump right in to
#"item 7"; you instead have to start with the first
#item and keep getting the next item until you reach the
#seventh item.
#
#Below is some code we've written to implement a
#Linked List. Specifically, this code represents a
#single node in a linked list: a full list is created
#just by chaining nodes like these together. The last
#node in the linked list will point to None as the
#next item; that indicates you've reached the end of
#the linked list.
#
#Write a function called linked_list_search. Your
#linked_list_search function should take two parameters:
#a single linked list node, and a search term. Your
#function should return True if the search term is the
#value of the linked list node or any node after it.
#It should return False if the value is not found in
#the linked list.

class LinkedListNode:
    def __init__(self, value, next_node = None):
        self.value = value
        self.next_node = next_node
        
#Write your function here!
def linked_list_search(node, search_term):
    while(node):
        if(node.value == search_term):
            return True
        node = node.next_node
    return False


#Below are lines of code that create a linked list,
#and then search for two values in that linked list:
#one that is there, one that isn't. If your function
#works, it should print True then False.
node_7 = LinkedListNode(5)
node_6 = LinkedListNode(2, node_7)
node_5 = LinkedListNode(9, node_6)
node_4 = LinkedListNode(1, node_5)
node_3 = LinkedListNode(4, node_4)
node_2 = LinkedListNode(6, node_3)
root_node = LinkedListNode(7, node_2)

print(linked_list_search(root_node, 9))
print(linked_list_search(root_node, 3))
