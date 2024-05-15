import os

# Define room configurations
rooms = {
    'Dungeon': {'South': 'Torture Hall'},
    'Torture Hall': {'North': 'Dungeon', 'East': 'Dining Hall', 'South': 'Greed', 'West': 'Limbo', 'Item': 'Keys to Limbo'},
    'Limbo': {'North': 'Gluttony', 'East': 'Torture Hall', 'South': 'Lust', 'West': 'Exit', 'Item': ''},
    'Lust': {'North': 'Limbo', 'Item': 'Whip of Pain', 'Key Item': 'Key to Gluttony'},
    'Gluttony': {'South': 'Limbo', 'West': 'Hidden Room', 'Item': "Glutton's Chest Piece"}, #Chest piece is basically armor. Increases max health
    'Hidden Room': {'East': 'Gluttony', 'Item': 'Blood Gem'}, #upgrade item
    'Greed': {'North': 'Torture', 'South': 'Anger', 'Item': 'Cursed Coin', 'Key Item': 'Key to Anger'},
    'Anger': {'North': 'Greed', 'East': 'Violence', 'West': 'Heresy', 'Item': 'Key to Heresy and Violence'},
    'Heresy': {'East': 'Anger'},
    'Violence': {'West': 'Anger', 'Item': "Murderer's Bloody Blade", 'Key Item': 'Key to Dining Hall'}, #The blade is a weapon. Though if we don't want to do weapons then we can just get rid of it
    'Dining Hall': {'North': 'Treachery', 'East': 'Throne Room', 'South': 'Fraud', 'East': 'Torture Hall', 'Item': 'Key to Fraud'},
    'Fraud': {'North': 'Dining Hall'},
    'Treachery': {'South': 'Dining Hall', 'Key Item': "Backstabber's Knife"},
    'Throne Room': {'West': 'Dining Hall'},
    'Exit': {'South': 'Limbo'} #exit, end of the game
}

# Define enemy configurations
enemies = {
    'Research Room': [{'name': 'Skeleton Warrior', 'health': 50, 'attack_power': 10, 'drop': 'Bone Sword'}],
    'Treasury': [{'name': 'Giant Spider', 'health': 60, 'attack_power': 12, 'drop': 'Spider Venom'}],
    'Bed Chambers': [{'name': 'Wraith', 'health': 80, 'attack_power': 18, 'drop': 'Ectoplasmic Essence'}],
    'Chamber of Shadows': [{'name': 'Shadow Assassin', 'health': 60, 'attack_power': 20, 'drop': 'Shadow Cloak'}],
    'Armory': [{'name': 'Soul Reaper', 'health': 100, 'attack_power': 25, 'drop': 'Reaper Scythe'}],
    'Throne Room': [{'name': 'Undead King', 'health': 120, 'attack_power': 30, 'drop': 'Cursed Crown'}]
}

# Player attributes
player_health = 100
player_attack_power = 20
heal_potions = 3
player_inventory = []

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
                break
        if command.lower() == 'heal':
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
        
        input("\n\nPress Enter to continue")
        reset_window()
        
    if player_health <= 0:
        reset_window()
        print(f"You have been defeated by the {enemy['name']}!")
        print("Game over.")
        exit()

# Control loop
current_room = 'Entrance to the Crypt'

reset_window()

while True:
    command = input("\nCommand: ").capitalize()
    if command in ['North', 'East', 'South', 'West']:
        if command in rooms[current_room]:
            current_room = rooms[current_room][command]
            enemies_in_room = get_enemies(current_room)
            if enemies_in_room:
                combat(enemies_in_room[0])
        else:
            reset_window()
            print("You cannot go that way.")
    elif command.lower() == 'status':
        reset_window()
        display_status(current_room)
    elif command.lower() == 'quit':
        reset_window()
        print("Exiting game.")
        break
    else:
        reset_window()
        print("Invalid command. Please enter a valid direction, 'status', or 'quit' to exit.")
