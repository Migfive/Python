def find_voume(length=1, width=1, depth=1):
    return length * width * depth, width, 'hola'


result, width, text = find_voume(width=10)
print(result)
print(width)
print(text)
