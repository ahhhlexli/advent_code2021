def load_file(day):
    
    with open(f"day{str(day)}_input.txt", "r") as f:
        
        data = [(i.split(" ")[0], int(i.split(" ")[1].strip("\n"))) for i in f.readlines()]
        return data
    

def calculate_positions(data):
    
    horizontal_position = 0
    depth_position = 0
    
    for move in data:
        if "forward" in move:
            horizontal_position += move[1]
        elif "up" in move:
            depth_position -= move[1]
        elif "down" in move:
            depth_position += move[1]
    
    return horizontal_position, depth_position

data = load_file(2)
horizontal_position, depth_position = calculate_positions(data)

print(horizontal_position * depth_position)