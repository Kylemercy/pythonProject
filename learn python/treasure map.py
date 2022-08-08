row1 = ["⬜️", "⬜️", "⬜️"]
row2 = ["⬜️", "⬜️", "⬜️"]
row3 = ["⬜️", "⬜️", "⬜️"]
treasure_map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
vertical = int(position[1])
horizontal = int(position[0])
selected_row = treasure_map[vertical - 1]
selected_row[horizontal - 1] = 'X'

print(f"{row1}\n{row2}\n{row3}")
