print(r"""\         ____...------------...____
               _.-"` /o/__ ____ __ __  __ \o\_`"-._
             .'     / /                    \ \     '.
             |=====/o/======================\o\=====|
             |____/_/________..____..________\_\____|
             /   _/ \_     <_o#\__/#o_>     _/ \_   \
             \_________\####/_________/
              |===\!/========================\!/===|
              |   |=|          .---.         |=|   |
              |===|o|=========/     \========|o|===|
              |   | |         \() ()/        | |   |
              |===|o|======{'-.) A (.-'}=====|o|===|
              | __/ \__     '-.\uuu/.-'    __/ \__ |
              |==== .'.'^'.'.====|
              |  _\o/   __  {.' __  '.} _   _\o/  _|
            `""""-""""""""""""""""""""""""""-""""`""")
print("Welcome to Treasure Island!\n Your mission is to find the treasure")
chose = input("You need to choose left or right")
if chose == "right":
    print("You fell into a hole. Game Over!")
elif chose == "left":
    chose = input("Do you want to swim or wait till ship arrive")
    if chose == "swim":
        print("Attacked by a trout. Game Over!")
    elif chose == "wait":
        chose = input("Which Door do you want keep going red? blue? or yellow?")
        if chose == "red":
            print("Burned by fire. Game Over!")
        elif chose == "yellow":
            print("You WIN!")
        elif chose == "blue":
            print("Eaten by beasts. Game Over!")
        else:
            print("You LOSE!")
    else:
        print("Game Over!")
else:
    print("Game Over!")
