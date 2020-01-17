import math
import random
from random import choice


class Board:

    num_seq = [i for i in range(9)]


    def __init__(self, difficulty):

        self.board = [[0 for i in range(9)] for j in range(9)]
        self.generate_board(difficulty)
        self.display()



    def generate_board(self, difficulty):

        self.solve()

        i = 0

        while i < difficulty:
            curr_row = choice(Board.num_seq)
            curr_col = choice(Board.num_seq)

            if self.board[curr_row][curr_col] != 0:
                self.board[curr_row][curr_col] = 0
                i = i + 1




    def display(self):

        for i in range(9):
            if i % 3 == 0 and i != 0:
                print("- - - - - - - - - - - -")

            for j in range(9):
                if j % 3 == 0 and j != 0:
                    print(" | ", end="")

                if j == 8:
                    print(self.board[i][j])

                else:
                    print(str(self.board[i][j]) + " ", end="")
        print("")


    #checks if board is valid
    def valid(self, num, row, col):

        for i in range(9):

            #check row (y)
            if self.board[row][i] == num and i != col:
                return False

            #check column (x)
            if self.board[i][col] == num and i != row:
                return False


        box_row = row // 3
        box_col = col // 3

        #check box
        for i in range(box_row*3, box_row*3 + 3):
            for j in range(box_col*3, box_col*3 + 3):
                if self.board[i][j] == num and (i != row and j != col):
                    return False

        return True



    #finds empty slot
    def find_empty(self):
        for i in range(9):
            for j in range(9):
                if self.board[i][j] == 0:
                    return (i, j)  #i is y(row) and j is x(col)

        return None



    #solves the puzzle
    def solve(self):

        find = self.find_empty()

        if not find:
            return True
        else:
            row, col = find

        visited = []
        while len(visited) < 9:

            curr_num = choice(Board.num_seq) + 1
            if curr_num in visited:
                continue
            else:
                visited.append(curr_num)

            if self.valid(curr_num, row, col):
                self.board[row][col] = curr_num

                if self.solve():
                    return True

                self.board[row][col] = 0

        return False





my_board = Board(60)

my_board.solve()

my_board.display()
