print("Welcome to first game!")

name = input("What is your name? ")
age = int(input("How old are you? "))


health = 10


if age >= 18:
    print("You are old enough to play this game")

    play_game = input("Do you want to play? ").lower()
    if play_game == "yes":
        print("You are starting with", health, "health")

        print("Let's play!")

        direction = input("First choice... Left or Right (left/right)? ")
        
        if direction == "left":
            answer = input("Great, you follow the path and reach a lake... Do you swim across or go around (across/around)? ")
           
            if answer == "around":
                print("You went around and reached the other side of the lake")
            elif  answer == "across":
                print("You manged to get across, but you got biten by a fish and lost 5 health.")
                health -= 5


            answer = input("You notice a house and a river. Which one do you go to (river/house)? ")
            if answer == "house":
                print("You go to the house and are greated by the owner... He doesn't like you and you lose 5 health")
                health -= 5
                if health <= 0:
                    print("You now have 0 health and you lose the game")
                else:
                    print("You have survived... You win!!!")
            else:
                print("You fell into the river and lost...")
                
                
        else:
            print("You fell down and lost...")
    else:
        print("Come back soon...")

else:
    print("You are not old enough to play....")
