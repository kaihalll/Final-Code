#Import libraries & variables
import os
import random
from Character import Hero, Enemy
from Weapon import short_bow, iron_sword, fists

#Define hero and enemy
hero = Hero(name="Hero", health=100)
hero.equip(iron_sword)
enemy = Enemy(name="Enemy", health=100, weapon=short_bow)

#Clear terminal
os.system('cls' if os.name == 'nt' else 'clear')


#Print instructions
print(f"Hello {hero.name}. You have two options each round:\n1. Heal\n2. Change Weapons\n\nTo heal, type heal and everyone will be healed a random amount from 4-8;\nTo Change Weapons, type select 'name of your weapon'. For example: select iron_sword, select short_bow, select fists.")
input("\n\nPress Enter To Proceed...")
os.system('cls' if os.name == 'nt' else 'clear')

#Infinite loop
while True:
    #Print instructions
    print("To heal, type heal and you will be healed a random amount from 4-8;\nTo Change Weapons, type select 'name of your weapon'. For example: select iron_sword, select short_bow, select fists.")
    
    #Run attack functions
    hero.attack(enemy)
    enemy.attack(hero)
    
    #Draw the healthbars
    hero.health_bar.draw()
    enemy.health_bar.draw()
    
    #Stop the loop until player inputs
    playerInput = input("\n")
    
    #Give player selected weapon
    if playerInput.lower() == "select iron_sword":
        hero.equip(iron_sword)
    elif playerInput.lower() == "select short_bow":
        hero.equip(short_bow)
    elif playerInput.lower() == "select fists":
        hero.equip(fists)
    
    #Heal everyone random amount
    if playerInput.lower() == "heal":
        healEffectiveness = random.randint(5, 8)
        hero.health += healEffectiveness
        print(f"{hero.name} has been healed {healEffectiveness} HP!")
        
        healEffectiveness = random.randint(5, 8)
        enemy.health += healEffectiveness
        print(f"{enemy.name} has been healed {healEffectiveness} HP!\n")
        
    #Stop progressing until player input
    print("\n\nPress Enter to Progress to Next Round...")
    input()
    
    #End game if health is 0
    if hero.health == 0:
        print(f"The game is over. {enemy.name} won!")
        break
    elif enemy.health == 0:
        print(f"The game is over. {hero.name} won!")
        break
    elif hero.health == 0 and enemy.health == 0:
        print(f"The game is over. Nobody won.")
        break
    
    #Clear terminal
    os.system('cls' if os.name == 'nt' else 'clear')