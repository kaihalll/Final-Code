#Import variables
import random
from Weapon import fists
from Health_Bar import HealthBar

#Create Character class
class Character:
    
    #Create name, health, health_max, and set default weapon
    def __init__(self,
                 name: str,
                 health: int,
                 ) -> None:
        self.name = name
        self.health = health
        self.health_max = health

        self.weapon = fists

    #Define the attack function
    def attack(self, target) -> None:
        AtkDamage = random.randint(self.weapon.damage, self.weapon.damage + 3)
        
        target.health -= AtkDamage
        target.health = max(target.health, 0)
        target.health_bar.update()
        print(f"{self.name} dealt {AtkDamage} damage to "
              f"{target.name} with {self.weapon.name}\n")
        
        if AtkDamage > self.weapon.damage + 2:
            print(f"{self.name} landed a critical hit!\n")

#Create Hero class
class Hero(Character):
    
    #Initialize the name, health, default weapon and set healthbar color
    def __init__(self,
                 name: str,
                 health: int
                 ) -> None:
        super().__init__(name=name, health=health)

        self.default_weapon = self.weapon
        self.health_bar = HealthBar(self, color="green")

    #Define equip function
    def equip(self, weapon) -> None:
        self.weapon = weapon
        print(f"{self.name} equipped a(n) {self.weapon.name}!\n")

    #Define drop function
    def drop(self) -> None:
        print(f"{self.name} dropped the {self.weapon.name}!\n")
        self.weapon = self.default_weapon

#Create Enemy class
class Enemy(Character):
    
    #Initialize name, health, weapon, and healthbar color
    def __init__(self,
                 name: str,
                 health: int,
                 weapon,
                 ) -> None:
        super().__init__(name=name, health=health)
        self.weapon = weapon

        self.health_bar = HealthBar(self, color="red")