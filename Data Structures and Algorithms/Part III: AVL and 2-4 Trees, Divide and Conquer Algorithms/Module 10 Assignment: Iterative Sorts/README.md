### Module 10 Assignment: Iterative Sorts

For this assignment you will be coding 3 different iterative sorts: bubble sort, insertion sort, and selection sort. In addition to the requirements for each sort, the autograder will be looking at the number of comparisons made between elements to test for efficiency.

For each sorting algorithm, you may assume that the array you are sorting will not contain null elements. You should also assume that the array may contain any number of duplicate elements.

Your implementations should match what was taught in this course.

#### Comparator
Each method will take in a Comparator, which is used to compare two elements. You must use this Comparator, as the number of comparisons performed with it will be used when testing your assignment. The comparator is used as follows:

comparator.compare(A, B) will return:

- "<" 0 if A is less than B
- ">" 0 if A is greater than B
- "0" if A is equal to B

#### Generic Methods
Most of the assignments is this course so far have utilized generics by incorporating them into the class declaration. However, the rest of the assignments will have you implement various algorithms as static methods in a utility class. Thus, the generics from here on will use generic methods instead of generic classes (hence the <T> in each of the method headers and javadocs).  This also means any helper methods you create will also need to be static with the same <T> in the method header.

#### In-Place Sorts
The three sorting algorithms that you will be implementing are in-place sorts. This means that the items in the array passed in should not get copied over to another data structure. Note that you can still create variables that hold only one item. However, you should not create another data structure, such as an array or list, in the method.

#### Stable Sorts
Some of the sorts below are stable sorts. This means that duplicates must remain in the same relative positions after sorting as they were before sorting.

#### Adaptive Sorts
Some of the sorts below are adaptive sorts. This means that the algorithm takes advantage of existing order in the input array. The algorithm can detect existing order in the input array and optimize its performance based on that order.

#### Bubble Sort
Bubble sort should be in-place, stable, and adaptive. It should have a worst case running time of O(n2) and a best case running time of O(n). Note: Implement bubble sort with the optimization where it utilizes the last swapped index. Remembering where you last swapped will enable some optimization for bubble sort. For example, traversing the array from smaller indices to larger indices, if you remember the index of your last swap, you know after that index, there are only the largest elements in order. Therefore, on the next iteration, you start at the front but stop at the last swapped index. Make sure you only look at the indices that you do not know are sorted. Do not make extra comparisons.

#### Insertion Sort
Insertion sort should be in-place, stable, and adaptive. It should have a worst case running time of O(n2) and a best case running time of O(n).

Note that, for this implementation, you should sort from the beginning of the array. This means that after the first pass, indices 0 and 1 should be relatively sorted. After the second pass, indices 0-2 should be relatively sorted. After the third pass, indices 0-3 should be relatively sorted, and so on.

#### Selection Sort
Selection sort should be in-place, unstable, and adaptive.  It should have a worst case running time of O(n2) and a best case running time of O(n2).  You can implement either the minimum version or the maximum version; both are acceptable since they will both yield the same number of comparisons.

#### General Tips

* If your comparison count is slightly over the required amount, double check your for-loop bounds to ensure that you are not unnecessarily comparing elements.

* We highly recommend copying the starter code and working in your preferred IDE in order to have access to features such as code completion, auto-formatting, and much more!

---

#### Here are general assignment guidelines that should be followed.

* Do not include any package declarations in your classes.
* Do not change any existing class headers, constructors, instance/global variables, or method signatures. For example, do not add throws to the method headers since they are not necessary. Instead, exceptions should be thrown as follows: throw new InsertExceptionHere("Error: some exception was thrown");
* All helper methods you choose to write should be made private. Recall the idea of Encapsulation in Object-Oriented Programming!
* Do not use anything that would trivialize the assignment. (e.g. Don't import/use java.util.ArrayList for an ArrayList assignment.)
* Always be very conscious of efficiency. Even if your method is to be O(n), traversing the structure multiple times is considered inefficient unless that is absolutely required (and that case is extremely rare).
* If applicable, use the generic type of the class; do not use the raw type of the class. For example, use new LinkedList<Integer>() instead of new LinkedList().

#### Use of the following statements should be avoided at all times.
| Statements 1 | Statements 2 | Statements 3 |
| :---: | :---: | :---: |
| package | System.arraycopy() | clone() |
| assert() | Arrays class | Array class |
| Thread class | Collections class | Collection.toArray() |
| Reflection APIs  | Inner or nested classes  | Lambda Expressions |
	
