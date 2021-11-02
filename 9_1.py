import time
class TrafficLight:
    __color=[["red", 7,31], ["yellow", 2,33], ["green", 10,32]]
    def running(self):
        iter=0
        vect=1
        while True:
            print(f'\r\033[{self.__color[iter][2]}m{self.__color[iter][0]}',end='')
            time.sleep(self.__color[iter][1])
            if iter==2:
                vect=-1
            if iter==0:
                vect=1
            iter+=vect

svet=TrafficLight()
svet.running()


