# game.py

# Importing necessary modules
from config import rooms, enemies
from player import player_health, player_max_health, player_attack_power, heal_potions, player_inventory, souls, current_room
from utils import reset_window, display_status, get_enemies
from combat import combat

# Resetting the game window
reset_window()

# Main game loop
while True:
    # Takes input command from the player
    command = input("\nCommand: ").capitalize()
    
    # Handles movement commands (North, East, South, West)
    if command in ['North', 'East', 'South', 'West']:
        if command in rooms[current_room]:
            new_room = rooms[current_room][command]
            
            # Checking special conditions for certain rooms
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
            
            # Handling combat encounters
            enemies_in_room = get_enemies(new_room, enemies)
            if enemies_in_room:
                player_health, player_max_health, heal_potions, player_inventory, souls = combat(enemies_in_room[0], player_health, player_max_health, player_attack_power, heal_potions, player_inventory, souls)
            
            # Updating the current room
            current_room = new_room
            reset_window()
            print(f"You have entered {current_room}")  # Print the room message
        else:
            reset_window()
            print("You cannot go that way.")
        # Upgrading player's health in the Dungeon with collected souls
    # Upgrades player's health in the Dungeon with collected souls
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
    # Displaying player status
    elif command.lower() == 'status':
        reset_window()
        display_status(current_room, player_health, player_max_health, heal_potions, player_inventory, souls, rooms)
    # Heals the player if they have healing potions
    elif command.lower() == 'heal':
        reset_window()
        if heal_potions > 0:
            player_health = player_max_health
            heal_potions -= 1
            print("Player healed back to full health!")
        else:
            print("You do not have any heal potions")
    # Exits the game
    elif command.lower() == 'quit':
        reset_window()
        print("Exiting game.")
        break
    # Handles invalid commands
    else:
        reset_window()
        print("Invalid command. Please enter a valid direction, 'status', 'heal', 'upgrade', or 'quit' to exit.")
    
    # Checks if player reached the Exit room to end the game
    if current_room == 'Exit':
        reset_window()
        print('You escaped hell. Congratulations!')
        break