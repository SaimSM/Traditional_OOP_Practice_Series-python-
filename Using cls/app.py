class Counter:
    count = 0

    def __init__(self):
        Counter.increment_count()

    @classmethod
    def increment_count(cls):
        cls.count += 1

    @classmethod
    def display_count(cls):
        print(f"Total objects created: {cls.count}")

if __name__ == "__main__":
    for _ in range(3):
        Counter()
    Counter.display_count()
