Lich_King_room = 'Ritual Sanctum'

# Define room configurations
rooms = {
    'Entrance to the Crypt': {'North': 'Research Room'},
    'Research Room': {'North': 'Chamber of Shadows', 'East': 'Bed Chambers', 'West': 'Treasury', 'South':'Entrance to the Crypt', 'Item': 'Tome of Dark Incantations'},
    'Treasury': {'East': 'Research Room', 'Item': 'Amulet of Undead Warding'},
    'Bed Chambers': {'West': 'Research Room', 'Item': 'Phylactery Orb'},
    'Chamber of Shadows': {'East': 'Armory', 'North': 'Throne Room', 'South': 'Research Room', 'Item': 'Orb of Shadow Veil'},
    'Armory': {'West': 'Chamber of Shadows', 'Item': 'Soul Reaper Scythe'},
    'Throne Room': {'South': 'Chamber of Shadows', 'West': 'Ritual Sanctum', 'Item': 'Cursed Crown of Dominion'},
    'Ritual Sanctum': {'East': 'Throne Room'}
}