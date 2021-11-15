try:
    value =10/0 
    number = int(input("Please enter a number "))
    print(number)

except ZeroDivisionError:
    print("Devide by 0 not allowed ")

except ValueError:
    print("Please enter a valid value")

