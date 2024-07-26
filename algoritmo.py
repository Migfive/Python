def main():
    numbers = []
    while True:
        num = int(input("Enter a number (0 is end): "))
        if num == 0:
            break

        numbers.append(num)
        if numbers:
            suma = sum(numbers)
            media = suma/len(numbers)
            print(f"The sum of all numbers is {suma}")
            print(f"The average of all numbers is {media}")

        else:
            print("No numbers entered")


main()




