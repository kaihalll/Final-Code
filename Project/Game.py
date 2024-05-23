from Data import *
from Functions import *

# Resets screen
reset_window()

# Main game loop
while True:
    command = input("\nCommand: ").capitalize()
    # Movement commands
    if command in ['North', 'East', 'South', 'West']:
        if command in rooms[current_room]:
            new_room = rooms[current_room][command]
            
            # Check for keys before entering the Throne Room or Exit
            if new_room == 'Throne Room':
                required_keys = ['Throne Room Key']
                if not all(key in player_inventory for key in required_keys):
                    reset_window()
                    print("You need the Throne Room Key to enter the Throne Room.")
                    continue
            elif new_room == 'Exit':
                if 'Key to Exit' not in player_inventory:
                    reset_window()
                    print("You need the Key to Exit to enter this room.")
                    continue
            
            enemies_in_room = get_enemies(new_room)
            if enemies_in_room:
                combat(enemies_in_room[0])
            current_room = new_room  # Update current_room here
            reset_window()  # Clear the screen
            print(f"You have entered {current_room}")  # Print the room message
        else:
            reset_window()
            print("You cannot go that way.")
    # Status command
    elif command.lower() == 'status':
        reset_window()
        display_status(current_room)
    # Heal command
    elif command.lower() == 'heal':
        reset_window()
        if heal_potions > 0:
            player_health = player_max_health
            heal_potions -= 1
            print("Player healed back to full health!")
        else:
            print("You do not have any heal potions")
    # Upgrade command
    elif command.lower() == 'upgrade':
        reset_window()
        if current_room == 'Dungeon':
            if souls > 0:
                souls -= 1
                player_max_health += 5
                player_health = player_max_health
                print("Your maximum health has increased by 5! Your new maximum health is", player_max_health)
            else:
                print("You do not have any souls to upgrade.")
        else:
            print("You can only upgrade in the Dungeon.")
    # Quit command
    elif command.lower() == 'quit':
        reset_window()
        print("Exiting game.")
        break
    # Error message
    else:
        reset_window()
        print("Invalid command. Please enter a valid direction, 'status', 'heal', 'upgrade', or 'quit' to exit.")
    #Check if player wins game
    if current_room == 'Exit':
        reset_window()
        print('You escaped hell. Congratulations!')
        exit()