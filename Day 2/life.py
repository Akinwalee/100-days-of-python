age = int(input("What is your current age? "))

years = 90 - age
months = years * 12
weeks = years * 52
days = years * 365

print("You have {} days, {} weeks, and {} moths left.".format(days, weeks, months))