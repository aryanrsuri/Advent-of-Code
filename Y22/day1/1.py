def part_one():
    def readfile(fp: str) -> list:
        with open(fp) as FILE:
            lines = FILE.readlines()
            lines = [x.strip('\n') for x in lines]
        return lines
    lines = readfile('../1.input.txt')
    sums = []
    sum = 0 
    for line in lines:
        if line != '':
            sum += int(line)
        else: 
            sums.append(sum)
            sum = 0
    return max(sums)

def part_two():
    def readfile(fp: str) -> list:
        with open(fp) as FILE:
            lines = FILE.readlines()
            lines = [x.strip('\n') for x in lines]
        return lines
    lines = readfile("./Y22/day1/1.input.txt")
    sums = []
    val = 0 
    for line in lines:
        if line != '':
            val += int(line)
        else: 
            sums.append(val)
            val = 0
    sums.sort(reverse=True)
    return sum(sums[0:3])

print(part_two())