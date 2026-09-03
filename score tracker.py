score_board = {}
while True:
    input_name = input("enter the student name :")

    if input_name == "stop":
        break
    else:
        input_score = int(input("enter the student score :"))

    if input_name in score_board:
        score_board[input_name] += input_score
    else:
        score_board[input_name] = input_score
print(score_board)
