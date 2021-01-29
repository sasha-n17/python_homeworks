from itertools import cycle
from time import sleep


class TrafficLight:
    __color = ['Красный', 'Жёлтый', 'Зелёный']

    def running(self, iteration):
        count = 0
        for el in cycle(TrafficLight.__color):
            print(el)
            if el == TrafficLight.__color[0]:
                sleep(7)
            elif el == TrafficLight.__color[1]:
                sleep(2)
            else:
                sleep(10)
            count += 1
            if count == iteration * len(TrafficLight.__color):
                break


test_traffic_light = TrafficLight()
test_traffic_light.running(2)
