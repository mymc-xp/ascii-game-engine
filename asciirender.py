#screenclear imports
import os
import platform
#screenclear instance
clear = lambda: os.system("cls") if platform.system() == "Windows" else lambda: os.system("clear")
#

class asciibox:
    def __init__(self, width, height, value = None, dr = "", buffer = 1, layering = None):    
        grid = {}
        for x in range(width):
            for y in range(height):
                grid[x,y] = []
                if value != None:
                    grid[x,y].append(value)
        self.grid = grid
        self.coords = grid.keys()
        self.points = []
        self.width = width
        self.height = height
        self.auto_update = False
        self.dr = dr #default render for empty coordinate
        self.buffer = buffer
        self.layering = layering
        self.render = ""
        self.update()
    #
    def __str__(self):
        return(self.render)
    #
    def add(self, points, values):#add value to point coordinate
        #input check
        if len(points) != len(values):
            if len(values) == 1 or values == "":
                values = [values for coordinate in range(len(points))]
            else:
                print( "invalid amount of values")
                sys.exit(0)
        #adds a list of values to a grid
        index = 0
        for coordinate in points:#probably want to enumerate to simplifly
            self.grid[coordinate].append(values[index])
            index += 1
        self.__auto_update()
    #
    def remove(self, points, values = None, default = " "):#removes 1st instance of a value in a point
        if len(points) != len(values):
            if len(values) == 1 or values == "":
                values = [values for coordinate in range(len(points))]
            else:
                print( "invalid amount of values")
                sys.exit(0)
        #adds a list of values to a grid
        index = 0
        for coordinate in [x for x in points if x in self.coords]:
            if values == None:
                self.grid[coordinate] = [default]
            else:
                for v in values:
                    if v in self.grid[coordinate]:
                        self.grid[coordinate].remove(v)
            index += 1
        self.__auto_update()
    #
    def replace(self, points, values):#replace all values in points with new values
        if len(points) != len(values):
            if len(values) == 1 or values == "":
                values = [values for coordinate in range(len(points))]
            else:
                print( "invalid amount of values")
                sys.exit(0)
        #adds a list of values to a grid
        index = 0
        for coordinate in [x for x in points if x in self.coords]:
            storage = [values[index]]
            if type(values[index]) == list:
                storage = [*values[index]]
            self.grid[coordinate] = storage
            index += 1
        self.__auto_update()
    #
    def __sort_layer(self, values):
        if self.layering == None:
            if values == []:#
                return self.dr
            else:
                return values[0]
        for v in self.layering:#return 1st item in values list
            if v in values:
                return v
        if len(values) == 0:
            return self.dr
        else:
            return values[0]
    #
    def update(self):#updates the rendering for display
    #returns a text representation of the grid based on the data inside it
        width = self.width
        height = self.height
        text = ""
        for y in range(height - 1, -1, -1):
            for x in range(width):
                top = self.__sort_layer(self.grid[x,y])
                text += self.dr + " " * self.buffer if top == "" else top + " " * self.buffer
            text += "\n"
        text = text[:len(text) - 1]
        #removes the last "\n" character from the render
        self.render = text
    def __auto_update(self):
        if self.auto_update:
            self.update()