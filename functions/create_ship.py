import random as rd

def create_ship(d):
  #     # = Blocked
  #     $ = Fire
  #     O = Open
  ship_layout = [["#" for x in range(d)] for x in range(d)]  # Fill array with blocked 
  x1,y1 = rd.randint(1, d-2), rd.randint(1, d-2)               # Choose random coordinates in interior
  ship_layout[x1][y1] = 'O'
  one_open_neighbor = []
    
  while True:  # "Iteratively do the following" part
      one_open_neighbor.clear()
      for x in range(1,d-1):
          for y in range(1,d-1):
              if ship_layout[x][y] == '#':
                      count = 0
                      if ship_layout[x-1][y]=='O':
                          count+=1
                      if ship_layout[x+1][y]=='O':
                          count+=1
                      if ship_layout[x][y-1]=='O':
                          count+=1
                      if ship_layout[x][y+1]=='O': count+=1
                      if count==1 and (x!=x1 or y!=y1):
                          one_open_neighbor.append((x,y))
                      
      if len(one_open_neighbor)==0:
                        break
      x,y = one_open_neighbor[rd.randint(0,len(one_open_neighbor)-1)] 
      ship_layout[x][y] = 'O'
  # Open half of dead-ends - final part
  closed_neighbors_dict = {}
  one_open_neighbor.clear()
  for x in range(1,d-1):
          for y in range(1,d-1):
              if ship_layout[x][y] == 'O':
                      temp_closed_neighbors = []
                      count = 0
                      if ship_layout[x-1][y]=='O':
                          count+=1
                      elif x!=1:
                           temp_closed_neighbors.append((x-1,y))  
                      if ship_layout[x+1][y]=='O':
                          count+=1
                      elif x!= d-2:
                           temp_closed_neighbors.append((x+1,y))  
                      if ship_layout[x][y-1]=='O':
                          count+=1
                      elif y!=1:
                           temp_closed_neighbors.append((x,y-1))    
                      if ship_layout[x][y+1]=='O': 
                           count+=1
                      elif y!= d-2:
                           temp_closed_neighbors.append((x,y+1))  
                      if count==1 and (x!=x1 or y!=y1):
                          one_open_neighbor.append((x,y))
                          closed_neighbors_dict[(x,y)] = closed_neighbors_dict.get((x,y), []) + temp_closed_neighbors

  rd.shuffle(one_open_neighbor) # Randomize the list of dead ends
  one_open_neighbor = one_open_neighbor[:len(one_open_neighbor)//2] # Split the list in half
  for x,y in one_open_neighbor:   # Open them
       neighbors_to_open = closed_neighbors_dict[(x,y)]      
       r = rd.randint(0, len(neighbors_to_open)-1)
       x2, y2 = neighbors_to_open[r]
       ship_layout[x2][y2] = 'O'
   
  return ship_layout
