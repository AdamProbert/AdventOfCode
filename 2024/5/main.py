import os
dir_path = os.path.dirname(os.path.realpath(__file__))

# Advent of Code 2024 #5

PUZZLE_INPUT_PATH = dir_path + "/input.txt"
    
def parseInput():
    
    with open(PUZZLE_INPUT_PATH, "r") as f:
        puzzle_input = f.readlines()
        for i in puzzle_input:
            pass # do thing

    return 
    

def main():
    input = parseInput()
    
    print("Done!")
    print("Output: ", output)

if __name__ == "__main__":
    main()  