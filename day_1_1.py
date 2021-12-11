input_list = open('day_1_input.txt').read().split()

#Test inputs
#test_input = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]

#function

sonar_sweeps = input_list

entries = len(sonar_sweeps)

print(len([sonar_sweeps[index]
    for index in range(0, entries)
    if index + 1 < entries
    and sonar_sweeps[index] < sonar_sweeps[index + 1]]))
