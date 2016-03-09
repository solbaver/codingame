import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
# ---
# Hint: You can use the debug stream to print initialTX and initialTY, if Thor seems not follow your orders.

# light_x: the X position of the light of power
# light_y: the Y position of the light of power
# initial_tx: Thor's starting X position
# initial_ty: Thor's starting Y position
light_x, light_y, initial_tx, initial_ty = [int(i) for i in raw_input().split()]

# game loop

while True:
    remaining_turns = int(raw_input())  # The remaining amount of turns Thor can move. Do not remove this line.

    # Write an action using print
    # To debug: print >> sys.stderr, "Debug messages..."

    # A single line providing the move to be made: N NE E SE S SW W or NW
    diff_x = light_x - initial_tx
    diff_y = light_y - initial_ty
    ans = ''
    while diff_x !=0 or diff_y !=0:
        
        if diff_y > 0:
            ans = ans + 'S'
            diff_y = diff_y - 1
            
        if diff_y < 0:
            ans = ans + 'N'
            diff_y = diff_y + 1
            
        if diff_x > 0:
            ans = ans + 'E'
            diff_x = diff_x - 1
            
        if diff_x < 0:
            ans = ans + 'W'
            diff_x = diff_x + 1
            

        print ans
        ans = ''