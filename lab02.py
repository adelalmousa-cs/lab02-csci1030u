# Fill in the body of each function below (look for the TODO comments).
#
# The function names and their arguments are already written for you - do NOT
# rename them or change their arguments, because the automated tests call them by
# name. Just replace each `pass` with your code, using `return` to send the answer
# back (not `return`).


def seconds_to_hms(total_seconds):
    # TODO (Part 1): return the time as a string "H:MM:SS"
    #   e.g. seconds_to_hms(3661) should return "1:01:01"
    seconds = total_seconds % 60
    total_minutes = total_seconds // 60
    minutes = total_minutes % 60
    hours = total_minutes // 60
    return f"{hours}:{minutes:02d}:{seconds:02d}"


print("Lab part 1:")
print(seconds_to_hms(3661))  # 1:01:01
print(seconds_to_hms(59))    # 0:00:59
print(seconds_to_hms(7325))  # 2:02:05
print()


def admission_price(age):
    # TODO (Part 2): return the ticket price (a number) for someone of this age
    if age < 5:
        return 0
    elif age <= 12:
        return 8
    elif age <= 64:
        return 15
    elif age >= 65:
        return 10
    else:
        return 0


print("Lab part 2:")
print(admission_price(4))   # 0
print(admission_price(10))  # 8
print(admission_price(20))  # 15
print(admission_price(65))  # 10
print()


def sum_multiples(limit):
    # TODO (Part 3): return the sum of every whole number below `limit`
    #   that is a multiple of 3 or of 5

    total = 0
    for i in range(limit):
        if i % 3 == 0 or i % 5 == 0:
            total += i
    return total


print("Lab part 3:")
print(sum_multiples(10))  # 23
print(sum_multiples(20))  # 78
print(sum_multiples(1))   # 0
print()


def total_of_positives(numbers):
    # TODO (Part 4 - STRETCH, optional): return the sum of just the
    #   positive numbers in the list `numbers`]
    total = 0
    for num in numbers:
        if num >0:
            total += num
    return total


print("Lab part 4:")
print(total_of_positives([1, -2, 3]))      # 4
print(total_of_positives([5, 0, -3, 7]))   # 12
print(total_of_positives([]))               # 0
print()


def main():
    # Optional scratch space - use this to try your functions with sample values.
    # Uncomment a line and run `python lab02.py` to see the result.
    return (
        seconds_to_hms(3661),            # 1:01:01
        admission_price(10),             # 8
        sum_multiples(10),               # 23
        total_of_positives([1, -2, 3]),  # 4
    )


if __name__ == "__main__":
    main()
