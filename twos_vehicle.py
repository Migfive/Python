# Exersice 16
speed = input("Speed of the vehicle 1 and 2: ")
distance = int(input("Distance of the vehicle 1: "))

list_speed = [int(speeds) for speeds in speed.split(",")]

V1 = list_speed[0]
V2 = list_speed[1]


class Calculate:
    def __init__(self, v1, v2, distances):
        self.v1 = v1
        self.v2 = v2
        self.distance = distances

    def reach(self):
        if self.v1 <= self.v2:
            time = self.distance/(self.v2-self.v1)
            t = time*3600
            hours = int(t // 3600)
            minutes = int((t % 3600) / 60)
            seconds = int(t % 60)
            return f"Time for vehicle 1 to reach vehicle 2: {hours} hours, {minutes} minutes, and {seconds} seconds."


total_velocity = Calculate(V1, V2, distance)
print(total_velocity.reach())
