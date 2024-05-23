import os
from Data import *

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