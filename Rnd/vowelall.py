from itertools import permutations 
vow = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
inp = []
list1 = []
count = 0
T = int(input())
for i in range(0,T):
    a = str(input())
    inp.append(a)
for j in inp:
    for i in range(1,(len(a)+1)):
        perm = permutations(a, i) 
        for i in list(perm): 
            list1.append(''.join(i))
#    print(list1)
    for ele in list1:
        b = list(ele)
        for i in b:
            if i in vow:
                count+=1
    print(count)