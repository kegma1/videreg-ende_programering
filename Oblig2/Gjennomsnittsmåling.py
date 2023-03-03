from datetime import datetime

def file_to_dictionary(filename):
    dict = {}
    with open(filename, "r") as f:
        for line in f.readlines():
            reg_nr, date = line.split(", ")
            dict[reg_nr] = date.strip()
    return dict

def list_speeders(file_a, file_b, speed, distance):
    a = file_to_dictionary(file_a)
    b = file_to_dictionary(file_b)

    speeders = {}

    for reg_nr in a:
        start_time = datetime.strptime(a[reg_nr], "%Y-%m-%d %H:%M:%S") 
        if reg_nr in b:
            end_time = datetime.strptime(b[reg_nr], "%Y-%m-%d %H:%M:%S") 
            tot_speed = distance / ((end_time - start_time).total_seconds() / 3600)
            if tot_speed > speed * 1.05:
                speeders[reg_nr] = (round(tot_speed, 3), str(start_time))

    return speeders

class SpeedTicket():
    def __init__(self, reg_nr, timestamp, over_speed, speed_limit ) -> None:
        self.reg_nr = reg_nr
        self.timestamp = timestamp
        self.over_speed = over_speed
        self.speed_limit = speed_limit

    def __str__(self) -> str:
        return f" Registration number:  {self.reg_nr}\n Time:  {self.timestamp}\n Speed:  {self.over_speed}km/h\n Speed limit:  {self.speed_limit}km/h"
    
    def __eq__(self, __o: object) -> bool:
        return self.reg_nr == __o.reg_nr and \
            self.timestamp == __o.timestamp and \
            self.over_speed == __o.over_speed and \
            self.speed_limit == __o.speed_limit

