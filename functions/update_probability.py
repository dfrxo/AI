import math

def update_probability_beep(ship_probability, robot_position, alpha):
    total_beep_probability = 0
    x, y = robot_position
    beep_mouse_probability = {}
    # Find P(Mouse|Beep) = P(B|M) * P(M) / P(B)

    for coordinates, mouse_probability in ship_probability.items():
        x1, y1 = coordinates
        manhattan_distance = abs(x - x1) + abs(y-y1)        
        beep_probability = math.e ** (-alpha * (manhattan_distance-1))
        beep_mouse_probability[coordinates] = beep_probability     # P(B|M)

        mouse_and_beep_probability = mouse_probability * (beep_probability)   # P(B|M) * P(M)
        total_beep_probability += mouse_and_beep_probability  # P(Beep)

    for coordinates, mouse_probability in ship_probability.items():
        x1, y1 = coordinates
        curr_bm_probability = beep_mouse_probability[coordinates]
        m_probability = ship_probability[coordinates]
        new_probability = (curr_bm_probability * m_probability) / total_beep_probability
        ship_probability[coordinates] = new_probability
    print("beep" + str(total_beep_probability))

    
def update_probability_no_beep(ship_probability, robot_position, alpha):
    total_no_beep_probability = 0
    x, y = robot_position
    no_beep_mouse_probability = {}
    # Find P(Mouse|~Beep) = P(~B|M) * P(M) / P(~B)

    for coordinates, mouse_probability in ship_probability.items():
        x1, y1 = coordinates
        manhattan_distance = abs(x - x1) + abs(y-y1)        
        no_beep_probability = 1 - (math.e ** (-alpha * (manhattan_distance-1)))
        no_beep_mouse_probability[coordinates] = no_beep_probability                # P(~B|M)
        mouse_and_no_beep_probability = mouse_probability * (no_beep_probability)   # P(~B|M) * P(M)
        total_no_beep_probability += mouse_and_no_beep_probability                  # P(~Beep)

    for coordinates, mouse_probability in ship_probability.items():
        x1, y1 = coordinates
        curr_nbm_probability = no_beep_mouse_probability[coordinates]
        m_probability = ship_probability[coordinates]
        new_probability = (curr_nbm_probability * m_probability) / total_no_beep_probability
        ship_probability[coordinates] = new_probability

def update_probabilities_two_mice(ship_probabilities, robot_position, beep, alpha):
    x,y = robot_position
    
    for cell in ship_probabilities:
        if cell != robot_position:
            p_mouse1, p_mouse2 = ship_probabilities[cell]
            d1 = abs(x - cell[0]) + abs(y - cell[1])
            if beep:
                prob_beep = math.exp(-alpha * (d1 - 1))
                ship_probabilities[cell][0] = prob_beep * p_mouse1
                ship_probabilities[cell][1] = prob_beep * p_mouse2
            else:
                prob_no_beep = 1 - math.exp(-alpha * (d1 - 1))
                ship_probabilities[cell][0] = prob_no_beep * p_mouse1
                ship_probabilities[cell][1] = prob_no_beep * p_mouse2

    total_prob_mouse1 = sum(p[0] for p in ship_probabilities.values())
    total_prob_mouse2 = sum(p[1] for p in ship_probabilities.values())

    for cell in ship_probabilities:
        ship_probabilities[cell][0] /= total_prob_mouse1
        ship_probabilities[cell][1] /= total_prob_mouse2

def normalize(ship_probabilties):
   total = sum(ship_probabilties.values())
   for x,y in ship_probabilties.keys():
      ship_probabilties[(x,y)] = ship_probabilties[(x,y)] / total