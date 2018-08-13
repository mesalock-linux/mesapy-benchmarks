BOARD_SIZE = 28

def under_attack(col, queens):
    return col in queens or \
           any(abs(col - x) == len(queens)-i for i,x in enumerate(queens))

def solve(n):
    solutions = [[]]
    for row in range(n):
        solutions = (solution+[i+1]
                       for solution in solutions # first for clause is evaluated immediately,
                                                 # so "solutions" is correctly captured
                       for i in range(BOARD_SIZE)
                       if not under_attack(i+1, solution))
    return solutions

if __name__ == '__main__':
    answers = solve(BOARD_SIZE)
    first_answer = next(answers)
