class Road:
    def __init__(self, length, width):
        self.__length = length
        self.__width = width
    def mass(self,depth=1,weight=25,):
        return (self.__length*self.__width*weight*depth)/1000
road_1=Road(5000,20)
print(road_1.mass(5))
print(road_1.mass())


