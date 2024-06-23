import random as rd

def stochastic_mouse(ship, mouse_position):
    def get_neighbors(curr_position):
        neighbors = []
        x, y = curr_position
        if x!=0 and (ship[x-1][y] == 'O'):
            neighbors.append((x-1,y))
        if x!=len(ship)-1 and (ship[x+1][y] == 'O'):
            neighbors.append((x+1,y))
        if y!=len(ship)-1 and (ship[x][y+1] == 'O'):
            neighbors.append((x,y+1))
        if y!=0 and (ship[x][y-1] == 'O'):
            neighbors.append((x,y-1))
        return neighbors    
    
    neighbors = get_neighbors(mouse_position)
    neighbors.append(mouse_position)

    roll = rd.randint(0, len(neighbors)-1)

    return neighbors[roll]

    
