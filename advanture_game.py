import re
import json
# --------------- #
# Adventure Game  #
# --------------- #
def display_title():

    print( "=" * 50 )
    print( "WELCOME TO THE ADVENTURE GAME" ) 

    print( "=" * 50 )

    print( "Instructions:" ) 

    print( "- Enter your player's name (in letters)." )

    print( "- Make choices by typing the corresponding number." )
    
    print( "=" * 50 )



# Validate name with regex
def get_player_name():

    pattern=r"^[A-Za-z]{3,15}$"
    while True: 
        name=input( "Enter your player's name (letters only, between 3–15 chars): " )

        if re.match( pattern,name ):

            return name

        else: print( "Invalid name. Please use letters only." )


# First decision
def forest_path(decisions):

    print( "\nYou are standing in a forest full of monsters." ) 
    
    print( "1) Take the left road" )

    print( "2) Take the right road" )


    choice=input( "Choose 1 or 2: " )



    if choice=="1":

        decisions.append( "Left Road" )

        return "river"
        
    elif choice=="2":

        decisions.append( "Right Road" )

        return "cave"

    else:
        print( "Invalid pick. Try again." )

        return forest_path(decisions)


# Second decision
def final_decision(location, decisions):
    
    if location=="river":

        print( "\nYou reach a raging river." )

        print( "1) Try to swim across" )

        print( "2) Build a raft" )


        choice = input( "Choose 1 or 2: " )


        if choice=="1":
            decisions.append( "Swim Across" )
            return "lost"
        else:
            decisions.append( "Build Raft" )
            return "win"

    elif location=="cave":

        print( "\nYou find a mysterious cave." )

        print( "1) Enter the cave" )

        print( "2) Walk away" )


        choice = input( "Choose 1 or 2: " )


        if choice=="1":

            decisions.append( "Enter Cave" )

            return "win"

        else:
            decisions.append( "Walk Away" )

            return "lost"



# Save data to a JSON file
def save_game(data):

    with open("game_results.json" , "a") as file:
        json.dump(data, file)
        file.write("\n")



# Main 
def main():

    display_title()

    play_again = True

    while play_again:

        decisions = []

        outcomes = {
            "win": "You survived the adventure and was not devoured!",
            "lost": "You were lost the game and was devoured."
        }

        player_name=get_player_name()
        decisions.append(f"Codename: {player_name}")

        location=forest_path(decisions)
        result_key=final_decision(location, decisions)

        print("\n" + outcomes[result_key])

        # Save game data
        game_data={
            "player": player_name,
            "decisions": decisions,
            "outcome": outcomes[result_key]
        }

        save_game(game_data)

        replay=input("\nWould you like to play again? (y/n): ").lower() 

        if replay != "y":

            play_again = False

            print("Thanks for playing the adventure game!")



# Run the game
if __name__ == "__main__":
    main()