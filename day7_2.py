def load_file(day):
    
    with open(f"day{str(day)}_input.txt", "r") as f:
        
        data = [int(i) for i in f.read().split(",")]
        return data
    
def find_closest_alignment(data):
    
    min_fuel = max(data)**10
    
    for num in range(max(data)):
        
        fuel = 0
        
        for crab in data:   
            distance = abs(crab - num)    
            fuel += sum(range(distance+1))
            
        if fuel < min_fuel:
            min_fuel = fuel
            
    return min_fuel
    
data = load_file(7)
minimum_fuel_use = find_closest_alignment(data)
print(minimum_fuel_use)