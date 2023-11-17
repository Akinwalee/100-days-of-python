print("Welcome to the Love Calculator")
name1 = input("What is your name? \n").lower()
name2 = input("What is their name? \n").lower()

names = name1 + name2

true = 0
love = 0

true += names.count("t")
true += names.count("r")
true += names.count("u")
true += names.count("e")

love += names.count("l")
love += names.count("o")
love += names.count("v")
love += names.count("e")

score = int(str(true) + str(love))

if 10 > score > 90:
    print("Your score is {}, you go together like coke and mentos.".format(score))
elif 40 < score < 50:
    print("Your score is {}, you are alright together.".format(score))
else:
    print("Your score is {}.".format(score))

