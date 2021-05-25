import math
import sys
import main_inputs as maininp
import both_colors as bothclr
import one_color as oneclr
import atleast as atlst
import atmost as atmst

colors_inp = input("Enter two 'colors' of balls in bag: ").split()    #str list
b_inp = input("Enter 'number' of balls: ").split()                #str list
balls = list(map(int,b_inp))                                    #int list
dict_balls_colors = maininp.basic_inputs(colors_inp,b_inp)      #dict
total_balls = sum(balls)                                        #int single
print(dict_balls_colors)


bp_input = input("Enter balls needed to be picked: ").split()
dict_balls_picked = maininp.picked_balls_func(colors_inp,bp_input)
ball_picked = list(map(int,bp_input)) #int
total_picked_balls = sum(ball_picked)

switch_inp = input("Enter [Y] if question contains 'atleast' or 'atmost' else enter [N]: ")

if switch_inp == "Y":
    switch_inp2 = input("Enter 'atleast' or 'atmost': ")
    if switch_inp2 == "atleast":
        atleast_list = input("Enter ballcount and color: ").split()
        atleast_list1 = list(map(int,atleast_list[0]))
        atleast_list1.append(atleast_list[1])           #(int,str)
        atleast_list1.reverse()                         #(str,int)final
        atleast_result = atlst.atleast_func(dict_balls_colors,total_picked_balls,atleast_list1,total_balls)
        print("-->Probability for your specific inputs is {}".format(atleast_result))
        sys.exit()

    if switch_inp2 == "atmost":
        atmost_list = input("Enter ballcount and color : ").split()
        atmost_list1 = list(map(int,atmost_list[0]))
        atmost_list1.append(atmost_list[1])           #(int,str)
        atmost_list1.reverse()                         #(str,int)final
        atmost_result = atmst.atmost_func(dict_balls_colors,total_picked_balls,atmost_list1,total_balls)
        print("-->Probability for your specific inputs is {}".format(atmost_result))
        sys.exit()
if switch_inp == "N":
    if (0 in ball_picked)== True:
        both_result = oneclr.one_color_func(balls,ball_picked,total_balls,total_picked_balls)
        print("-->> Probability that {} balls are {} and {} balls are {} is {}".format(ball_picked[0],colors_inp[0],ball_picked[1],colors_inp[1],both_result))

    if (0 not in ball_picked)== True:
        both_result = bothclr.both_color_func(balls,ball_picked,total_balls,total_picked_balls)
        print("-->> Probability that {} balls are {} and {} balls are {} is {}".format(ball_picked[0],colors_inp[0],ball_picked[1],colors_inp[1],both_result))

