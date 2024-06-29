import pygame, random as rd, math, heapq, csv, os
from collections import defaultdict, OrderedDict
from functions import create_ship, search_button_increment, sense, update_probability, stochastic_mouse


def main(): 
    pygame.init()
    d = 41
    mice_type = 2   # 1 for stationary, 2 for stochastic
    alpha = .11
    #rd.seed(3) # Set random seed (same result each run)
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
                     #open_cells.append(coordinates)
                     open_cells.append((round(coordinates[1]/SPLIT), round(coordinates[0]/SPLIT)))
    pygame.display.update()
    # Initial Robot and Mouse
    rd.shuffle(open_cells)
    robot_location = open_cells[0]
    mouse_1_location = open_cells[1]
    
    ship_probabilities = {} # Probabilities of mouse being in each given square
    starting_probability = 1 / (len(open_cells) - 1) # At the start, the mouse can be in any open square other than the robot square
    for x,y in open_cells[1:]:  
         ship_probabilities[(x,y)] = starting_probability   # Set all of them to each other


    ship_probabilities = dict(sorted(list(ship_probabilities.items()), key = lambda x: x[0]))

    robot_position = robot_location
    mouse_1_position = mouse_1_location
      
    test_surface.fill("whitesmoke")
    screen.blit(test_surface,(int(robot_position[1]*SPLIT), int(robot_position[0]*SPLIT)))
    ship[robot_position[0]][robot_position[1]] = 'R'
    ship_probabilities[robot_position] = 0 

    test_surface.fill("chartreuse")
    screen.blit(test_surface,(int(mouse_1_position[1]*SPLIT), int(mouse_1_position[0]*SPLIT)))
    ship[mouse_1_position[0]][mouse_1_position[1]] = 'M'
    path = search_button_increment.search_button_increment(ship, robot_position, mouse_1_position, 
                                                                    ship_probabilities, alpha)
    end = False
    run =True
    step_counter = 0
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                # If user presses X, stop the program
                pygame.quit()
        pygame.display.update()
        
        # Increment 
        if len(path)==0:   # If the bot has moved to the spot with the highest probability, sense.
            print("Sense")
            if sense.sense(robot_position,mouse_1_position,alpha): # Sense. 
                update_probability.update_probability_beep(ship_probabilities, robot_position, alpha) # Update probabilities given a beep
            else: # No beep so update probabilities
                update_probability.update_probability_no_beep(ship_probabilities, robot_position, alpha) 
            path = search_button_increment.search_button_increment(ship, robot_position, mouse_1_position, 
                                                                                ship_probabilities, alpha)

        new_robot_position = path[0]
        ship_probabilities[new_robot_position] = 0
        path.pop(0)

        x,y = robot_position
        ship[x][y] = 'O'
        test_surface.fill("orchid")
        screen.blit(test_surface,(y*SPLIT,x*SPLIT))
       
        x,y = new_robot_position
        if ship[x][y]=='M':
             end = True

        ship[x][y] = 'R'
        test_surface.fill("whitesmoke")
        screen.blit(test_surface,(y*SPLIT,x*SPLIT))
        robot_position = new_robot_position 

        if mice_type == 2:
            new_mouse_position = stochastic_mouse.stochastic_mouse(ship, mouse_1_position)

            x, y = mouse_1_position
            ship[x][y] = 'O'
            test_surface.fill("orchid")
            screen.blit(test_surface,(y*SPLIT,x*SPLIT))

            test_surface.fill("chartreuse")
            screen.blit(test_surface,(int(new_mouse_position[1]*SPLIT), int(new_mouse_position[0]*SPLIT)))
            ship[new_mouse_position[0]][new_mouse_position[1]] = 'M'

            mouse_1_position = new_mouse_position
            ship_probabilities = stochastic_mouse.stochastic_update_probability(ship, ship_probabilities)

            


        if end:
             pygame.quit()  
          #    with open(r'C:\Users\vsh00\OneDrive - Rutgers University\python\AI-Project\IAL-Projects\Project 1\DataFiles\robot_data.csv', 'a', newline='') as file:
          #         writer = csv.writer(file)
          #         writer.writerows([[robot_type, d, q, step_counter, new_fire_positions]])
          #         print("written", new_fire_positions)
          #    run = False
             break
        pygame.time.wait(100)
        step_counter+=1
        clock.tick(60) # Set framerate
    pygame.quit()

if __name__ == "__main__":
  main()
