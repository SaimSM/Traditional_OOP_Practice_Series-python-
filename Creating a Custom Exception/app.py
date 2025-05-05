class InvalidAgeError(Exception):
    pass

def check_age(age):
    if age < 18:
        raise InvalidAgeError(f"Age {age} is not valid; must be ≥ 18")

if __name__ == "__main__":
    try:
        check_age(16)
    except InvalidAgeError as e:
        print("Caught exception:", e)
