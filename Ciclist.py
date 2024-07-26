# Exercise_17
cyclist = input("Clock of star rute HH:MM:SS: ")
List_cyclist = [int(cycle) for cycle in cyclist.split(":")]

# TODO conversion of horus a minute

time_travel = input("How long do you travel for? HH:MM:SS: ")
list_travel = [int(time_travel) for time_travel in time_travel.split(":")]


class Out_time:
    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def travel(self):
        if self.hours > 24 or self.minutes > 60 or self.seconds > 60:
            raise TypeError("You Clock is Ok?")

        total_seconds = int(self.hours * 3600 + self.minutes * 60 + self.seconds)
        return total_seconds


class Children_cyclist:
    def __init__(self, routes):
        self.route = routes

    def route_travel(self):
        total_hours = int(self.route // 3600)
        hours = total_hours % 24
        minutes = int((self.route // 60) % 60)
        seconds = int(self.route % 60)

        print(f"Your arrival time is {hours:02}:{minutes:02}:{seconds:02}")


route = Out_time(list_travel[0], list_travel[1], list_travel[2])
cyclist_Travel = Out_time(List_cyclist[0], List_cyclist[1], List_cyclist[2])

if route and cyclist_Travel:
    sum_Total = route.travel() + cyclist_Travel.travel()

    enter = Children_cyclist(sum_Total)

    print(enter.route_travel())


