#One concept you will encounter in future CS class is the
#idea of a binary tree.
#
#A binary tree is made of nodes. Each node has three
#attributes: its own value, a left branch, and a right branch.
#The left branch will be lower than the node's own value, and
#the right branch will be higher than the node's own value.
#
#Some nodes will not have any branches; these are called leaf
#nodes. They only have their own value. Some nodes may have
#only one branch as well.
#
#Every binary tree has a single root node at the top of the
#tree. Most algorithms that operate on the tree will start at
#this root node.
#
#For example, let us imagine a binary tree with seven nodes.
#The top node's value is 10. The top node has two child nodes:
#the left node's value is 5, lower than 10. The right node's
#value is 15, higher than 10. Then, the left node has its own
#left and right nodes, with values 3 and 7: the lower and higher
#than 5 respectively, but both lower than 10 because they come
#from the original node's left (lower) branch. The right node's
#left and right branches have values 12 and 18, again lower
#and higher than 15 but both higher than 10.
#
#Below is the code for a single node. Right function called
#binary_tree_search. binary_tree_search should take two
#parameters: a single node, and a search value. It should return
#True if the search value is found anywhere in the tree with
#the node at the top, and False if the search value is not found.
#
#To do this, you'll want to write a function that goes down the
#tree similar to a binary search. If the search value is lower than
#the current node's value, it should continue searching to the
#left. If the search value is higher than the current node's value,
#it should continue searching to the right. If the search value is
#equal to the current node's value, it should return True. If the
#current node has no children (both left and right are None), it
#should return False as it has reached the bottom of the tree.
#
#You may assume that no two nodes will have the same value, and that
#every node will have either two children or none. You should not
#assume that the tree will have 7 nodes; it may have 3, 7, 15, 31,
#or more.
#
#HINT: Try breaking this into cases. What do you do if the node
#has the right value? What if the node is none? What if the node's
#value is higher than the search term? What if it's lower?
#
#HINT 2: To get around not knowing how big the tree will be,
#think about a process you can repeat over and over until either
#you find the search term or reach a leaf node. To repeat that
#process, you'd apply the same reasoning each time, just changing
#what node you're looking at.

class Node:
    def __init__(self, value, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right

#Write your binary_tree_search function here!
def binary_tree_search(node, value):
    while(node):
        if node.value == value:
            return True
        elif node.value > value:
            node = node.left
        elif node.value < value:
            node = node.right
       
    return False


#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print: True, True, True, True, False, False, False
#(each on a separate line)

root_node = Node(10)
root_node.left = Node(5)
root_node.right = Node(15)
root_node.left.left = Node(3)
root_node.left.right = Node(7)
root_node.right.left = Node(12)
root_node.right.right = Node(18)

print(binary_tree_search(root_node, 18))
print(binary_tree_search(root_node, 7))
print(binary_tree_search(root_node, 15))
print(binary_tree_search(root_node, 10))
print(binary_tree_search(root_node, 1))
print(binary_tree_search(root_node, 11))
print(binary_tree_search(root_node, 21))
