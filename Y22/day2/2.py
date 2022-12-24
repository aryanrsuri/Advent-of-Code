

'''

A ... Rock
B ... Paper
C ... Scissors

X ... Rock
Y ... Paper
Z ... Scissors

R 1
P 2
S 3

'''
def part_one():
    values =  {"A": 1, "B": 2, "C": 3,"X": 1, "Y": 2, "Z": 3}
    def readfile(fp: str) -> list:
        with open(fp) as FILE:
            lines = FILE.readlines()
            lines = [x.strip() for x in lines]
        return lines
    lines = readfile("./Y22/day2/2.input.txt")
    for line in lines:
        for char in line:
            print(char)
            

print(part_one())
    