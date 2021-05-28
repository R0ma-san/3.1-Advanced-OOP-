from abc import ABC, abstractmethod


class Shape(ABC):

    @abstractmethod
    def calculate_area(self):
        pass
 

class Rectangle(Shape):

    def __init__(self, *args):
        self.length = args[0]
        self.height = args[1]
        try:
            self.__color = args[2]
        except:
            self.__color = 'Black'

    def calculate_area(self):
        self.area = self.length*self.height
    
    def show_color(self):
        return self._Rectangle__color
    
    def __eq__(self, other1, other2):
        return self.area == other1.area and self.area == other2.area
    def __ne__(self, other1, other2):
        return self.area != other1.area and self.area != other2.area
    def __lt__(self, other1, other2):
        return self.area < other1.area and self.area < other2.area
    def __gt__(self, other1, other2):
        return self.area > other1.area and self.area > other2.area
    def __le__(self, other1, other2):
        return self.area <= other1.area and self.area <= other2.area
    def __ge__(self, other1, other2):
        return self.area >= other1.area and self.area >= other2.area 

class Triangle(Shape):

    def __init__(self, *args):
        self.length = args[0]
        self.height = args[1]
        try:
            self.__color = args[2]
        except:
            self.__color = 'Black'

    def calculate_area(self):
        self.area = self.length*self.height/2

    def show_color(self):
        return self._Triangle__color

    def __eq__(self, other1, other2):
        return self.area == other1.area and self.area == other2.area
    def __ne__(self, other1, other2):
        return self.area != other1.area and self.area != other2.area
    def __lt__(self, other1, other2):
        return self.area < other1.area and self.area < other2.area
    def __gt__(self, other1, other2):
        return self.area > other1.area and self.area > other2.area
    def __le__(self, other1, other2):
        return self.area <= other1.area and self.area <= other2.area
    def __ge__(self, other1, other2):
        return self.area >= other1.area and self.area >= other2.area 


class Circle(Shape):
    
    def __init__(self, *args):
        self.radius = args[0]
        try:
            self.__color = args[1]
        except:
            self.__color = 'Black'

    def calculate_area(self):
        pi = 3.14
        self.area = pi*self.radius**2
    
    def show_color(self):
        return self._Circle__color

    def __eq__(self, other1, other2):
        return self.area == other1.area and self.area == other2.area
    def __ne__(self, other1, other2):
        return self.area != other1.area and self.area != other2.area
    def __lt__(self, other1, other2):
        return self.area < other1.area and self.area < other2.area
    def __gt__(self, other1, other2):
        return self.area > other1.area and self.area > other2.area
    def __le__(self, other1, other2):
        return self.area <= other1.area and self.area <= other2.area
    def __ge__(self, other1, other2):
        return self.area >= other1.area and self.area >= other2.area 


