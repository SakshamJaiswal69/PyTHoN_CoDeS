class calculator :
    def __init__(self,num):
        self.number = num

    def square (self):
        print(f"the square of {self.number} is {self.number **2}")
        
    def squareRoot (self):
        print(f"the squareRoot of {self.number} is {self.number **0.5}")
        
    def cube (self):
        print(f"the cube of {self.number} is {self.number **3}")

a = calculator(int(input("enter a number :")))
a.square()
a.squareRoot()
a.cube()