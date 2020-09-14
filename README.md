# Session 8 - Functional Parameters
This assignment project is written in Python, and tested with pytest. It includes following files.
-session8.py      : This is the assignment code
-test_session8.py : This is pytest unit test. It tests completeness of assignment
>**Global Variable:**   
In Python, a variable declared outside of the function or in global scope is known as a global variable. This means that a global variable can be accessed inside or outside of the function.  
>**Local Variable:**  
A variable declared inside the function's body or in the local scope is known as a local variable.  
>**NonLocal Variable:**  
Nonlocal variables are used in nested functions whose local scope is not defined. This means that the variable can be neither in the local nor the global scope.  
>**Closure:**  
A Closure is a function object that remembers values in enclosing scopes even if they are not present in memory.

>When do we have closures?  
The criteria that must be met to create closure in Python are summarized in the following points.
- We must have a nested function (function inside a function).  
- The nested function must refer to a value defined in the enclosing function.  
- The enclosing function must return the nested function.  

>When to use closures?  
Closures can avoid the use of global values and provides some form of data hiding. It can also provide an object oriented solution to the problem.
When there are few methods (one method in most cases) to be implemented in a class, closures can provide an alternate and more elegant solution. But when the number of attributes and methods get larger, it's better to implement a class.

>Assignement Problem Statement:  
- **Problem Statement 1:** Write a closure that takes a function and then check whether the function passed has a docstring with more than 50 characters. 50 is stored as a free variable.  
**Solution:**  
1. Write outer function with character length threshold.  
2. Write inner function which checks if doc string length is greater than the threshold in outer function.

- **Problem Statement 2:** Write a closure that gives you the next Fibonacci number.  
**Solution:**  
1. Write outer function which creates empty list.
2. Write inner function which reads list and calculates next fubonacci number and updates the list with new fibonacci number.

- **Problem Statement 3:**We wrote a closure that counts how many times a function was called. Write a new one that can keep a track of how many times add/mul/div functions were called, and update a global dictionary variable with the counts.  
**Solution:**
1. Define function add, mul, div
2. Define global empty dictionary variable to update function count.
3. Write outer function which adds function name to dictionary.
4. Write inner function which will increment the count by one,each time the function is called.  

- **Problem Statement 4:**Modify above such that now we can pass in different dictionary variables to update different dictionaries.    
1. Define outer function which takes function name and dictionary as input arguement.
2. Add functin name to dictionary in outer function.
3. Write inner function which will increment the count by one,each time the function is called.
