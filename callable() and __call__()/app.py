class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, x):
        return x * self.factor
        
if __name__ == "__main__":
    m = Multiplier(5)
    print(callable(m))  
    print(m(10))        
