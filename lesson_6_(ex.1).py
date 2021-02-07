from time import sleep
from termcolor import cprint

class TrafficLight:
    __color = {"Красный": ["red", 7], "Желтый_кр": ["yellow", 2], "Зеленый": ["green", 7], "Желтый_зел": ["yellow", 2]}

    def running(self):
        for i in TrafficLight.__color:
            cprint(TrafficLight.__color.get(i)[0], TrafficLight.__color.get(i)[0])
            sleep(TrafficLight.__color.get(i)[1])

class TrafficLight1(TrafficLight):
    def running1(self):
        print("Это метод из дочернего класса")

a = TrafficLight1()
a.running1()
while True:
    a.running()
