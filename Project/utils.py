# utils.py

# Importing necessary modules
import os


# Function to reset the game window
def reset_window():
    os.system('clear')
    show_instructions()
    print()

# Function to display game instructions
def show_instructions():
    instructions = """
Instructions:
-------------
- Enter a direction (North, East, South, West) to move.
- You will encounter enemies in each room.
- Some rooms are locked and require keys which you will find in other rooms.
- When you are in a combat encounter you cannot leave the room.
- Defeat enemies by attacking them.
- To attack, type 'Attack'.
- Loot obtained from defeated enemies is added to your inventory.
- Type 'status' to see your current status.
- Type 'heal' to use a health potion if you have one.
- Type 'upgrade health' to exchange souls for increased health (only in Dungeon).
- Type 'upgrade power' to exchange souls for more damage (only in Dungeon).
- Type 'quit' to exit the game.
-------------
"""
    print(instructions)

# Function to display player's current status
def display_status(current_room, player_health, player_max_health, heal_potions, player_inventory, souls, rooms, player_attack_power):
    print("Current Room:", current_room)
    print("Player Health:", player_health, "/", player_max_health)
    print("Health Potions:", heal_potions)
    print("Inventory:", ', '.join(player_inventory) if player_inventory else 'None')
    print("Souls:", souls)
    print("Available Directions:", ', '.join(rooms[current_room].keys()))
    print("Player Atk Power:", player_attack_power)

# Function to display health bars for player and enemy
def display_health_bars(player_health, enemy_health):
    print("Player Health: [","\033[92m█" * (player_health // 5),"\033[0m]")
    print("Enemy Health:  [","\033[91m█" * (enemy_health // 5),"\033[0m]")

# Function to get enemies in a specified room
def get_enemies(room, enemies):
    if room in enemies:
        return enemies[room]
    else:
        return []