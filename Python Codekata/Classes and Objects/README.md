Classes and Objects

# Problem Statement

You have been given an array ( a ) containing ( n ) positive integers.

Your task is to find the minimum number of moves required to transform the array such that each element is divisible by ( k ) (given).

During each move, you can either increase ( x ) by 1 or choose one element ( ai ) from ( a ) and increase it by ( x ) (then increase ( x ) by 1). However, you can only perform the first operation once for each ( i ) from 1 to ( n ).

Let's solve ( t ) independent test cases.

### Input:

The first line contains ( t ) (the number of test cases).
For each test case: - The first line contains ( n ) and ( k ) (length of ( a ) and required divisor). - The second line contains ( n ) integers ( a1, a2, ..., an ).

### Output:

For each test case, print the minimum number of moves required.
 
### Constraints:

( 1 <= t <= 2 times 10^4 )
( 1 <= n <= 2 times 10^5 )
( 1 <= k <= 10^9 )
( 1 <= ai <= 10^9 )

### Sample input:

5
4 3
1 2 1 3
10 6
8 7 1 8 3 7 5 10 8 9
5 10
20 100 50 20 100500
10 25
24 24 24 24 24 24 24 24 24 24
8 8
1 2 3 4 5 6 7 8

### Sample output:

6
18
0
227
8



