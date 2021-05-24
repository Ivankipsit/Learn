import math
from fractions import Fraction
def basic_inputs(colors_inp,b_inp):
    balls = list(map(int,b_inp))
    dict_balls_colors = {colors_inp[n]:balls[n] for n in range(len(colors_inp))}
    return dict_balls_colors

def picked_balls_func(colors_inp,bp_input):
    ball_picked = list(map(int,bp_input))
    dict_balls_picked = {colors_inp[n]:ball_picked[n] for n in range(len(colors_inp))}
    return dict_balls_picked






