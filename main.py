import pygame
import math
from Djirskta import *

WIDTH, HEIGHT = 900,500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Djirksta's Algorithm")

WHITE = (255, 255, 255)

FPS = 60

GREEN_POS = (WIDTH * .75, HEIGHT/2)

GREEN = (0,255,0)
end_point = pygame.Rect(GREEN_POS[0], GREEN_POS[1], 50,50)

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
    #pygame.draw.circle(WIN, (0, 255, 0), GREEN_POS, 10)
    pygame.draw.rect(WIN, GREEN, end_point)


    # draw all the lines

    for line_array in lines_dict.keys():
        for num in range(len(lines_dict[line_array])):
            pygame.draw.line(lines_dict[line_array][num].get_surface(), lines_dict[line_array][num].get_color(),
                             lines_dict[line_array][num].get_start_pos(), lines_dict[line_array][num].get_end_pos())

    # draw all the circles

    for circles_array in circles_dict.keys():
        for num in range(len(circles_dict[circles_array])):
            pygame.draw.circle(circles_dict[circles_array][num].get_surface(), circles_dict[circles_array][num].get_color(),
                               circles_dict[circles_array][num].get_pos(), circles_dict[circles_array][num].get_width())



    pygame.display.update()

def pass_list(lines,circles):

    line_dictionary = lines.copy()
    mega_dict = {}
    shortest_path_dict = {}

    # take each route from the lines dictionary and pass their respective distances into a new dictionary
    for line_array in line_dictionary.keys():
        for num in range(len(line_dictionary[line_array])):
            mega_dict.update({line_dictionary[line_array][num].get_id(): line_dictionary[line_array][num].get_length()})

    # take each circle array and pass their ids into a dictionary for Djirksta's algorith
    for circle_array in circles.keys():
        for num in range(len(circles[circle_array])):

            if circles[circle_array][num].get_id() == "A":
                shortest_path_dict.update( {circles[circle_array][num].get_id(): 0})
            else:
                shortest_path_dict.update( {circles[circle_array][num].get_id(): math.inf})

    # set the rect cost to inf
    shortest_path_dict.update({"Z": math.inf})

    # return the dictionaries
    return mega_dict, shortest_path_dict


def main():

    clock = pygame.time.Clock()

    run = True
    run_through = False

    array_num = 0
    circles, lines  = {},{}



    # add all of one route to a list - done
    # stop program after two routes in list_of_routes - done
    # calculate distances from each circle - done
    # display the distances (maybe)
    # |-> make the distances between different links longer or shorter
    # pass the list of distances to Djirksta
    # return the best path
    # change the best route to green


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

                # handle the connection of different circles
                if event.type == pygame.MOUSEBUTTONUP and array_num >= 2:
                    pos = pygame.mouse.get_pos()

                    # loop through the circles to check if they have been clicked
                    # if circle has been clicked get its pos
                    # when second cirlce has been clicked draw line between previous circle and current circle
                    # add this line to one of the routes

        # once the routes have been finished, take the dict of routes, and the shortest distance from A dict and pass to Djirksta
        # update to use a button
        if array_num == 2 and run_through != True:

            #print(pass_list(lines,circles))
            tuple_of_dicts = pass_list(lines, circles)

            best_path = Djirksta_Alg(tuple_of_dicts[0], tuple_of_dicts[1])

            # search through the route list and if the route matches change the color to Green
            for line_array in lines.keys():

                for num in range(len(lines[line_array])):
                    if lines[line_array][num].get_id() in best_path:
                        lines[line_array][num].set_color(GREEN)


            # Only make the algorithm run once
            run_through = True

        # draw everything to the screen
        draw_window(circles,lines, array_num)

    pygame.quit()


if __name__ == "__main__":
    main()
