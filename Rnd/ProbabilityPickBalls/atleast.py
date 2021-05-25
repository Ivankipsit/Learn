import math
from fractions import Fraction

def atleast_func(dict_balls_colors,total_picked_balls,atleast_list1,total_balls):
    N1_list = []
    N2_list = []
    colors = list(dict_balls_colors.keys())
    color_balls = list(dict_balls_colors.values())
    for i in atleast_list1:
        if atleast_list1[0] == i:
            color_needed = i
    list_color = [j for j in range(atleast_list1[1],(total_picked_balls + 1))]
    list_ocolor = [(total_picked_balls - list_color[k]) for k in range(len(list_color))]
#    print(list_color)
#    print(list_ocolor)
    for k in range(len(list_color)):
        N1 = math.comb(color_balls[0],list_color[k])
        N1_list.append(N1)
        N2 = math.comb(color_balls[1],list_ocolor[k])
        N2_list.append(N2)
    N1N2_list = [N1_list[l]*N2_list[l] for l in range(len(N1_list))]
    N_total = sum(N1N2_list)
    D_total = math.comb(total_balls,total_picked_balls)
    result = Fraction(N_total,D_total)
    return result
