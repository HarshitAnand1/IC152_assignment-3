# Part a
def float_check():
    x = float(input("Enter a floating point number: "))

    if x > 10 or x ==10:
        print("High")

    else:
        print("Low")

# Part b
def int_sign():
    num = int(input("Enter an integer: "))

    if num > 0:
        print("Positive")
    elif num == 0:
        print("Zero")
    else:
        print("Negative")


# Part c
def text_case():
    text = input("Enter a string: ")

    if text == text.lower():
        print("the given text only contains lowercase letters")
    if text == text.upper():
        print("the given text only contains uppercase letters")
    else:
        print("the given text contains both uppercase and lowercase letters")

# Part d
def day_letter():
    day = input("Enter the name of a day: ")

    print(f"The day name contains {len(day)} letters")

# Part e
def num_avg():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    c = int(input("Enter third number: "))

    avg = (a+b+c)/3
    print(f"The average is{avg}")

float_check()
int_sign()
text_case()
day_letter()
num_avg()