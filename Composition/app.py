class Engine:
    def start(self):
        print("Engine started.")

class Car:
    def __init__(self, engine):
        self.engine = engine

    def start(self):
        self.engine.start()

if __name__ == "__main__":
    eng = Engine()
    car = Car(eng)
    car.start()
