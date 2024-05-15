# To-Do list
# 1. Training room
# 2. Equipping different weapons from inventory
# 3. Printing out items in inventory and direction arrays instead of whole array
# 4. Creating enemies for each room (besides starting room)


import os

# Define room configurations
rooms = {
    'Dungeon': {'South': 'Torture Hall'},
    'Torture Hall': {'North': 'Dungeon', 'East': 'Dining Hall', 'South': 'Greed', 'West': 'Limbo'},
    'Limbo': {'North': 'Gluttony', 'East': 'Torture Hall', 'South': 'Lust', 'West': 'Exit'},
    'Lust': {'North': 'Limbo'},
    'Gluttony': {'South': 'Limbo', 'West': 'Hidden Room'}, #Chest piece is basically armor. Increases max health
    'Hidden Room': {'East': 'Gluttony'}, #upgrade item
    'Greed': {'North': 'Torture Hall', 'South': 'Anger'},
    'Anger': {'North': 'Greed', 'East': 'Violence', 'West': 'Heresy'},
    'Heresy': {'East': 'Anger'},
    'Violence': {'West': 'Anger'}, #The blade is a weapon. Though if we don't want to do weapons then we can just get rid of it
    'Dining Hall': {'North': 'Treachery', 'East': 'Throne Room', 'South': 'Fraud', 'East': 'Torture Hall'},
    'Fraud': {'North': 'Dining Hall'},
    'Treachery': {'South': 'Dining Hall'},
    'Throne Room': {'West': 'Dining Hall'},
    'Exit': {'South': 'Limbo'} #exit, end of the game
}

# Define enemy configurations (Giles, if you could do this it would be helpful)
# To do this all you have to do is write the name of each room at the start, then the name, health, atk power, and drop of the enemy.
# Use what is already there as a template if you need to. Delete this comment and the one above it once this is complete
enemies = {
    # Example
    # 'Research Room': [{'name': 'Skeleton Warrior', 'health': 50, 'attack_power': 10, 'drop': 'Bone Sword'}],
    
}

# Player attributes
player_health = 100
player_attack_power = 20
heal_potions = 3
player_inventory = []

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
- When you are in a combat encounter you can not leave the room.
- Defeat enemies by attacking them.
- To attack, type 'Attack'.
- Loot obtained from defeated enemies is added to your inventory.
- Type 'status' to see your current status.
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
    print("Player Health:", player_health)
    print("Health Potions:", heal_potions)
    print("Inventory:", player_inventory)
    print("Available Directions:", list(rooms[current_room].keys()))

# Function to display health bars
def display_health_bars(player_health, enemy_health):
    print("Player Health: [", "█" * (player_health // 5), "]")
    print("Enemy Health:  [", "█" * (enemy_health // 5), "]")

# Function to handle combat
def combat(enemy):
    global player_health
    global heal_potions
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
                player_inventory.append(enemy['drop'])
                print("You obtained", enemy['drop'], "and added it to your inventory.")
                input("\n\nPress Enter to continue")
                return
        elif command.lower() == 'heal':
            if heal_potions > 0:
                player_health = 100
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
    #Quit command
    elif command.lower() == 'quit':
        reset_window()
        print("Exiting game.")
        break
    #Error message
    else:
        reset_window()
        print("Invalid command. Please enter a valid direction, 'status', or 'quit' to exit.")