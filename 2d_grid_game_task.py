import random as r

playerXY = [0,0]
foodXY = [3,3]


grid = [
    [".",".",".","."],
    [".",".",".","."],
    [".",".",".","."],
    [".",".",".","."]]

def DrawField():
  field = ""
  j = 0
  for col in grid:
    i = 0
    row = ""
    for tile in col:
      if j == playerXY[1] and i == playerXY[0]:
        tile = "P"
      if j == foodXY[1] and i == foodXY[0]:
        tile = "*"
      row = row + tile + " "
      i = i + 1
    field = field + row + "\n"
    j = j + 1
  print(field)

def PlayerMove():
  moveDir = input("Введите направление: ")
  if moveDir == "d":
    playerXY[0] = playerXY[0] + 1
  if moveDir == "a":
    playerXY[0] = playerXY[0] - 1
  if moveDir == "w":
    playerXY[1] = playerXY[1] - 1
  if moveDir == "s":
    playerXY[1] = playerXY[1] + 1
  global hunger
  hunger = hunger - 1


hunger = 8
while True:
  DrawField()
  PlayerMove()
  print("Голод:",hunger)
  if playerXY == foodXY:
    foodXY = [r.randint(0,3), r.randint(0,3)]
    hunger = 8
  if hunger == 0:
    break