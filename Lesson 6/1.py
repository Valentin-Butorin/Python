from time import sleep
from colorama import Fore


class TrafficLight:
    __color = [[Fore.RED + 'Red', 7], [Fore.YELLOW + 'Yellow', 2], [Fore.GREEN + 'Green', 7]]

    def running(self):
        while True:
            for color, timer in self.__color:
                print(color)
                sleep(timer)


traffic_light = TrafficLight()
traffic_light.running()
