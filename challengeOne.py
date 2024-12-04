# Challenge One : Historain Hysteria
# Part One

input_data = input("Data ~ \n")

l_list = []
r_list = []


for line in input_data.strip("\n"):
    left, right = line.split(maxsplit=1)
    l_list.append(left)
    r_list.append(right)

l_list.sort()
r_list.sort()

total_distance = sum(abs(left[i] - right[i]) for i in range(len(left))) 
print("Total Distance: ", total_distance)