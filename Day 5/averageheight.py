heights = input("Input a list of heights seperated by comma: ").split(", ")
sum = 0
for height in heights:
    sum += float(height)

average = round(sum / len(heights))

print("The average student height is {}".format(average))
