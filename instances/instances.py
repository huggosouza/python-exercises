import os

class Car():
    def __init__(self):
        self.color = input("Type the color of the car: ")
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

for i in range(0, len(carList)):
    carList[i].printall()
