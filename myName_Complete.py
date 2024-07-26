# Exercise_18
my_name = input("Enter your name: ")
complete = [name.capitalize() for name in my_name.split(' ')]
initials = ''.join([name[0] for name in complete])
print("Initials:", initials)
