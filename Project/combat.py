# Importing necessary functions
from utils import reset_window, display_health_bars

# Function to handle combat encounters
def combat(enemy, player_health, player_max_health, player_attack_power, heal_potions, player_inventory, souls):
    # Initializing enemy health
    enemy_health = enemy['health']
    
    # Displaying encounter message and enemy stats
    reset_window()
    print(f"You encounter a {enemy['name']}!\n")
    print("Enemy Stats:")
    print("Name:", enemy['name'])
    print("Health:", enemy_health)
    
    # Main combat loop
    while player_health > 0 and enemy_health > 0:
        # Player's turn
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
                return player_health, player_max_health, heal_potions, player_inventory, souls
        elif command.lower() == 'heal':
            if heal_potions > 0:
                player_health = player_max_health
                heal_potions -= 1
                print("Player healed back to full health!")
            else:
                print("You do not have any heal potions")
            
        # Enemy's turn
        print("\nEnemy's turn:")
        print(f"The {enemy['name']} attacks you!")
        player_health -= enemy['attack_power']
        print(f"You took {enemy['attack_power']} damage!")
        
        # Checking player's health
        if player_health <= 0:
            reset_window()
            print(f"You have been defeated by the {enemy['name']}!")
            print("Game over.")
            exit()
        
        input("\n\nPress Enter to continue")
        reset_window()

    return player_health, player_max_health, heal_potions, player_inventory, souls