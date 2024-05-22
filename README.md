# DS-GoZen-Tasks

Ds/Algorithm\
1: Find Missing Number\
Question: Given an array of integers from 1 to n with one missing number, find the missing number.\
Explanation:\
One approach is to calculate the sum of integers from 1 to n using the formula (n * (n + 1)) / 2.\
Then, iterate through the given array and calculate the sum of all elements.\
The missing number can be found by subtracting the sum of array elements from the sum of integers from 1 to n.\
Example Input:\
Input Array: [1, 2, 3, 4, 6, 7, 8]\
Answer:\
Missing Number: 5\
Test Input:\
Input Array: [1, 3, 4, 5, 6, 7, 8, 9, 10]


2: Remove Duplicates\
Question: Given a sorted array, remove the duplicates in-place such that each element appears only once and returns the new length.\
Explanation:\
Start with two pointers, i and j, initially pointing to the first two elements of the array.\
Iterate through the array with the pointer j, comparing each element with the element at index i.\
If the element at index j is different from the element at index i, increment i and update the element at index i with the element at index j.\
Continue this process until j reaches the end of the array. The length of the array up to index i will be the new length without duplicates.\
Example Input:\
Input Array: [1, 1, 2, 2, 3, 4, 4, 5]\
Answer:\
New Length: 5\
Test Input:\
Input Array: [1, 1, 1, 2, 2, 3, 3, 3, 4, 5]


3. Recursion Question: Factorial\
Question: Write a recursive function to find the factorial of a non-negative integer n.\
Explanation:\
The factorial of a non-negative integer n is the product of all positive integers less than or equal to n.\
Base case: If n is 0 or 1, return 1 (the factorial of 0 and 1 is 1).\
Recursive step: Multiply n by the factorial of n - 1 (i.e., n * factorial(n - 1)).\
Example Input:\
n = 5\
Answer:\
Factorial of 5: 120\
Test Input:\
n = 10


5. Rotate Array\
Question: Given an array and an integer k, rotate the array to the right by k steps.\
Explanation:\
Given an array and an integer k, we want to move the last k elements of the array to the front.\
We can achieve this by performing the following steps:\
● Reverse the entire array.\
● Reverse the first k elements.\
● Reverse the remaining elements.\
Example Input:\
Input Array: [1, 2, 3, 4, 5, 6, 7]\
k = 3\
Answer:\
Rotated Array: [5, 6, 7, 1, 2, 3, 4]\
Test Input:\
Input Array: [3, 8, 9, 2, 5]\
k = 2
