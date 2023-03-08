import random
number = random.randint(-10000, 10000)
last_digit = abs(number) % 10
script = f"Last digit of {number} is {last_digit} and is"
script_negative = f"Last digit of {number} is {0 - last_digit} and is"
if number >= 0:
    if last_digit == 0:
        print(f"{script} 0")
    elif last_digit < 6:
        print(f"{script} less than 6 and not 0")
    else:
        print(f"{script} greater than 5")
else:
    print(f"{script_negative} less than 6 and not 0")
