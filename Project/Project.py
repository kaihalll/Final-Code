import os

# Define room configurations
rooms = {
    'Dungeon': {'South': 'Torture Hall'},
    'Torture Hall': {'North': 'Dungeon', 'East': 'Dining Hall', 'South': 'Greed', 'West': 'Limbo'},
    'Limbo': {'North': 'Gluttony', 'East': 'Torture Hall', 'South': 'Lust', 'West': 'Exit'},
    'Lust': {'North': 'Limbo'},
    'Gluttony': {'South': 'Limbo', 'West': 'Hidden Room'},
    'Hidden Room': {'East': 'Gluttony'},
    'Greed': {'North': 'Torture Hall', 'South': 'Anger'},
    'Anger': {'North': 'Greed', 'East': 'Violence', 'West': 'Heresy'},
    'Heresy': {'East': 'Anger'},
    'Violence': {'West': 'Anger'},
    'Dining Hall': {'North': 'Treachery', 'East': 'Throne Room', 'South': 'Fraud', 'West': 'Torture Hall'},
    'Fraud': {'North': 'Dining Hall'},
    'Treachery': {'South': 'Dining Hall'},
    'Throne Room': {'West': 'Dining Hall'},
    'Exit': {}
}

# Define enemy configurations
enemies = {
    'Torture Hall': [{'name': 'Torturer', 'health': 40, 'attack_power': 10, 'drop': 'soul'}],
    'Limbo': [{'name': 'Lost Soul', 'health': 30, 'attack_power': 8, 'drop': 'soul'}],
    'Lust': [{'name': 'Seducer', 'health': 35, 'attack_power': 12, 'drop': 'soul'}],
    'Gluttony': [{'name': 'Gluttonous Beast', 'health': 50, 'attack_power': 15, 'drop': 'soul'}],
    'Hidden Room': [{'name': 'Guardian', 'health': 60, 'attack_power': 18, 'drop': 'soul'}],
    'Greed': [{'name': 'Greedy Merchant', 'health': 45, 'attack_power': 14, 'drop': 'soul'}],
    'Anger': [{'name': 'Wrathful Warrior', 'health': 55, 'attack_power': 16, 'drop': 'soul'}],
    'Heresy': [{'name': 'Heretic Priest', 'health': 50, 'attack_power': 14, 'drop': 'soul'}],
    'Violence': [{'name': 'Violent Knight', 'health': 90, 'attack_power': 20, 'drop': 'Throne Room Key'}],
    'Dining Hall': [{'name': 'Vengeful Spirit', 'health': 40, 'attack_power': 12, 'drop': 'soul'}],
    'Fraud': [{'name': 'Deceiver', 'health': 45, 'attack_power': 14, 'drop': 'soul'}],
    'Treachery': [{'name': 'Backstabber', 'health': 50, 'attack_power': 16, 'drop': 'soul'}],
    'Throne Room': [{'name': 'Undead King', 'health': 200, 'attack_power': 45, 'drop': 'Key to Exit'}]
}

# Player attributes
player_health = 100
player_max_health = 100  # Added max health
player_attack_power = 20
heal_potions = 3
player_inventory = []
souls = 0  # Added souls count

# Starting room
current_room = 'Dungeon'

# Function to clear the screen and show instructions
def reset_window():
    os.system('clear')
    show_instructions()
    print()

# Function to show instructions
def show_instructions():
    instructions = """
Instructions:
-------------
- Enter a direction (North, East, South, West) to move.
- You will encounter enemies in each room.
- When you are in a combat encounter you cannot leave the room.
- Defeat enemies by attacking them.
- To attack, type 'Attack'.
- Loot obtained from defeated enemies is added to your inventory.
- Type 'status' to see your current status.
- Type 'heal' to use a health potion if you have one.
- Type 'upgrade' to exchange souls for increased health (only in Dungeon).
- Type 'quit' to exit the game.
-------------
"""
    print(instructions)

# Function to get enemies in a room
def get_enemies(room):
    if room in enemies:
        return enemies[room]
    else:
        return []

# Function to display player status
def display_status(current_room):
    print("Current Room:", current_room)
    print("Player Health:", player_health, "/", player_max_health)
    print("Health Potions:", heal_potions)
    print("Inventory:", ', '.join(player_inventory) if player_inventory else 'None')
    print("Souls:", souls)
    print("Available Directions:", ', '.join(rooms[current_room].keys()))

# Function to display health bars
def display_health_bars(player_health, enemy_health):
    print("Player Health: [", "█" * (player_health // 5), "]")
    print("Enemy Health:  [", "█" * (enemy_health // 5), "]")

# Function to handle combat
def combat(enemy):
    global player_health
    global heal_potions
    global souls
    enemy_health = enemy['health']
    
    reset_window()
    print(f"You encounter a {enemy['name']}!\n")
    print("Enemy Stats:")
    print("Name:", enemy['name'])
    print("Health:", enemy_health)
    
    # Combat loop
    while player_health > 0 and enemy_health > 0:
        print("\nPlayer's turn:")
        display_health_bars(player_health, enemy_health)
        command = input("Command: ")
        if command.lower() == 'attack':
            enemy_health -= player_attack_power
            print(f"You attack the enemy for {player_attack_power} damage!")
            if enemy_health <= 0:
                reset_window()
                print(f"You defeated the {enemy['name']}!")
                drop = enemy['drop']
                if drop == 'soul':
                    souls += 1
                    print("You obtained a soul and added it to your collection.")
                else:
                    player_inventory.append(drop)
                    print("You obtained", drop, "and added it to your inventory.")
                input("\n\nPress Enter to continue")
                return
        elif command.lower() == 'heal':
            if heal_potions > 0:
                player_health = player_max_health
                heal_potions -= 1
                print("Player healed back to full health!")
            else:
                print("You do not have any heal potions")
            
        print("\nEnemy's turn:")
        print(f"The {enemy['name']} attacks you!")
        player_health -= enemy['attack_power']
        print(f"You took {enemy['attack_power']} damage!")
        
        if player_health <= 0:
            reset_window()
            print(f"You have been defeated by the {enemy['name']}!")
            print("Game over.")
            exit()
        
        input("\n\nPress Enter to continue")
        reset_window()

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