#Read the txt file for the input
with open('Challenge-01/input.txt') as file:
    data = [i for i in file.read().strip().split("\n")]


# traverse the data 
max = 0
count = 0
for item in data:
    if item == '':
        count = 0
    else:
        num = int(item)
        count += num
    if count > max:
        max = count

print("Answer to part 1: ", max)


#Part 2 
top1 = 0
top2 = 0
top3 = 0
count = 0
for item in data:
    if item == '':
        count = 0
    else:
        num = int(item)
        count += num
    if count > top1:
        #we need to shift the 3 position of the top1 to top2 and to top3 so that the newest highest number could take place first
        top3 = top2
        top2 = top1
        top1 = count
    elif count > top2:
        top3 = top2
        top2 = count
    elif count > top3:
        top3 = count

print("Answer to part 2: ", top1 + top2 + top3)