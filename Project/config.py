# config.py

# Stores room data
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

# Stores enemy data
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