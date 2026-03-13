def table_generator(number):
    print("-----------------")
    for counter in range(1,11):
        print(f"  {number} * {counter:2} = {number * counter:3}")

while True:
    try:
        number = int(input("Please enter a number(1-12): "))
        if 1 <= number <= 12:
            table_generator(number)
            break
        else:
            print("Error ==> Please enter a number between 1 and 12")
    except ValueError:
        print("Error ==> This is not a valid number. Try again.")

print("All tables for numbers between 1 and 12")
for i in range(1,13):
    table_generator(i)