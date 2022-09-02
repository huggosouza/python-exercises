import os

class Car():
    def __init__(self):
        self.color = input("Type the car color:")
        self.year = input("Type the year of the car: ")
        self.carID = 0
        
    def printall(self):
            print(self.color)
            print(self.year)
    

howManyCars = int(input("How many cars do you want to input ? "))
carList = []

for i in range(0, howManyCars):
    carList.append(i)

for i in carList:
    carList[i] = Car()
    carList[i].carID = [i]


os.system("cls")
for i in range(0, len(carList)):
    print(carList[i].printall())