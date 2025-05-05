class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print(f"{self.name} says: Woof!")

if __name__ == "__main__":
    d = Dog("Buddy", "Beagle")
    d.bark()
