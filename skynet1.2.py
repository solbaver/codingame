



#works with fast start1
import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

road = int(raw_input())  # the length of the road before the gap.
gap = int(raw_input())  # the length of the gap.
platform = int(raw_input())  # the length of the landing platform.
jumpflag = 0
# game loop
while True:
    speed = int(raw_input())  # the motorbike's speed.
    coord_x = int(raw_input())  # the position on the road of the motorbike.
    print >> sys.stderr, "speed =", speed, "coord_x =", coord_x, "road =", road, "gap =", gap ,  "platform =", platform 
    # Write an action using print
    # To debug: print >> sys.stderr, "Debug messages..."
    
    # A single line containing one of 4 keywords: SPEED, SLOW, JUMP, WAIT.
    if jumpflag == 0:
        if (road - coord_x < speed):
            print "JUMP"
            jumpflag = 1
        else:
            if(speed*2>platform):
                print "SLOW"
            else:
                print "SPEED"
    else:
        print "SLOW"
