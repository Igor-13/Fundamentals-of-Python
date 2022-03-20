# Создание класса сфетофор
import time


class TrafficLight:

    def __init__(self):
        self.__color = ['red', 'yellow', 'green']

    def running(self, counter=0):
        while counter < 3:
            if counter == 0:
                print(self.__color[counter])
                counter += 1
            elif counter == 1:
                time.sleep(7)
                print(self.__color[counter])
                counter += 1
            elif counter == 2:
                time.sleep(2)
                return self.__color[counter]

            else:
                return None


traffic_lights = TrafficLight()
print(traffic_lights.running())
