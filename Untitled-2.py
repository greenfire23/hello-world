class Vehicle():
    def __init__(self,Vtype):
        self.Vtype =Vtype


class Automobile(Vehicle):
    def __init__(self,Vtype, year, make, model, doors, roof):

        super().__init__(Vtype)
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof

IV=input("What type of vehicle :")
Iy=input("What is the year :")
Ima=input("What is the make :")
Imo=input("What is the model :")
Id=input("What is number of doors(2 or 4) :")
Ir=input("What is the roof(Solid or Sun Roof) :")
car_1=Automobile(IV,Iy,Ima,Imo,Id,Ir)






#print(f"Vehicle type: {type.Vtype}")
print(f"Vehicle type: {car_1.Vtype}")
print(f"Year: {car_1.make}")
print(f"Make: {car_1.model}")
print(f"Model: {car_1.year}")
print(f"Type of roof: {car_1.doors}")
print(f"Number of doors: {car_1.roof}")