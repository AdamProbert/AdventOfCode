import re
import os
from pprint import pprint
dir_path = os.path.dirname(os.path.realpath(__file__))

# Advent of Code 2024 #4

PUZZLE_INPUT_PATH = dir_path + "/input.txt"
    
def parseInput():
    
    with open(PUZZLE_INPUT_PATH, "r") as f:
        # Extract input into matrix
        puzzle_input = [list(line.strip()) for line in f]
        return puzzle_input

# Generator returning the x, y coordinates of a letter in a matrix
def findLetter(matrix, letter):
    for x in range(len(matrix)):
        for y in range(len(matrix[x])):
            if matrix[x][y] == letter:
                yield x, y
            
def findNeighbourM(matrix, x, y):
    neighboursM = []
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue
            if x+i < 0 or y+j < 0:
                continue
            try:
                if matrix[x+i][y+j] == "M":
                    neighboursM.append((x+i,y+j))
            except IndexError:
                pass

    return neighboursM

def findSAM(matrix, x, y):
    try:
        diag1 = [matrix[x+i[0]][y+i[1]] for i in [(1,1), (-1, -1)]]
        diag2 = [matrix[x+i[0]][y+i[1]] for i in [(-1,1), (1, -1)]]
    except IndexError:
        return False
    
    print("Diag1", diag1)
    print("Diag2", diag2)

    if set(diag1) == set(["S", "M"]) and set(diag2) == set(["S", "M"]):
        return True
    
    return False

def getRemainingVectorPositions(x_x, x_y, m_x, m_y):
    # Calculate the direction vector
    direction_x = m_x - x_x
    direction_y = m_y - x_y
    
    # Calculate the third point
    third_x = m_x + direction_x
    third_y = m_y + direction_y
    
    # Calculate the fourth point
    fourth_x = third_x + direction_x
    fourth_y = third_y + direction_y
    
    if fourth_x < 0 or fourth_y < 0 or third_x < 0 or third_y < 0:
        return None, None
    
    return (third_x, third_y), (fourth_x, fourth_y)

def part_one():
    i = parseInput()

    outputgrid = [["." for x in range(len(i[0]))] for y in range(len(i))]

    xmas_count = 0
    
    for x, y in findLetter(i, "X"):
        print("X found at", x, y)
        neighboursM = findNeighbourM(i, x, y)
        print("Neighbours M", neighboursM)
        
        for neighbour in neighboursM:
            print("neighbourM", neighbour)
            third, fourth = getRemainingVectorPositions(x, y, neighbour[0], neighbour[1])
            if third is None or fourth is None:
                continue

            print("Third", third)
            print("Fourth", fourth)
            try:
                if i[third[0]][third[1]] == "A" and i[fourth[0]][fourth[1]] == "S":
                    print("Found XMAS!")
                    xmas_count += 1
                    outputgrid[x][y] = "X"
                    outputgrid[neighbour[0]][neighbour[1]] = "M"
                    outputgrid[third[0]][third[1]] = "A"
                    outputgrid[fourth[0]][fourth[1]] = "S"
            except IndexError:
                pass
    
    pprint(outputgrid) 
    print("Answer: ", xmas_count)
    print("Done")



def part_two():
    i = parseInput()
    
    outputgrid = [["." for x in range(len(i[0]))] for y in range(len(i))]
    xmas_count = 0

    for x, y in findLetter(i, "A"):
        print("A found at", x, y)
        sam = findSAM(i, x, y)
        if(sam):
            xmas_count += 1
            outputgrid[x][y] = "A"
            outputgrid[x+1][y+1] = i[x+1][y+1]
            outputgrid[x-1][y-1] = i[x-1][y-1]
            outputgrid[x+1][y-1] = i[x+1][y-1]
            outputgrid[x-1][y+1] = i[x-1][y+1]
    print("Answer: ", xmas_count)
    print("Done")    

def main():
    # part_one()
    part_two()
    

if __name__ == "__main__":
    main()
