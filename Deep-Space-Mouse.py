import pygame, random as rd, math, heapq, csv, os
from collections import defaultdict
from functions import create_ship, search_button_increment

def main(): 
    pygame.init()
    d = 40
    mice_type = 1
    alpha = .04
    # rd.seed(25) # Set random seed (same result each run)

    SCREEN_WIDTH = 900
    SCREEN_HEIGHT = 900
    SURFACE_WIDTH = math.ceil(SCREEN_WIDTH / d) 
    SURFACE_HEIGHT = math.ceil(SCREEN_HEIGHT / d) 

    test_surface = pygame.Surface((SURFACE_WIDTH,SURFACE_HEIGHT)) # Surface object goes on top of display
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    pygame.display.set_caption("My little robot")
    clock = pygame.time.Clock() # Time object

    ship = create_ship.create_ship(d)
    ship_probabilities = {} 

    SPLIT = SCREEN_HEIGHT / len(ship)
    # Split screen into blocks 
    ship_surfaces_dict = {(y*SPLIT,x*SPLIT):ship[x][y] for x in range(len(ship)) for y in range(len(ship))}

    open_cells = []
    # Color in the blocks with respective colors
    for coordinates in ship_surfaces_dict: 
                color = "black" if ship_surfaces_dict[coordinates]=="#"  \
                else "orchid" if ship_surfaces_dict[coordinates]=="O" \
                else "orange" if ship_surfaces_dict[coordinates]=='F' else 'white'
          
                test_surface.fill(color)
                screen.blit(test_surface, coordinates[0:2])
                if color == "orchid":
                     open_cells.append(coordinates)

    for x, y in open_cells:
         x, y = int(x//SPLIT), int(y//SPLIT)
         print(x,y)

    # Initial Robot and Mouse
    rd.shuffle(open_cells)
    robot_location = open_cells[0]
    mouse_1_location = open_cells[1]
    
    robot_position = (int(robot_location[1] // SPLIT), int(robot_location[0] // SPLIT))
    mouse_1_position = (int(mouse_1_location[1] // SPLIT), int(mouse_1_location[0] // SPLIT))
      
    test_surface.fill("whitesmoke")
    screen.blit(test_surface,robot_location[0:2])
    ship[robot_position[0]][robot_position[1]] = 'R'

    test_surface.fill("chartreuse")
    screen.blit(test_surface,mouse_1_location[0:2])
    ship[mouse_1_position[0]][mouse_1_position[1]] = 'M'
    run =True
    step_counter = 0
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                # If user presses X, stop the program
                pygame.quit()
        pygame.display.update()
        # Increment, find new robot  
        _, new_robot_position = search_button_increment.search_button_increment(ship, robot_position, mouse_1_position, alpha)

        # Robot has no path to the button, self-destruct. 
        if True and False:
             pygame.quit()  
          #    with open(r'C:\Users\vsh00\OneDrive - Rutgers University\python\AI-Project\IAL-Projects\Project 1\DataFiles\robot_data.csv', 'a', newline='') as file:
          #         writer = csv.writer(file)
          #         writer.writerows([[robot_type, d, q, step_counter, new_fire_positions]])
          #         print("written", new_fire_positions)
          #    run = False
             break

        x,y = robot_position
        ship_surfaces_dict[(y*SPLIT,x*SPLIT)]
        ship[x][y] = 'O'
        test_surface.fill("orchid")
        screen.blit(test_surface,(y*SPLIT,x*SPLIT))

        x,y = new_robot_position
        ship_surfaces_dict[(y*SPLIT,x*SPLIT)]
        ship[x][y] = 'R'
        test_surface.fill("whitesmoke")
        screen.blit(test_surface,(y*SPLIT,x*SPLIT))
        robot_position = new_robot_position
        pygame.time.wait(50)
        step_counter+=1

        clock.tick(60) # Set framerate
    pygame.quit()

if __name__ == "__main__":
  main()
