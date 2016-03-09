import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = []
m = []
# game loop
while True:
    space_x, space_y = [int(i) for i in raw_input().split()]
    n = []
    m = []
    for i in xrange(8):
        mountain_h = int(raw_input())  # represents the height of one mountain, from 9 to 0. Mountain heights are provided from left to right.
        if mountain_h != 0:
            n.append(i)
            m.append(mountain_h)
        print >> sys.stderr, "SpaceX =", space_x, "SpaceY =", space_y, "mountain_h =", mountain_h, "i =", i ,  "n =", n ,  "m =", m 
    # Write an action using print
    maxh = m.index(max(m))
    print >> sys.stderr, "maxh =", maxh
    if space_x == n[maxh]:
        print 'FIRE'
    else:
        print 'HOLD'
    # To debug: print >> sys.stderr, "Debug messages..."

    # either:  FIRE (ship is firing its phase cannons) or HOLD (ship is not firing).
    # print "FIRE"
