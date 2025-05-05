class Car:
    def __init__(self, brand):
        self.brand = brand 

    def start(self):       
        print(f"{self.brand} engine started.")
if __name__ == "__main__":
    my_car = Car("Toyota")
    print(my_car.brand)  
    my_car.start()       
