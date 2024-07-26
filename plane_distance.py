import math
import matplotlib.pyplot as plt

# Exercise_12

value_one = input("Enter a values x1, y1, x2, y2: ")

value_total = [float(values) for values in value_one.split(',')]


class Diagram:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def operations(self):
        result = math.sqrt((self.x2 - self.x1) ** 2 + (self.y2 - self.y1) ** 2)
        return result


diagram = Diagram(value_total[0], value_total[1], value_total[2], value_total[3])
distance = diagram.operations()

# print of the result operation
print(f"The distance between the points is: {distance}")

# display
plt.figure()

# display the punts
plt.plot([diagram.x1, diagram.x2], [diagram.y1, diagram.y2], 'ro')  # Puntos en rojo
plt.plot([diagram.x1, diagram.x2], [diagram.y1, diagram.y2], 'b-')  # Línea en azul

# labels
plt.text(diagram.x1, diagram.y1, f'({diagram.x1}, {diagram.y1})', fontsize=12, ha='right')
plt.text(diagram.x2, diagram.y2, f'({diagram.x2}, {diagram.y2})', fontsize=12, ha='left')

# add title and other
plt.title('Distance Between Two Points')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

# see of distance
midpoint_x = (diagram.x1 + diagram.x2) / 2
midpoint_y = (diagram.y1 + diagram.y2) / 2
plt.text(midpoint_x, midpoint_y, f'Distance: {distance:.2f}', fontsize=12, ha='center', va='bottom')

# display graphic
plt.grid()
plt.show()

