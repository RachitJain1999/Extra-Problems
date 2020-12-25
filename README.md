# Extra-Problems
Some extra problems based on DSA.

## Array
<p align="justify">
<ins>KSum</ins>: We are given an array, a number n and k, we need to find all the unique combinations of k numbers that sum up to n. If n=10 and k=4, we need to find all unique 
set of numbers of size 4 from the array that sum up to 10. The ksum function takes in a sorted array.
</p>

<p align="justify">
<ins>Spiral Matrix</ins>: Displaying a matrix in spiral form. This means the outer most elements are displayed first and then the innermost in a circular fashion. 
</p>

    matrix =[[1,2,3],
             [4,5,6],
             [7,8,9]], 
              
    result = 1,2,3,6,9,8,7,4,5.

<p align="justify">
<ins>Longest Consecutive Sequence</ins>: We have an array of integers and we have to find the length of longest sequence we can form such that the numbers are in increments of 1.
</p>

    arr = [0,2,4,5,0,1,1]
    ans = 3, The sequence is [0,1,2] 

<p align="justify">
<ins>Maximum Subarray Modulo Sum</ins>: This is an extension of subarray sum problem, we need to find the maximum sum modulo M that we can form from taking any subarray from a 
given array. We use properties of modulo sum and prefix array to solve this problem in O(nLogn).
</p>

    arr = [3,3,9,9,5], mod = 7
    answer = 6 for the subarray [3,3] ((3+3)mod7=6)
