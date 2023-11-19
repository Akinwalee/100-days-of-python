import random
rock = '''
       ,--.--._
------" _, \___)
        / _/____)
        \//(____)
------\     (__)
       `-----"
       '''
paper = '''
           ___..__
  __..--""" ._ __.'
              "-..__
            '"--..__";
 ___        '--...__"";
    `-..__ '"---..._;"
          """"----'      
          '''
scissors = '''  
    .-.  _
    | | / )
    | |/ /
   _|__ /_
  / __)-' )
  \  `(.-')
   > ._>-'
  / \/
'''
choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if choice == 0:
    print(rock)
elif choice == 1:
    print(paper)
else:
    print(scissors)

comp = random.randint(0, 2)
print("Computer chose: {}".format(comp))


if comp == 0:
    print(rock)
elif comp == 1:
    print(paper)
else:
    print(scissors)

if comp == choice:
    print("It's a draw")
else:
    print("You {}".format("lose" if (comp == 0 and choice == 2) or (comp == 1 and choice == 0) or (comp == 2 and choice == 1) else "win"))