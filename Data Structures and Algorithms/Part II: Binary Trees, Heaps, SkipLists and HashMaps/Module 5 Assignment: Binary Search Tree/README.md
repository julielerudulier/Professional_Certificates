### Module 5 Assignment: Binary Search Tree

For this assignment, you will be coding the add() and remove() methods of a binary search tree. A binary search tree, or BST, is a collection of nodes, each having a data item and a reference pointing to a left and a right child node. The BST must adhere to the following order property: for any given node, its left child's data and all of its children's data must be less than the current node while its right child's data and all of its children's data must be greater than the current node. In order to compare the data, all elements added to the tree must implement Java's generic Comparable interface. Since trees are naturally recursive structures, each of these methods should be implemented recursively.

#### BSTNode
A BSTNode class is provided to you and will be used to represent the nodes in the tree. This file should be treated as read-only and should not be modified in any way. This BSTNode class contains getter and setter methods to access and mutate the structure of the nodes. Please make sure that you understand how this class works, as interaction with this class is crucial for this assignment.

#### Pointer Reinforcement
Since both the add() and remove() methods may change the structure of the tree, we highly recommend that you use a technique called pointer reinforcement. Although using pointer reinforcement is not required, it will help to make your code cleaner, and it'll also help greatly in future assignments if you end up taking the next course in our series! 

#### Comparable
As stated, the data in the BST must implement the Comparable interface. As you'll see in the les, the generic typing has been specified to require that it implements the Comparable interface. You use the interface by making a method call like data1.compareTo(data2). This will return an int, and the value tells you how data1 and data2 are in relation to each other.

* If the int is positive, then data1 is larger than data2.
* If the int is negative, then data1 is smaller than data2.
* If the int is zero, then data1 equals data2.

Note that the returned value can be any integer in Java's int range, not just -1, 0, 1.

#### Successor
Recall that earlier in the modules you learned about the successor and predecessor of a node in a tree. As a refresher, the successor of a node, n, is the node in the tree that contains the smallest data that is larger than n's data. The predecessor of a node, n, is the node in the tree that contains the largest data that is smaller than n's data. When removing a node from a BST that has two children, we can choose to replace the removed node with either it's successor or predecessor. For the 2-child case in remove(), you will be replacing the removed node with its successor node, NOT the predecessor node. For more details, please refer to the javadocs for remove().

#### Helper Methods
You'll also notice that the public method stubs we've provided do not contain the parameters necessary for recursion to work, so these public methods should act as "wrapper methods" for you to use. You will have to write private recursive helper methods and call them in these wrapper methods. All of these helper methods must be private. To reiterate, do not change the method headers for the provided methods.

#### General Tips

* Don't forget your base case; this should be the first thing that is checked in your recursive calls. Note that the base case for add() may be different that the base case in remove().

* If you get stuck on remove(), the video above on pointer reinforcement has pseudocode for the remove() method!

* We highly recommend copying the starter code and working in your preferred IDE in order to have access to features such as code completion, auto-formatting, and much more!

---

#### Here are general assignment guidelines that should be followed.

* Do not include any package declarations in your classes.
* Do not change any existing class headers, constructors, instance/global variables, or method signatures. For example, do not add throws to the method headers since they are not necessary. Instead, exceptions should be thrown as follows: throw new InsertExceptionHere("Error: some exception was thrown");
* All helper methods you choose to write should be made private. Recall the idea of Encapsulation in Object-Oriented Programming!
* Do not use anything that would trivialize the assignment. (e.g. Don't import/use java.util.ArrayList for an ArrayList assignment.)
* Always be very conscious of efficiency. Even if your method is to be , traversing the structure multiple times is considered inefficient unless that is absolutely required (and that case is extremely rare).
* If applicable, use the generic type of the class; do not use the raw type of the class. For example, use new LinkedList<Integer>() instead of new LinkedList().

#### Use of the following statements should be avoided at all times.
| Statements 1 | Statements 2 | Statements 3 |
| :---: | :---: | :---: |
| package | System.arraycopy() | clone() |
| assert() | Arrays class | Array class |
| Thread class | Collections class | Collection.toArray() |
| Reflection APIs  | Inner or nested classes  | Lambda Expressions |
	
