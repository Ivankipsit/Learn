"""
Please Pass the Coded Messages
==============================

You need to pass a message to the bunny workers, but to avoid detection, the code you agreed to use is... obscure, to say the least. The bunnies are given food on standard-issue plates that are stamped with the numbers 0-9 for easier sorting, and you need to combine sets of plates to create the numbers in the code. The signal that a number is part of the code is that it is divisible by 3. You can do smaller numbers like 15 and 45 easily, but bigger numbers like 144 and 414 are a little trickier. Write a program to help yourself quickly create large numbers for use in the code, given a limited number of plates to work with.

You have L, a list containing some digits (0 to 9). Write a function solution(L) which finds the largest number that can be made from some or all of these digits and is divisible by 3. If it is not possible to make such a number, return 0 as the solution. L will contain anywhere from 1 to 9 digits.  The same digit may appear multiple times in the list, but each element in the list may only be used once.

Languages
=========

To provide a Java solution, edit Solution.java
To provide a Python solution, edit solution.py

Test cases
==========
Your code should pass the following test cases.
Note that it may also be run against hidden test cases not shown here.

-- Java cases --
Input:
Solution.solution({3, 1, 4, 1})
Output:
    4311

Input:
Solution.solution({3, 1, 4, 1, 5, 9})
Output:
    94311

-- Python cases --
Input:
solution.solution([3, 1, 4, 1])
Output:
    4311

Input:
solution.solution([3, 1, 4, 1, 5, 9])
Output:
    94311
"""


from itertools import combinations

def solution(l):
    l.sort(reverse = True)
    for i in reversed(range(1, len(l) + 1)):
        for k in list(combinations(l, i)):
            if sum(k) % 3 == 0: 
                return int(''.join(map(str, k)))
    return 0
l = [3, 1, 4, 1]
print(solution(l))

"""
What basically happens is
line 1 - import necessities
line 3 - reads function and jumps to end of function
line 10 - input
line 11 - function call
line 3 - function runs
line 4 - input is sorted and reversed.. (arranged in decending order)
line 5 - for i in --reversed--: reversed means that the loop is running in backwards..
    i.e, normal loop(0,i) runs from 0 -> i .. reversed loop(0,i) runs from i to 0
line 6 - k is a list of combinations i.e., 
    combinations(a,b) means a = list and b is the number of digits/ele in list
line 7 - checks divisibility of the sum(list) with 3
line 8 - if passed- 
"""
