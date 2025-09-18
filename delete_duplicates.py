numbers = [5,2,3,6,2,7,9,3,2,3,9,1,2,2,2]
new = []
for item in numbers:
    if item not in new:
        new.append(item)
print(new)

