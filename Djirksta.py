import pygame
import sys
from Djirskta import *

pygame.init()

WIDTH, HEIGHT = 900,500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Djirksta's Algorithm")

WHITE = (255, 255, 255)
RADIUS = 10
FPS = 60
BUTTON_DEST = (WIDTH * .70, HEIGHT * .80)

GREEN_POS = (WIDTH * .75, HEIGHT/2)
GREEN = (0,255,0)
LIGHT_SHADE = (170,170,170)

smallfont = pygame.font.SysFont('Corbel', 35)
text = smallfont.render('Calculate Path!', True,
                        (0,0,0))

end_point = pygame.Rect(GREEN_POS[0], GREEN_POS[1], 50,50)
button = pygame.Rect(BUTTON_DEST[0], BUTTON_DEST[1], 185,25)

class Circle():

    ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    counter = 0

    def __init__(self, surface, color, pos, width):
        self.surface = surface
        self.color = color
        self.pos = pos
        self.width = width

        self.id = Circle.ALPHABET[Circle.counter:Circle.counter + 1]
        Circle.counter += 1

    def get_color(self):
        return self.color

    def get_surface(self):
        return self.surface

    def get_pos(self):
        return self.pos

    def get_width(self):
        return self.width

    def get_id(self):
        return self.id



class Lines():

    #define method to cacluate the distance of lines
    def __init__(self, surface, color, start_pos, end_pos, id):
        self.surface = surface
        self.color = color
        self.start_pos = start_pos
        self.end_pos = end_pos
        self.id = id

    def __str__(self):
        return self.id

    def set_color(self, color):
        self.color = color

    def get_color(self):
        return self.color

    def get_surface(self):
        return self.surface

    def get_start_pos(self):
        return self.start_pos

    def get_end_pos(self):
        return self.end_pos

    def get_length(self):
        return math.sqrt((self.end_pos[0] - self.start_pos[0]) ** 2) + (math.sqrt((self.end_pos[1] - self.start_pos[1]) ** 2))

    def get_id(self):
        return self.id


def draw_window(circles_dict, lines_dict, num_array):

    WIN.fill(WHITE)
    pygame.draw.rect(WIN, GREEN, end_point)
    pygame.draw.rect(WIN, LIGHT_SHADE, button)
    WIN.blit(text, BUTTON_DEST)

    # draw all the lines

    for key in lines_dict:
        for lines in lines_dict[key]:
            pygame.draw.line(lines.get_surface(), lines.get_color(), lines.get_start_pos(), lines.get_end_pos())

    # draw all the circles
    for key in circles_dict:
        for circle in circles_dict[key]:
            pygame.draw.circle(circle.get_surface(), circle.get_color(), circle.get_pos(), circle.get_width())

    pygame.display.update()

    
def pass_list(lines,circles_dict):

    lines_dict = lines.copy()
    mega_dict = {}
    shortest_path_dict = {}

    # take each route from the lines dictionary and pass their respective distances into a new dictionary
    for key in lines_dict:
        for lines in lines_dict[key]:
            mega_dict.update({lines.get_id(): lines.get_length()})

    # take each circle array and pass their ids into a dictionary for Djirksta's algorithm
    for key in circles_dict:
        for circle in circles_dict[key]:

            if circle.get_id() == "A":
                shortest_path_dict.update( {circle.get_id(): 0})
            else:
                shortest_path_dict.update( {circle.get_id(): math.inf})

    # set the rect cost to inf
    shortest_path_dict.update({"Z": math.inf})

    # return the dictionaries
    return mega_dict, shortest_path_dict

"""
currently working on a way to connect circles after the two main routes have been established to show the real power of the algorithm
def circle_id_by_pos(pos, circles_dict):

    for key in circles_dict:
        for circle in  circles_dict[key]:
            print(circle, circle.get_id())
"""




def main():

    clock = pygame.time.Clock()

    run = True
    run_through = False
    clicked_once = False
    no_more = False

    start_pos = ()

    array_num = 0
    circles, lines  = {},{}

    id_circle = ""


    # add all of one route to a list - done
    # stop program after two routes in list_of_routes - done
    # calculate distances from each circle - done
    # display the distances (maybe)
    # |-> make the distances between different links longer or shorter
    # pass the list of distances to Djirksta - done
    # return the best path - done
    # change the best route to green - done


    while run:

        #setting the refresh rate
        clock.tick(FPS)


        for event in pygame.event.get():
            # checking if the x is clicked
            if event.type == pygame.QUIT:
                run = False

            # get the mouseclick
            if event.type == pygame.MOUSEBUTTONUP and array_num < 2:

                # getting the mouse position on click
                pos = pygame.mouse.get_pos()

                # handle when the route is completed
                if end_point.collidepoint(pos):

                    # draw a line from the last circle to the green box
                    lines[array_num].append(Lines(WIN, (0, 0, 0), (GREEN_POS[0] + 25, GREEN_POS[1] + 25), circles[array_num][-1].get_pos(),
                                                  circles[array_num][-1].get_id() + "Z"))

                    # increase array_num so that the lines and circles are now stored in a new array
                    array_num += 1
                    circles[array_num] = []
                    lines[array_num] = []


                else:

                    # setting up the dictionaries
                    if len(circles) == 0 and len(lines) == 0:
                        circles[array_num] = []
                        lines[array_num] = []

                    # adding the circles
                    circles[array_num].append(Circle(WIN, (255, 0, 0), pos, 10))

                    # adding the lines into an array after there are two circles
                    if len(circles[array_num]) >= 2:
                        lines[array_num].append(Lines(WIN, (0, 0, 0), pos, circles[array_num][-2].get_pos(),
                                                      circles[array_num][-2].get_id() + circles[array_num][-1].get_id()))

                    if len(circles[array_num]) == 1 and array_num > 0:
                        lines[array_num].append(Lines(WIN, (0, 0, 0), circles[array_num-1][0].get_pos(), circles[array_num][-1].get_pos(),
                                                      circles[array_num-1][0].get_id() + circles[array_num][-1].get_id()))

            # handle the connection of different circles after the two arrays have been set
            # if start pos has been set and it is after the routes have been set
            if event.type == pygame.MOUSEBUTTONUP and no_more:
                pos = pygame.mouse.get_pos()

                # check if the position of the mouse when clicked is inside of a circle and then get that circle id, pos

                # repeat to get second circle's id, pos
                # draw line between the two circles by adding line to the array of lines


                circle_id_by_pos(pos, circles)

                # once the routes have been finished, take the dict of routes, and the shortest distance from A dict and pass to Djirksta
                # update to use a button

                if button.collidepoint(pos) and run_through != True:

                    tuple_of_dicts = pass_list(lines, circles)

                    best_path = Djirksta_Alg(tuple_of_dicts[0], tuple_of_dicts[1])

                    # search through the route list and if the route matches change the color to Green
                    for key in lines:
                        for lines_ in lines[key]:
                            if lines_.get_id() in best_path:
                                lines_.set_color(GREEN)


                    # Only make the algorithm run once
                    run_through = True

        if array_num >= 2:
            no_more = True
        # draw everything to the screen
        draw_window(circles, lines, array_num)

    pygame.quit()


if __name__ == "__main__":
    main()
