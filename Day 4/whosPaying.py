import random
 
names = input("Give me everybody's names, seperated by a comma: ").split(", ")
who_pays = names[random.randint(0, len(names) - 1)]

print("{} is going to buy the meal today!".format(who_pays))