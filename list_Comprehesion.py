# version 1
numbers = [int(elements) for elements in range(1, 11)]
print(numbers)

numbers = [int(elements*2) for elements in range(1, 11)]
# TODO        Element     it's cycle of extraction
print(numbers)

# abbreviation
numbers_2 = [i * 2 for i in range(1, 11) if i % 2 == 0]
print(numbers_2)


