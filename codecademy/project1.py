import os
import math
os.system("cls")


class Moshina:
    def __init__(self,nomi) -> None:
        self.nomi = nomi
        self.petrol = 100
        self.engine = False
        self.code = 1111
        self.km = 0.102
        self.sum = 0

    def change(self,code):
        self.code = code

    def get_info(self):
        print(f"\nNomi: {self.nomi}\nBenzin: {math.ceil(self.petrol)}%\nEngine: {bool(self.engine)}")

    def switch_on(self):
        if self.engine == True:
            print("It's so turned on")
        else:
            self.engine += 1

    def switch_off(self):
        if self.engine == False:
            print("It's so turned off")
        else:
            self.engine -= 1

    def road(self):
        n = int(input("What distance do you want to drive: "))
        if n > self.petrol:
            print("There won't be enough petrol!!!")
        if self.engine == False:
            print("Turn om the machine")
        elif n <= self.petrol:
            for i in range(n):
                self.sum += self.km
            self.petrol -= self.sum
            print("Yuo've errived")

    def refill(self):
        n = int(input("Pour petrol: "))
        if (n + self.petrol) > 100:
            print(f"Extra fuel {((self.petrol + n) - 100)}")
            self.petrol = (self.petrol + n) - ((self.petrol + n) - 100)
        else:
            self.petrol += n
            print("Tank is full")

nima = Moshina("Malibu")
code1 = int(input("Enter password: "))
if code1 == nima.code:
    nima.get_info()
    while True:
        print("""
    1. Swich on 
    2. Swich off
    3. Road
    4. Refill
    5. Automatic drive
    6. Change password 
    7. Break
    """)
        number = int(input("Enter a number: "))
        if number == 1:
            nima.switch_on()
            nima.get_info()
        elif number == 2:
            nima.switch_off()
            nima.get_info()
        elif number == 3:
            nima.road()
            nima.get_info()
        elif number == 4:
            nima.refill()
            nima.get_info()
        elif number == 5:
            nima.switch_on()
            nima.road()
            nima.get_info()
        elif number == 7:
            break
        elif number == 6:
            code = int(input("Enter a new password: "))
            nima.change(code)
            nima.get_info()
 
                
