def load_file(day):
    
    with open(f"day{str(day)}_input.txt", "r") as f:
        
        data = [int(i) for i in f.read().split(",")]
        return data
    
def calculate_next_day(data):
    
    for timer in range(len(data)):
        
        if data[timer] == 0:
            data[timer] = 6
            data.append(8)
        else:
            data[timer] -= 1
    
    return data
    
data = load_file(6)

for day in range(80):
    data = calculate_next_day(data)
    
print(len(data))
