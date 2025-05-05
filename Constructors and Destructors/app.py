class Logger:
    def __init__(self):
        print("Logger initialized.")

    def __del__(self):
        print("Logger destroyed.")

if __name__ == "__main__":
    log = Logger()
    del log
