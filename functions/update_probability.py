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
        beep_mouse_probability[coordinates] = beep_probability                  # P(B|M)

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
        no_beep_mouse_probability[coordinates] = no_beep_probability                  # P(~B|M)

        mouse_and_no_beep_probability = mouse_probability * (no_beep_probability)   # P(~B|M) * P(M)
        total_no_beep_probability += mouse_and_no_beep_probability  # P(~Beep)

    for coordinates, mouse_probability in ship_probability.items():
        x1, y1 = coordinates
        curr_nbm_probability = no_beep_mouse_probability[coordinates]
        m_probability = ship_probability[coordinates]
        new_probability = (curr_nbm_probability * m_probability) / total_no_beep_probability
        ship_probability[coordinates] = new_probability

    
