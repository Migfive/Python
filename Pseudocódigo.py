def adult():
    definition = input("What is your age ")
    print(definition)
    if int(definition) < 18:
        print("Your age is too young")
    else:
        print("Your age is good, you are adult")

    return "Program end"


print(adult())
