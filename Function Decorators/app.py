def log_function_call(fn):
    def wrapper(*args, **kwargs):
        print("Function is being called")
        return fn(*args, **kwargs)
    return wrapper

@log_function_call
def say_hello():
    print("Hello!")

if __name__ == "__main__":
    say_hello()
