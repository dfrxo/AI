import math, random as rd

def sense(robot_position, mouse_positions, alpha):
     x,y = robot_position
     a,b = mouse_positions

     manhattan_distance = abs(x-a) + abs(y-b)

     result = math.e ** (-alpha * (manhattan_distance-1))  # Find chance of beep
     if rd.random() < result:          # Roll for beep, return True if we get a beep
          print("Beep" + str(result))
          return True
     return False             # Return false if no beep

def senseTwo(robot_position, mouse_1, mouse_2, alpha):
     x,y = robot_position
     if mouse_1 != False:
          a,b = mouse_1

          manhattan_distance = abs(x-a) + abs(y-b)

          result = math.e ** (-alpha * (manhattan_distance-1))  # Find chance of beep
          print(result)
          if rd.random() < result:          # Roll for beep, return True if we get a beep
               print("Beep")
               return True

     if mouse_2 != False:
          a,b = mouse_2

          manhattan_distance = abs(x-a) + abs(y-b)

          result = math.e ** (-alpha * (manhattan_distance-1))  # Find chance of beep
          print(result)
          if rd.random() < result:          # Roll for beep, return True if we get a beep
               print("Beep")
               return True
     
     return False             # Return false if no beep
