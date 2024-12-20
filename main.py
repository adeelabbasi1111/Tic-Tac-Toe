import random

print("\n\t\t\t\tWelcome to Tic Tac Toe!")

#============= Taking players name and deciding Who will play

p1 = input("Player 1: ")
p2 = input("Player 2: ")
toss = random.random()
if toss > 0.5:
    turn = True
    print(f"{p1} ki bari ha !")
else:
    print(f"{p2}")
    turn = False

# Making a list to store decisions

ls = ["___" for i in range(1, 10)]
avalaible_boxes = [i for i in range(9)]

game_not_over = True
counter = 0

wins = [ [" X " for i in range(3)] , [" O " for i in range(3)] ]

# ================ Game loop

while game_not_over:

#================ Making the box

    for i in range(1,10):
            if i == 1:
                print("\t\t\t",end="")
            if i%3 == 0:
                print(f"{ls[i-1]}", end="")
                print("\n",end="")
                print("\t\t\t",end="")
                continue
            print(f"{ls[i-1]}|",end="")
    print("\n")

# ============ Taking input from the players
    if turn:
        inp = int(input(f"{p1} konsa box par circle lagana ha ? :"))
        if inp-1 in avalaible_boxes:
            ls[inp-1] = " O "
            avalaible_boxes.remove(inp-1)
        else:
            inp = int(input(f"Ispar laga hua ha doosra choose karo:"))
            ls[inp-1] = " O "
    else:
        inp = int(input(f"{p2} konsa box par cross lagana ha ? : "))
        if inp-1 in avalaible_boxes:
            ls[inp-1] = " X "
            avalaible_boxes.remove(inp-1)
        else:
            inp = int(input(f"Ispar laga hua ha doosra choose karo:"))
            ls[inp-1] = " X "


# ===================== Calculating if someone got a row

    for win in wins:
        if ls[:3] == win or ls[3:6] == win or ls[:6:9] == win or ls[:9:3] == win or ls[1:9:3] == win or ls[2:9:3] == win or ls[:9:4] == win or ls[2::2][:-1] == win:
            if win[1] == " O ":
                print(f"{p1} is the winner !!!")

            else:
                print(f"\n {p2} is the winner !!! \n")

            game_not_over = False

            for i in range(1, 10):
                if i == 1:
                    print("\t\t\t", end="")
                if i % 3 == 0:
                    print(f"{ls[i - 1]}", end="")
                    print("\n", end="")
                    print("\t\t\t", end="")
                    continue
                print(f"{ls[i - 1]}|", end="")
            print("\n")


# ============== Switching turn and ending game

    turn = not turn
    counter += 1
    if counter == 9:
        game_not_over = False


