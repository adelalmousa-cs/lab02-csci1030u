# Fill in the body of each function below (look for the TODO comments).
#
# The function names and their arguments are already written for you - do NOT
# rename them or change their arguments, because the automated tests call them by
# name. Just replace each `pass` with your code, using `return` to send the answer
# back (not `print`).


def seconds_to_hms(total_seconds):
    # TODO (Part 1): return the time as a string "H:MM:SS"
    #   e.g. seconds_to_hms(3661) should return "1:01:01"
    seconds_to_hms = total_seconds % 60
    total_minutes = total_seconds // 60
    minutes_to_hms = total_minutes % 60
    hours_to_hms = total_minutes // 60    
    return f"{hours_to_hms}:{minutes_to_hms:02d}:{seconds_to_hms:02d}"

print(f'Lab part 1:')
print(seconds_to_hms(3661))   # returns "1:01:01"
print(seconds_to_hms(59))     # returns "0:00:59"
print(seconds_to_hms(7325))   # returns "2:02:05"
print(f'\n')


def admission_price(age):
    # TODO (Part 2): return the ticket price (a number) for someone of this age
    price: float = 0

    if age < 5:
        price = 0
        print(f"Admission price for age {age} is ${price:.2f}")
    elif age >= 5 and age <= 12: 
        price = 8
        print(f"Admission price for age {age} is ${price:.2f}")
    elif age >= 13 and age <= 64:
        price = 15
        print(f"Admission price for age {age} is ${price:.2f}")
    elif age >= 65:
        price = 10
        print(f"Admission price for age {age} is ${price:.2f}")
    else:
        print(f'Enter valid age')
    
    return price
print(f'Lab part 2:')
admission_price(65)  # returns $10.00
print(f'\n')


def sum_multiples(limit):
    # TODO (Part 3): return the sum of every whole number below `limit`
    #   that is a multiple of 3 or of 5

    total = 0
    for i in range(limit):
        if i % 3 == 0 or i % 5 == 0:
            total += i
    return total

print(f'Lab part 3:')
print(sum_multiples(10))  # returns 23
print(sum_multiples(20))  # returns 78
print(sum_multiples(1))   # returns 0
print(f'\n')


def total_of_positives(numbers):
    # TODO (Part 4 - STRETCH, optional): return the sum of just the
    #   positive numbers in the list `numbers`]
    total = 0
    for num in numbers:
        if num >0:
            total += num
    return total

print(f'Lab part 4:')
print(total_of_positives([1, -2, 3]))  # returns 4
print(total_of_positives([-1, -2, -3]))  # returns 0
print(total_of_positives([0, 1, 2,  3]))  # returns 6


print(f'\nLab Final Tests:')
def main():
    # Optional scratch space - use this to try your functions with sample values.
    # Uncomment a line and run `python lab02.py` to see the result.
    print(seconds_to_hms(3661))            # 1:01:01
    print(admission_price(10))             # 8
    print(sum_multiples(10))               # 23
    print(total_of_positives([1, -2, 3]))  # 4
    pass


if __name__ == "__main__":
    main()
