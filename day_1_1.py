#data = open("...\day_1_input.txt")
input = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]

def count_increased(input):
    count, compare = 0, int(input[0])
    for num in input[1:]:
        if int(num) > compare:
            count += 1
        compare = int(num)
    return count
