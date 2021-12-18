import numpy as np

def load_file(day):
    
    with open(f"day{str(day)}_input.txt", "r") as f:
        
        data = [i.strip("\n") for i in f.readlines()]
        return data
    
def calculate_gamma_epsilon(data):
    
    transposed = np.array([[char for char in row] for row in data]).T.tolist()
    
    gamma_digits = ""
    epsilon_digits = ""
    
    for i in range(len(transposed)):
        transposed_string = "".join(transposed[i])
        one_count = transposed_string.count("1")
        zero_count = transposed_string.count("0")

        if one_count > zero_count:
            gamma_digits += "1"
            epsilon_digits += "0"
        elif zero_count > one_count:
            gamma_digits += "0"
            epsilon_digits += "1"

    gamma_rate = int(gamma_digits, 2)
    epsilon_rate = int(epsilon_digits, 2)
    
    return gamma_rate, epsilon_rate

data = load_file(3)
gamma_rate, epsilon_rate = calculate_gamma_epsilon(data)
power_consumption = gamma_rate * epsilon_rate

print(power_consumption)