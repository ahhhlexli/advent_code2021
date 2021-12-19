import numpy as np

def load_file(day):
    
    with open(f"day{str(day)}_input.txt", "r") as f:
        
        data = [i.strip("\n") for i in f.readlines()]
        return data
    
def get_bingo_boards(data):

    bingo_boards = []

    for i in range(1,len(data), 6):
        if data[i] == "":
            single_board = []
            for j in range(1,6):
                row = data[i+j]
                row = row.split(" ")
                row = [int(num) for num in row if num != ""]
                single_board.append(row)
            bingo_boards.append(single_board)
    
    return bingo_boards

def check_if_winner(board):
    
    transposed_board = np.array(board).T.tolist()
    
    for row in board:
        if set(row) == {"X"}:
            return True
    for row in transposed_board:
        if set (row) == {"X"}:
            return True
    return False

def find_winning_board(bingo_numbers, bingo_boards):
    for number in bingo_numbers:
        
        for board in bingo_boards:
            # check if winner:
            status = check_if_winner(board)
            
            if status == True:
                return board, winning_number
            for row in board:
                for i in range(len(row)):
                    if row[i] == number:
                        row[i] = "X"
        winning_number = number
                    
def calculate_final_score(board, winning_number):
    
    unmarked_numbers = []
    
    for row in board:
        for number in row:
            if number != "X":
                unmarked_numbers.append(number)
                
    unmarked_sum = sum(unmarked_numbers)
    final_score = unmarked_sum * winning_number
    
    return final_score
                        
data = load_file(4)

bingo_numbers = [int(i) for i in data[0].split(",")]
bingo_boards = get_bingo_boards(data)

winning_board, winning_number = find_winning_board(bingo_numbers, bingo_boards)
final_score = calculate_final_score(winning_board, winning_number)
print(final_score)