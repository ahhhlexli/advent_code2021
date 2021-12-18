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
        
data = load_file(1)
count = count_increases(data)
print(count)
