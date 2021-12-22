def load_file(day):
    
    with open(f"day{str(day)}_input.txt", "r") as f:
        
        data = [int(i) for i in f.read().split(",")]
        return data
    
def calculate_next_day(current_day):
    
    next_day = {
        0: current_day[1],
        1: current_day[2],
        2: current_day[3],
        3: current_day[4],
        4: current_day[5],
        5: current_day[6],
        6: current_day[7],
        7: current_day[8],
        8: current_day[0]
    }
    
    if current_day[0] > 0:
        next_day[6] += current_day[0]
    
    current_day = next_day
    
    return current_day
    
data = load_file(6)

current_day = {
    0: data.count(0),
    1: data.count(1),
    2: data.count(2),
    3: data.count(3),
    4: data.count(4),
    5: data.count(5),
    6: data.count(6),
    7: data.count(7),
    8: data.count(8)
}

for day in range(256):
    current_day = calculate_next_day(current_day)
    
print(sum(current_day.values()))