from time import sleep
class TrafficLight:
    __color = ()
    def running(self):
         while True:
             print("Red")
             sleep(7)
             print("yellow")
             sleep(2)
             print("green")
             sleep(5)
             print("yellow")
             sleep(2)
a = TrafficLight()
a.running()