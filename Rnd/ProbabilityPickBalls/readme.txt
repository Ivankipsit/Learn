TEST CASES:
==========

Q1:     A bag contains 6 red and 4 yellow ball. Four balls
    are picked at random what is the probability that 1 is 
    yellow and 3 are red?
O/p:
    Enter colors of balls in bag: red yellow
    Enter number of balls: 6 4
    {'red': 6, 'yellow': 4}
    Enter balls needed to be picked: 3 1
    Enter [Y] if question contains 'atleast' or 'atmost' else enter [N]: N
    -->> Probability that 3 balls are red and 1 balls are yellow is 8/21


Q2:     A Bag contains 6 Red balls and 4 Yellow balls. 
    Three balls are picked at random what is the probability that 1 is
    red?
O/p:
    Enter two 'colors' of balls in bag: red yellow
    Enter 'number' of balls: 6 4
    {'red': 6, 'yellow': 4}
    Enter balls needed to be picked: 1 2
    Enter [Y] if question contains 'atleast' or 'atmost' else enter [N]: N
    -->> Probability that 1 balls are red and 2 balls are yellow is 3/10


Q3:     A Bag contains 6 Red balls and 4 Yellow balls. 
    Three balls are picked at random what is the probability that none is red?
O/p:
    Enter colors of balls in bag: red yellow
    Enter number of balls: 6 4
    {'red': 6, 'yellow': 4}
    Enter balls needed to be picked: 0 3
    Enter [Y] if question contains 'atleast' or 'atmost' else enter [N]: N
    -->> Probability that 0 balls are red and 3 balls are yellow is 1/30


Q4:     A Bag contains 6 Red balls and 4 Yellow balls. 
    Four balls are picked at random what is the probability atleast
    one is red?
O/p:
    Enter colors of balls in bag: red yellow
    Enter number of balls: 6 4
    {'red': 6, 'yellow': 4}
    Enter balls needed to be picked: 4 0
    Enter [Y] if question contains 'atleast' or 'atmost' else enter [N]: Y
    Enter 'atleast' or 'atmost': atleast
    Enter ballcount and color: 1 red
    -->Probability for your specific inputs  = 209/210


Q5:     A Bag contains 6 Red balls and 4 Yellow balls. 
    Three balls are picked at random what is the probability atmost
    2 are red?
O/p:
    Enter colors of balls in bag: red yellow
    Enter number of balls: 6 4
    {'red': 6, 'yellow': 4}
    Enter balls needed to be picked: 3 0
    Enter [Y] if question contains 'atleast' or 'atmost' else enter [N]: Y
    Enter 'atleast' or 'atmost': atmost
    Enter ballcount and color : 2 red
    -->Probability for your specific inputs  = 5/6


Q6:     A Bag contains 6 Red balls and 4 Yellow
    balls. Four balls are picked at random what is the probability that
    3 are red and 1 is yellow or 2 are red and two is yellow?
    (if question contains 2 parts or more run the program again and add 
    the possibilities)
O/p:
    Enter colors of balls in bag: red yellow
    Enter number of balls: 6 4
    {'red': 6, 'yellow': 4}
    Enter balls needed to be picked: 3 1
    Enter [Y] if question contains 'atleast' or 'atmost' else enter [N]: N
    -->> Probability that 3 balls are red and 1 balls are yellow is 8/21

    Enter colors of balls in bag: red yellow
    Enter number of balls: 6 4
    {'red': 6, 'yellow': 4}
    Enter balls needed to be picked: 2 2
    Enter [Y] if question contains 'atleast' or 'atmost' else enter [N]: N
    -->> Probability that 2 balls are red and 2 balls are yellow is 3/7

    8/21 + 3/7 = 17/21


*At the time of usage the values ll be accurate but there may be 
changes in final statement*
