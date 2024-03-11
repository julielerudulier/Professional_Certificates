### Module 6 Assignment: MinHeap

For this assignment, you will be coding a MinHeap that is backed by an array of contiguous elements. Here is a tree and array representation of the same MinHeap:

#### Properties
A MinHeap is a type of binary tree with two main properties:

Shape Property: The tree must be complete. All levels of the tree must be full except the bottom-most level. If the bottom-most level is not full, it must be filled from left to right with no gaps.
Order Property: Each node's data is smaller than the data in its children. There is no explicit relationship between sibling nodes.
These properties guarantee that the smallest element in the heap will be at the root of the heap.

#### Implementation Details
Although heaps are usually classified as a type of tree, they are commonly implemented using an array due to their completeness. In your implementation, you should leave index 0 empty and begin your heap at index 1. This will make the arithmetic for finding parent and children indices simpler.

When resizing your backingArray, double the current capacity. Therefore, if the initial capacity is 13, the first resize should bring the total backingArray capacity to 26. Note that this includes the 0th index!

You may assume that your implementation does not need to handle duplicate elements. That is, the add method will never be passed duplicates and the remove method will never have to deal with the heap having duplicates. To be clear, your implementation would most likely work even if we were to test for duplicates; however, this will help remove ambiguity surrounding grading and testing your implementation.

Unlike your BST homework, you are not required to use recursion in this assignment. Use whatever you find most intuitive - recursion, iteration, or both. However, regardless of the technique you use, make sure to meet the efficiency requirements as discussed in this course.

#### General Tips

* In a MinHeap containing n elements, only the first n / 2 elements will have children. How can you utilize this important property when upheaping and downheaping elements in your MinHeap?
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
	
