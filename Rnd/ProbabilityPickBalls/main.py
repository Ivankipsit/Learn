import math
import main_inputs as maininp
import both_colors as bothclr
import one_color as oneclr
import atleast 
import atmost

colors_inp = input("Enter colors of balls in bag: ").split()    #str list
b_inp = input("Enter number of balls: ").split()                #str list
balls = list(map(int,b_inp))                                    #int list
dict_balls_colors = maininp.basic_inputs(colors_inp,b_inp)      #dict
total_balls = sum(balls)                                        #int single
print(dict_balls_colors)

bp_input = input("Enter balls needed to be picked: ").split()
dict_balls_picked = maininp.picked_balls_func(colors_inp,bp_input)
ball_picked = list(map(int,bp_input)) #int
total_picked_balls = sum(ball_picked)
print(dict_balls_picked)

if (0 not in ball_picked)== True:
    both_result = bothclr.both_color_func(balls,ball_picked,total_balls,total_picked_balls)
    print("-->> Probability that {} balls are {} and {} balls are {} is {}".format(ball_picked[0],colors_inp[0],ball_picked[1],colors_inp[1],both_result))
