class Car:
    def __init__(self):
        self.newWheelNum=1
        self.newColor='red'
    def pri(self):
        print("车在跑，目标:夏威夷。")
car=Car()
car.pri()
print(car.newWheelNum,car.newColor)
del car

