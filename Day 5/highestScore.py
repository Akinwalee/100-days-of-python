scores = input("Enter a list of scores seperated by commas: ").split(",")
# highest = int(scores[0])
# for score in scores:
#     if int(score) > highest:
#         highest = int(score)

for score in scores:
    score = int(score)

print("The highest score is: {}".format(scores))