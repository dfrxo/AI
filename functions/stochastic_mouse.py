import random as rd

def stochastic_mouse(ship, mouse_position):
    neighbors = __get_neighbors(ship, mouse_position)
    neighbors.append(mouse_position)
    roll = rd.randint(0, len(neighbors)-1)
    return neighbors[roll]

def stochastic_update_probability(ship, ship_probability):
    ship_probability = dict(sorted(list(ship_probability.items()), key = lambda x: x[0]))
    new_probabilities = {}
    for x in range(len(ship)):
        for y in range(len(ship)):
            if ship[x][y] in ('O', 'M'):
                neighbors = __get_neighbors(ship, (x,y))
                new_probability = 0
                for n in neighbors:
                    mouse_probability = ship_probability[n]
                    temp = __get_neighbors(ship, n)
                    new_probability += mouse_probability/len(temp)
                new_probabilities[(x,y)] = new_probability
            if ship[x][y] == 'R':
                new_probabilities[(x,y)] = 0
    
    return new_probabilities



def __get_neighbors(ship, curr_position):
    neighbors = []
    x, y = curr_position
    if x!=0 and (ship[x-1][y] in ('O','M')):
        neighbors.append((x-1,y))
    if x!=len(ship)-1 and (ship[x+1][y] in ('O','M')):
        neighbors.append((x+1,y))
    if y!=len(ship)-1 and (ship[x][y+1] in ('O','M')):
        neighbors.append((x,y+1))
    if y!=0 and (ship[x][y-1] in ('O','M')):
        neighbors.append((x,y-1))
    return neighbors   