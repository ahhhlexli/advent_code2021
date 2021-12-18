def load_file(day):

    with open(f"day{str(day)}_input.txt", "r") as f:
        
        data = [int(i) for i in f.readlines()]
        return data

def count_increases(data):
        
    increase_count = 0
    for i in range(1, len(data)):
        if data[i] > data[i-1]:
            increase_count += 1
        
    return increase_count

def calculate_sliding_window_sums(data):
    
    window_list = []
    for i in range(0, len(data)//3 * 3):
        window_list.append(sum([data[i], data[i+1], data[i+2]]))
    
    return window_list

data = load_file(1)
window_sums = calculate_sliding_window_sums(data)
increase_count = count_increases(window_sums)

print(increase_count)