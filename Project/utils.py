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


# Function to display player's current status
def display_status(current_room, player_health, player_max_health, heal_potions, player_inventory, souls, rooms):
    print("Current Room:", current_room)
    print("Player Health:", player_health, "/", player_max_health)
    print("Health Potions:", heal_potions)
    print("Inventory:", ', '.join(player_inventory) if player_inventory else 'None')
    print("Souls:", souls)
    print("Available Directions:", ', '.join(rooms[current_room].keys()))

# Function to display health bars for player and enemy
def display_health_bars(player_health, enemy_health):
    print("Player Health: [", "█" * (player_health // 5), "]")
    print("Enemy Health:  [", "█" * (enemy_health // 5), "]")

# Function to get enemies in a specified room
def get_enemies(room, enemies):
    if room in enemies:
        return enemies[room]
    else:
        return []