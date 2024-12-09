from pprint import pprint
import os
dir_path = os.path.dirname(os.path.realpath(__file__))

# Advent of Code 2024 #5

PUZZLE_INPUT_PATH = dir_path + "/smolinput.txt"

def parseInput():
    
    with open(PUZZLE_INPUT_PATH, "r") as f:
        puzzle_input = f.read().splitlines()
        input_break_index = puzzle_input.index("")
        rules = puzzle_input[:input_break_index]
        pages = puzzle_input[input_break_index+1:]
        for i in range(len(rules)):
            rules[i] = tuple([int(x) for x in rules[i].split("|")])

        for i in range(len(pages)):
            pages[i] =[int(y) for y in pages[i].split(",")]

    return pages, rules

def checkPageAgainstRule(page, rule):
    try:
        if page.index(rule[0]) < page.index(rule[1]):
            return True
    except ValueError:
        return True # Rule value not in page, so it is valid

    return False

def getMiddleIndexValue(page):
    return page[len(page) // 2]

def checkPageIsValid(page, rules):
    for rule in rules:
        if not checkPageAgainstRule(page, rule):
            return False

    return True

def getRulesMatchingNumber(number, rules):
    matching_rules = []
    for rule in rules:
        if number in rule:
            matching_rules.append(rule)

    return matching_rules

def getLessThanRules(rules, number):
    matching_rules = []
    for rule in rules:
        if number == rule[0]:
            matching_rules.append(rule)
    
    return matching_rules

def getGreaterThanRules(rules, number):
    matching_rules = []
    for rule in rules:
        if number == rule[1]:
            matching_rules.append(rule)
    
    return matching_rules

def sortPage(page, rules):
    


def part2(pages, rules):
    outputsum = 0
    invalid_pages = []
    for page in pages:
        if not checkPageIsValid(page, rules):
            invalid_pages.append(page)
    
    ordered_pages = []
    for page in invalid_pages:
        x = sortPage(page, rules)
        pprint(x)
        
        
    for page in ordered_pages:
        outputsum += getMiddleIndexValue(page)

    return outputsum


def part1(pages, rules):
    outputsum = 0

    for page in pages:
        broken_rule = False
        for rule in rules:
            if not checkPageAgainstRule(page, rule):
                broken_rule = True
                break
        
        if not broken_rule:
            outputsum += getMiddleIndexValue(page)

    return outputsum

def main():
    pages, rules = parseInput()
    print("Pages: ", pages)
    print("Rules: ", rules) 

    outputsum = part2(pages, rules)
    
        
    print("Done!")
    print("Output: ", outputsum)

if __name__ == "__main__":
    main()  