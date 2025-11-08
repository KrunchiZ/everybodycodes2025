list = [5,3,7,8,9,10,4,5,7,8,8]
left = []
right = []
spine = []
spine.append(list[0])
s = 0
for i in range(1, len(list)):
    if ((len(left) < len(spine)) and (list[i] < spine[len(left)])):
        left.append(list[i])
    elif ((len(right) < len(spine)) and (list[i] > spine[len(right)])):
        right.append(list[i])
    else:
        if (list[i] > spine[len(left)]):
            left.append(0)
            right.append(0)
        spine.append(list[i])
        s += 1

print(spine)
print(left)
print(right)
