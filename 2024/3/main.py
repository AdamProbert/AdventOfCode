import re
import os
from pprint import pprint
dir_path = os.path.dirname(os.path.realpath(__file__))

# Advent of Code 2024 #3

PUZZLE_INPUT_PATH = dir_path + "/input.txt"
    
def parseInput():
    
    with open(PUZZLE_INPUT_PATH, "r") as f:
        puzzle_input = f.read()
        print("Puzzle input: ", puzzle_input)
        return puzzle_input
    

def extractMulCommands(puzzle_input):
    pattern = r"mul\(\d+,\d+\)"
    mul_commands = re.findall(pattern, puzzle_input)
    print("Mul commands", mul_commands)
    return mul_commands

def part_one():
    input = parseInput()
    mul_commands = extractMulCommands(input)
    answer = sum([int(command[4:command.index(",")]) * int(command[command.index(",")+1:-1]) for command in mul_commands])
    
    print("Answer: ", answer)
    print("Done")

def extract_dos_from_input(puzzle_input):
    splitdo = puzzle_input.split("do")
    all_dos = []
    for x in splitdo:
        if not x.startswith("n't()"):
            all_dos.append(x)

    return " ".join(all_dos)

def part_two():
    input = parseInput()
    the_dos = extract_dos_from_input(input)
    mul_commands = extractMulCommands(the_dos)
        
    answer = sum([int(command[4:command.index(",")]) * int(command[command.index(",")+1:-1]) for command in mul_commands])
    
    print("Answer: ", answer)
    print("Done")

def main():
    part_two()
    

if __name__ == "__main__":
    main()  