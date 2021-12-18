import numpy as np

def load_file(day):
    
    with open(f"day{str(day)}_input.txt", "r") as f:
        
        data = [i.strip("\n") for i in f.readlines()]
        return data
    
def calculate_oxygen_generator_rating(data):
    
    for i in range(len(data[0])):
        
        row_values = np.array([row[i] for row in data])

        zeros = np.where(row_values== "0")[0].tolist()
        ones = np.where(row_values=="1")[0].tolist()
        
        if len(zeros) > len(ones):
            data = [data[i] for i in range(len(data)) if i in zeros]
        elif len(zeros) < len(ones):
            data = [data[i] for i in range(len(data)) if i in ones]
        elif len(zeros) == len(ones):
            data = [data[i] for i in range(len(data)) if i in ones]
    
        if len(data) == 1:
            return int(data[0], 2)

def calculate_co2_rating(data):
    for i in range(len(data[0])):
        
        row_values = np.array([row[i] for row in data])

        zeros = np.where(row_values== "0")[0].tolist()
        ones = np.where(row_values=="1")[0].tolist()
        
        
        if len(zeros) < len(ones):
            data = [data[i] for i in range(len(data)) if i in zeros]
        elif len(zeros) > len(ones):
            data = [data[i] for i in range(len(data)) if i in ones]
        elif len(zeros) == len(ones):
            data = [data[i] for i in range(len(data)) if i in zeros]
    
        if len(data) == 1:
            return int(data[0], 2)
    
data = load_file(3)
oxygen_rating = calculate_oxygen_generator_rating(data)
co2_rating = calculate_co2_rating(data)
life_support_rating = oxygen_rating * co2_rating

print(life_support_rating)