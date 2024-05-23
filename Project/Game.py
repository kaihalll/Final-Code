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
            if new_room == 'Greed': 
                if 'Key to Greed' not in player_inventory:
                    reset_window()
                    print("You need the Key to Greed to enter this room.")
                    continue
            if new_room == 'Dining Hall':
                if 'Key to Dining Hall' not in player_inventory:
                    reset_window()
                    print("You need the Key to Dining Hall to enter this room")
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
            
            # Room Descriptions
            if current_room == 'Dungeon':
                print("You are in a dimly lit, damp cell with iron bars and the faint sound of distant screams.")
            if current_room == 'Torture Hall':
                print("You are in a chamber filled with medieval torture devices, stained with blood, and echoing with the agonized cries of past victims.")
            if current_room == 'Limbo':
                print("You are in a misty, ethereal space suspended in time, where lost souls wander aimlessly without hope of salvation.")
            if current_room == 'Lust':
                print("You are in a decadent room adorned with velvet drapes and seductive paintings, exuding an intoxicating atmosphere of forbidden desires.")
            if current_room == 'Gluttony':
                print("You are in an overstuffed banquet hall overflowing with decaying food, where grotesque figures gorge themselves endlessly.")
            if current_room == 'Hidden Room':
                print("You are in a secret, well-concealed chamber accessible through a disguised entrance, containing ancient artifacts and forgotten secrets.")
            if current_room == 'Greed':
                print("You are in a vault glittering with gold, jewels, and treasures, guarded by traps and the lingering presence of materialism.")
            if current_room == 'Anger':
                print("You are in a fiery, chaotic arena with walls scorched by flames, resonating with the sounds of furious battles and enraged roars.")
            if current_room == 'Heresy':
                print("You are in a blasphemous sanctuary filled with profane symbols and dark rituals, challenging the very foundations of faith.")
            if current_room == 'Violence':
                print("You are in a brutal, blood-soaked battleground littered with weapons and the remains of countless brutal confrontations.")
            if current_room == 'Dining Hall':
                print("You are in a grand, yet eerie hall with long, empty tables set for a feast that never comes, haunted by the whispers of ghostly diners.")
            if current_room == 'Fraud':
                print("You are in a labyrinthine room of illusions and deceit, where nothing is as it seems and every step could lead to treachery.")
            if current_room == 'Treachery':
                print("You are in a cold, treacherous chamber where danger lingers in the air.")
            if current_room == 'Throne Room':
                print("You are in a majestic, yet ominous throne room with a dark, commanding seat of power.")
                 
        else:
            reset_window()
            print("You cannot go that way.")
    # Upgrades player's health in the Dungeon with collected souls
    elif command.lower() == 'upgrade health':
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
    elif command.lower() == 'upgrade power':
        reset_window()
        if current_room == 'Dungeon':
            if souls > 0:
                souls -= 1
                player_attack_power += 5
                print("Your attack power has increased by 5! Your current damage is", player_attack_power)
            else:
                print("You do not have any souls to upgrade.")
        else:
            print("You can only upgrade in the Dungeon.")
    # Displaying player status
    elif command.lower() == 'status':
        reset_window()
        display_status(current_room, player_health, player_max_health, heal_potions, player_inventory, souls, rooms, player_attack_power)
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