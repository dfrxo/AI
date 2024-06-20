import math, random as rd

def sense(robot_position, mouse_positions, alpha):
     x,y = robot_position
     a,b = mouse_positions

     manhattan_distance = abs(x-a) + abs(y-b)

     result = math.e ** (-alpha * (manhattan_distance-1))  # Find chance of beep
     if rd.random() < result:          # Roll for beep, return True if we get a beep
          return True
     return False             # Return false if no beep