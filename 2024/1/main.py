import os
dir_path = os.path.dirname(os.path.realpath(__file__))

# Advent of Code 2024 #1

PUZZLE_INPUT_PATH = dir_path + "/input.txt"
    
def parseInput():
    puzzle_input_l = []
    puzzle_input_r = []
    with open(PUZZLE_INPUT_PATH, "r") as f:
        puzzle_input = f.readlines()
        for i in puzzle_input:
            l, r = i.split()
            puzzle_input_l.append(int(l))
            puzzle_input_r.append(int(r))
    
    return puzzle_input_l, puzzle_input_r

def calculateTotalDistance(puzzle_input_l, puzzle_input_r):
    puzzle_input_l.sort()
    puzzle_input_r.sort()

    total_distance = 0
    for i in range(len(puzzle_input_l)):
        total_distance += abs(puzzle_input_l[i] - puzzle_input_r[i])
    
    return total_distance

def calculateSimilarityScore(puzzle_input_l, puzzle_input_r):
    simularity_score = 0

    # Prepare score frequency dictionary for right list
    puzzle_input_r_frequency = {}
    for i in puzzle_input_r:
        if i in puzzle_input_r_frequency:
            puzzle_input_r_frequency[i] += 1
        else:
            puzzle_input_r_frequency[i] = 1

    for i in puzzle_input_l:
        try:
            simularity_score += i * puzzle_input_r_frequency[i]
        except KeyError: # Score not found, simularity_score does not increase
            pass

    return simularity_score

def main():
    puzzle_input_l, puzzle_input_r = parseInput()
    total_distance = calculateTotalDistance(puzzle_input_l, puzzle_input_r)        
    simularity_score = calculateSimilarityScore(puzzle_input_l, puzzle_input_r)

    print("Done!")
    print("Total distance: ", total_distance)
    print("Simularirty score: ", simularity_score)


if __name__ == "__main__":
    main()  