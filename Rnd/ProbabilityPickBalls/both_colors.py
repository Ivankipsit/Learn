import math
from fractions import Fraction
def both_color_func(balls,ball_picked,total_balls,total_picked_balls):
    N_list = []
    for n in range(len(balls)):
        N = math.comb(balls[n],ball_picked[n])
        N_list.append(N)
    N_total = math.prod(N_list)
    D_total = math.comb(total_balls,total_picked_balls)  
    result = Fraction(N_total,D_total)
    return result

