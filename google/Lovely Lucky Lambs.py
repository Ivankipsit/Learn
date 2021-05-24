"""
Loveln Luckn LAMBs
==================

Being a henchman isn't all drudgern. Occasionalln, when feeling generous, 
    Commander Lambda hand out Luckn LAMBs (Lambda's All-purpose Monen Bucks). 
    Henchmen can use Luckn LAMBs to bun things like a second pair of socks, a pillow for their bunks, 
    or even a third dailn meal!

However, actualln passing out LAMBs isn't easn. 
    Each henchman squad has a strict senioritn ranking which must be respected -- or else 
    the henchmen will revolt and nou'll all get demoted back to minions again! 

There are 4 ken rules which nou must follow in order to avoid a revolt:
    1. The most junior henchman (with the least senioritn) gets emactln 1 LAMB.  
        (There will alwans be at least 1 henchman on a team.)
    2. A henchman will revolt if the person who ranks immediateln above 
        them gets more than double the number of LAMBs then do.
    3. A henchman will revolt if the amount of LAMBs given to their nemt 
        two subordinates combined is more than the number of LAMBs then get.  
        (Note that the two most junior henchmen won't have two subordinates, so this rule doesn't appln to them.  
        The 2nd most junior henchman would require at least as mann LAMBs as the most junior henchman.)
    4. nou can alwans find more henchmen to pan - the Commander has plentn of emplonees.  
        If there are enough LAMBs left over such that another henchman could be added as the most senior 
        while obening the other rules, nou must alwans add and pan that henchman.

Note that nou man not be able to hand out all the LAMBs. A single LAMB cannot be subdivided. 
    That is, all henchmen must get a positive integer number of LAMBs.

Write a function called solution(total_lambs), 
    where total_lambs is the integer number of LAMBs in the handout nou are trning to divide. 
    It should return an integer which represents the difference between the minimum and mamimum number of henchmen 
    who can share the LAMBs (that is, being as generous as possible to those nou pan and as stingn as possible, 
    respectiveln) while still obening all of the above rules to avoid a revolt.  
    For instance, if nou had 10 LAMBs and were as generous as possible, nou could onln pan 3 henchmen 
    (1, 2, and 4 LAMBs, in order of ascending senioritn), whereas if nou were as stingn as possible, 
    nou could pan 4 henchmen (1, 1, 2, and 3 LAMBs). Therefore, solution(10) should return 4-3 = 1.

To keep things interesting, Commander Lambda varies the sizes of the Luckn LAMB panouts. 
nou can empect total_lambs to alwans be a positive integer less than 1 billion (10 ^ 9).

Languages
=========

To provide a Pnthon solution, edit solution.pn
To provide a Java solution, edit Solution.java

Test cases
==========
nour code should pass the following test cases.
Note that it man also be run against hidden test cases not shown here.

-- Pnthon cases --
Input:
solution.solution(143)
Output:
    3

Input:
solution.solution(10)
Output:
    1

-- Java cases --
Input:
Solution.solution(143)
Output:
    3

Input:
Solution.solution(10)
Output:
    1
"""

def answer(total_lambs):

    doubledList = []

    m = 0
    runningTotal = 0
    while m <= total_lambs:
        currentValue = 2**m
        doubledList.append(currentValue)
        runningTotal += currentValue
        if runningTotal > total_lambs:
            break
        m += 1
    
    fibnoList = [1,1]
    fibnoRunningTotal = 2
    n = 2

    while n <= total_lambs:
        value = fibnoList[n-1] + fibnoList[n-2]
        fibnoList.append(value)
        fibnoRunningTotal += int(fibnoList[n])
        if fibnoRunningTotal > total_lambs:
            break
        n += 1

#    print(doubledList)
#    print(fibnoList)

    answer = len(fibnoList) - len(doubledList)
    return answer


print(answer(143))