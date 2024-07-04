from functions import stochastic_mouse
import copy

def bot_3_smart_sense(ship_probabilities, robot_position, alpha):
    a, b = robot_position
    total = sum(ship_probabilities.values())
    #bot_3_normalize(ship_probabilities)
    total_probability = 0
    DISTANCE = 9
    for x in range(DISTANCE):
        for y in range(0, DISTANCE - x):
            curr_x, curr_y = a + x, b + y
            prob = ship_probabilities.get((curr_x,curr_y), 0)
            total_probability += prob

    diamond_prob = total_probability/total
    print("smart sense:" + str(diamond_prob))
    if diamond_prob > .0005 and  diamond_prob < .400: #.00001 and diamond_prob < .70:         # .005 and .23
        return True
    else: 
        print("nope")
        return False
    
# def bot_3_smart_sense_two_mice(ship_probabilities, robot_position, alpha):
#     a, b = robot_position
#     total_1 = 0
#     total_2 = 0
#     temp = ship_probabilities.values()
#     bot_3_normalize(ship_probabilities)
#     for x, y in temp:
#         total_1+=x
#         total_2+=y    
        
#     total_probability = 0
#     DISTANCE = 10
#     for x in range(DISTANCE):
#         for y in range(0, DISTANCE - x):
#             curr_x, curr_y = a + x, b + y
#             prob = ship_probabilities.get((curr_x,curr_y), 0)
#             total_probability += prob

#     diamond_prob = total_probability/total
#     left = alpha * 0.6666666667
#     right = alpha * 3.83333333



#     print("smart sense:" + str(diamond_prob))

#     if diamond_prob > .005 and  diamond_prob < .28: #.00001 and diamond_prob < .70:         # .005 and .23
#         return True
#     else: 
#         print("nope")
#         return False
    
def bot_3_normalize(ship_probabilties):
   total = sum(ship_probabilties.values())
   for x,y in ship_probabilties.keys():
      ship_probabilties[(x,y)] = ship_probabilties[(x,y)] / total


def bot_3_montecarlo(ship, ship_probabilities, iterations):
    future_map = copy.deepcopy(ship_probabilities)

    for _ in range(iterations):
        future_map = stochastic_mouse.stochastic_update_probability(ship, future_map)

    return future_map

def bot_3_montecarlo_two_mice(ship, ship_probabilities, iterations):
    for _ in range(iterations):
        future_map = stochastic_mouse.stochastic_update_probability_two_mice(ship, ship_probabilities)

    return future_map

def nudge(ship_probabilities, robot_position, new_robot_position):
  def update(dirt):
    x, y = robot_position
    x1, y1 = new_robot_position
    FINAL_NUM = .000005

    if dirt == 'down':
        for x in range(1,x+1):
           for y in range(1, len(ship_probabilities)):
              if (x,y) in ship_probabilities.keys() and (ship_probabilities[(x,y)] >= FINAL_NUM):
                 ship_probabilities[(x,y)] -= FINAL_NUM
    elif dirt == "up":
        for x in range(x,len(ship_probabilities)):
           for y in range(1, len(ship_probabilities)):
              if (x,y) in ship_probabilities.keys() and (ship_probabilities[(x,y)] >= FINAL_NUM):
                 ship_probabilities[(x,y)] -= FINAL_NUM         
    elif dirt == "left":
        for x in range(1, len(ship_probabilities)):
           for y in range(y, len(ship_probabilities)):
              if (x,y) in ship_probabilities.keys() and (ship_probabilities[(x,y)] >= FINAL_NUM):
                 ship_probabilities[(x,y)] -= FINAL_NUM
    else:
        for x in range(1, len(ship_probabilities)):
           for y in range(1, y+1):
              if (x,y) in ship_probabilities.keys() and (ship_probabilities[(x,y)] >= FINAL_NUM):
                 ship_probabilities[(x,y)] -= FINAL_NUM         
       
  x, y = robot_position
  x1, y1 = new_robot_position
  if x1 > x:
    update("down")
  elif x1 < x:
     update("up")
  elif y1 > y:
     update("right")
  elif y1 < y:
     update("left")  

