import numpy as np

def load_file(day):
    
    with open(f"day{str(day)}_input.txt", "r") as f:
        
        data = [i.strip("\n") for i in f.readlines()]
        return data
    
def parse_coordinate_pairs(data):
    
    coordinate_pairs = []
    for row in data:
        row_data = row.split(" -> ")
        starting_pair = [int(i) for i in row_data[0].split(",")]
        ending_pair = [int(i) for i in row_data[1].split(",")]
        coordinate_pairs.append([(starting_pair[0], starting_pair[1]),(ending_pair[0], ending_pair[1])])
        
    return coordinate_pairs

def find_valid_pairs(coordinate_pairs):
    
    valid_hor_vert_pairs = []
    valid_diag_pairs = []
    for pair in coordinate_pairs:
        if (pair[0][0] == pair[1][0]) or (pair[0][1] == pair[1][1]):
            valid_hor_vert_pairs.append(pair)
        elif abs(pair[0][0] - pair[1][0]) == abs(pair[0][1]-pair[1][1]):
            valid_diag_pairs.append(pair)
            
    return valid_hor_vert_pairs, valid_diag_pairs

def mark_hor_vert_lines(grid, valid_pairs):

    for pair in valid_pairs:

        x_difference = abs(pair[1][0] - pair[0][0])
        y_difference = abs(pair[1][1] - pair[0][1])

        min_x = min([pair[1][0],pair[0][0]])
        max_x = max([pair[1][0],pair[0][0]])
        min_y = min([pair[1][1],pair[0][1]])
        max_y = max([pair[1][1],pair[0][1]])

        if x_difference > 0:
            y_coord = pair[0][1]
            for i in range(min_x, max_x+1):
                grid[y_coord][i] += 1

        elif y_difference > 0:
            x_coord = pair[0][0]
            for i in range(min_y, max_y+1):
                grid[i][x_coord] += 1

    return grid

def mark_diag_lines(grid, valid_pairs):
    
    for pair in valid_pairs:
        
        min_x = min([pair[1][0],pair[0][0]])
        max_x = max([pair[1][0],pair[0][0]])
        min_y = min([pair[1][1],pair[0][1]])
        max_y = max([pair[1][1],pair[0][1]])
        
        if pair[0][0] < pair[1][0]:
            if pair[0][1] < pair[1][1]:
                y_coord = min_y
                count = 0
                for i in range(min_x, max_x+1):
                    grid[y_coord+count][i] += 1
                    count += 1
            elif pair[0][1] > pair[1][1]:
                y_coord = max_y
                count = 0
                for i in range(min_x, max_x+1):
                    grid[y_coord-count][i] += 1
                    count += 1
    
        elif pair[0][0] > pair[1][0]:
            if pair[0][1] < pair[1][1]:
                y_coord = max_y
                count = 0
                for i in range(min_x, max_x+1):
                    grid[y_coord-count][i] += 1
                    count += 1
            elif pair[0][1] > pair[1][1]:
                y_coord = min_y
                count = 0
                for i in range(min_x, max_x+1):
                    grid[y_coord+count][i] += 1
                    count += 1
    
    return grid

def calculate_overlapped(grid):

    flattened_grid = grid.flatten().tolist()

    count = 0
    for i in flattened_grid:
        if i >= 2:
            count += 1
            
    return count

data = load_file(5)
coordinate_pairs = parse_coordinate_pairs(data)
valid_hor_vert_pairs, valid_diag_pairs = find_valid_pairs(coordinate_pairs)

grid = np.zeros((999, 999))

grid_lines = mark_hor_vert_lines(grid, valid_hor_vert_pairs)
grid_lines = mark_diag_lines(grid, valid_diag_pairs)
overlap_count = calculate_overlapped(grid_lines)

print(overlap_count)

