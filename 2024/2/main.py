from pprint import pprint
import os
dir_path = os.path.dirname(os.path.realpath(__file__))

# Advent of Code 2024 #2

PUZZLE_INPUT_PATH = dir_path + "/input.txt"
    
def bruteForceReportIsSafe(report):
    safe = isReportSafe(report)
    if safe:
        return True
    else:
        for i in range(0, len(report)):
            reportCopy = report.copy()
            reportCopy.pop(i)
            safe = isReportSafe(reportCopy)
            if safe:
                return True
    return False

def isReportSafe(report):
    increasing = True if report[-1] > report[0] else False
    for i in range(1, len(report)):
        if increasing:
            if report[i] < report[i-1]:
                return False
        else:
            if report[i] > report[i-1]:
                return False
        
        diff = abs(report[i] - report[i-1])
        if diff > 3 or diff < 1:
            return False
        
    return True


# Keep track of the problem reports and retry removing one by one
def checkReportIsSafe(report, retry=False):
    increasing = True if report[-1] > report[0] else False
    problemReports = []
    for i in range(1, len(report)):
        if increasing:
            if report[i] < report[i-1]:
                problemReports.append(i-1)
        else:
            if report[i] > report[i-1]:
                problemReports.append(i)
            
        diff = abs(report[i] - report[i-1])
        if diff > 3 or diff < 1:
           problemReports.append(i)
           problemReports.append(i-1)
    
    if len(problemReports) == 0:
        return True
    elif len(problemReports) >= 1 and not retry:
        for problem in problemReports:
            reportCopy = report.copy()
            reportCopy.pop(problem)
            return checkReportIsSafe(reportCopy, True)        
    return False


def recurceReportIsSafe(report, removals=0):
    if removals > 1:
        return False
    
    increasing = True if report[-1] > report[0] else False
    for i in range(1, len(report)):
        if increasing:
            if report[i] < report[i-1]:
                return recurceReportIsSafe(report[:i-1] + report[i:], removals+1)
        else:
            if report[i] > report[i-1]:
                return recurceReportIsSafe(report[:i-1] + report[i:], removals+1)
            
        diff = abs(report[i] - report[i-1])
        if diff > 3 or diff < 1:
            return recurceReportIsSafe(report[:i-1] + report[i:], removals+1)
    
    return True
    
def parseInput():
    
    levels = []
    with open(PUZZLE_INPUT_PATH, "r") as f:
        puzzle_input = f.readlines()
        for i in puzzle_input:
            levels.append([int(e) for e in i.strip().split()])
    
    return levels
    

def main():
    levels = parseInput()
    safe_levels = 0

    for level in levels:
        safe_levels += 1 if bruteForceReportIsSafe(level) else 0

    print("Done!")
    print("Safe levels: ", safe_levels)

if __name__ == "__main__":
    main()  