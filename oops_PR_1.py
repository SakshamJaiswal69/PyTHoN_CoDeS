#create a class program to store details for progarammers of micrrosoft company.
class Programmer:
    company = "Microsoft"
#this is a constructor method and these are the some arguments which we are going to use
    def __init__(self, name, product, language):
        self.name = name
        self.product = product
        self.language = language
    
    def getInfo(self):
        print(f"The name of Employee is {self.name} and he is Working on this {self.product} and tha major Language he uses {self.language}")
    
#creating an object of class
"""
saksham = Programmer("Saksham", "Windows", "C++")
shivansh = Programmer("Shivansh", "bussiness model AI", "Python")
suransh = Programmer("Suransh", "Azure", "Java")
aditya = Programmer("Aditya", "Microsoft Office", "C#")
"""
saksham = Programmer("Saksham", "Windows", "C++")
shivansh = Programmer("Shivansh", "bussiness model AI", "Python")
suransh = Programmer("Suransh", "Azure", "Java")
aditya = Programmer("Aditya", "Microsoft Office", "C#")
#we can also make this by user input

#creating a list of objects
saksham.getInfo()
shivansh.getInfo()
suransh.getInfo()
aditya.getInfo()