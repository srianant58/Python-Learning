name  = input("Hey type your name: ")
print(f"Hello {name}, welcome to my game!")

should_we_play = input("Do you want to play the game? ").lower()

if should_we_play == "yes" or should_we_play == "y":
    print("We are going to start playing")

    direction = input("Do you want to go left or right? (left/right)").lower()
    if direction == "left":
        print("Okay you went left and fell off a cliff, you die !!!")
    elif direction == "right":
        choice = input("You now see a bridge, do you want to swim under it or cross over it? (Swim/cross) ").lower()

        if choice == "swim":
            print("You get eaten by a crocodile, you die !!!")
        elif choice == "cross":
            print("You find the Gold and Won !!!")
        else:
            print("Sorry not a valid input, you die !!!")
    else:
        print("Sorry not a valid input, you die !!!")
else:
    print("We are NOT playing, sad :( !!!")    