import os
from Commands import reset_window, get_new_state, show_status, show_instructions
from Rooms import Lich_King_room, rooms
from Endings import goodEnding, badEnding

os.system('Clear')

def main():
    show_instructions()
    current_room = 'Entrance to the Crypt'  # Initialize current room here
    player_inventory = []

    while True:
        while True:
            command = input('\n\nEnter a command: ').lower()
            reset_window()
            if command == '':
                continue
            else:
                break
        
        action, * params = command.split()

        if action == 'go':
            direction = params[0].capitalize()
            if direction in rooms[current_room]:
                current_room = get_new_state(direction, current_room)
            else:
                reset_window()
                print('Invalid direction!')
        elif action == 'get':
            if len(params) == 0:
                reset_window()
                print('Please specify the item name.')
            else:
                item_name = ' '.join(params).lower()
                if 'Item' in rooms[current_room]:
                    room_item = rooms[current_room]['Item']
                    if item_name.lower() == room_item.lower():
                        player_inventory.append(room_item)
                        del rooms[current_room]['Item']
                        reset_window()
                        print(f'You obtained the {room_item} from this room.')
                    else:
                        reset_window()
                        print('Item not found in this room.')
                else:
                    reset_window()
                    print('No item in this room.')
        elif action == 'status':
            show_status(current_room, player_inventory)  # Pass current_room and player_inventory
        elif action == 'quit':
            break
        else:
            reset_window()
            print('Command does not exist')

        if len(player_inventory) == 6 and current_room == Lich_King_room:
            
            Answer = input('\nWould You Like To Fight The Lich King? (y/n)')
            
            if Answer == 'y':
                os.system('Clear')
                print('Congratulations!\nYou have collected all of the items and defeated the Lich King!\nYou Win!\n\n')
                goodEnding()
                exit()
            else:
                reset_window()
                current_room = 'Throne Room'
                print('You Have Returned To The Throne Room')
        if current_room == Lich_King_room and len(player_inventory) < 6:
            
            Answer = input('Would You Like To Fight The Lich King? (y/n)')
            
            if Answer == 'y':
                os.system('Clear')
                print("You encounter the Lich King, but you don't have all the required items to stop his treachery.\nYou lose!\n\n")
                badEnding()
                exit()
            else:
                reset_window()
                current_room = 'Throne Room'
                print('You Have Returned To The Throne Room')

if __name__ == "__main__":
    main()