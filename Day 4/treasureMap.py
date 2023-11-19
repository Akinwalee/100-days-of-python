row1 = ["⬜", "⬜", "⬜"]
row2 = ["⬜", "⬜", "⬜"]
row3 = ["⬜", "⬜", "⬜"]
map = [row1, row2, row3]
print("{}\n{}\n{}".format(row1, row2, row3))
position = input("Where do you want to put the treasure? ")

row = int(position[1]) - 1
col = int(position[0])

map[row][col] = "X"

print("{}\n{}\n{}".format(row1, row2, row3))

