import os
from Rooms import *

# Function to clear window and reset it
def reset_window():
    os.system('Clear')
    show_instructions()
    print()

# Define the get_new_state function
def get_new_state(direction_from_user, current_room):
    global player_inventory
    global rooms
    
    if direction_from_user in rooms[current_room]:
        new_room = rooms[current_room][direction_from_user]
        print("You moved to", new_room)

        # Check if the new room has an item
        if 'Item' in rooms[new_room]:
            item = rooms[new_room]['Item']
            print("You found an item:", item)

        return new_room
    else:
        reset_window()
        print("You can't go that way.")
        return current_room

# Function to display game instructions 
def show_instructions():
    instructions = ("The Lich King's Terror!\nCollect Six Items To Win The Game!\n__________________________________\n\nControls\nMovement: go North, go South, go East, go West\nGet Item Command: get [item name]\nCheck Status: status\n__________________________________")
    print(instructions)

# Move the show_status() function outside the main() function
def show_status(current_room, player_inventory):
    print("Current Room:", current_room)

    if 'Item' in rooms[current_room]:
        print("Item in Room:", rooms[current_room]['Item'])
    else:
        print("No item in this room.")

    print("\nInventory: ")
    for item in player_inventory:
        print(item)

    print("\nAvailable Directions:")
    available_directions = rooms[current_room].keys()
    available_directions = [direction for direction in available_directions if direction != 'Item']
    print(", ".join(available_directions))