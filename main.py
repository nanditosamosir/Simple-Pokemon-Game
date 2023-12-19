import tkinter as tk
from tkinter import ttk
import tkinter.simpledialog as sd
import random
from abc import ABC, abstractmethod

from classPokemon import *
from classInheritance import*
from battleMenu import *

if __name__ == '__main__':
    Pikachu = Electric('Pikachu', 95, 30, 30, ['Thunder Shock', 'Quick Attack', 'Thunderbolt', 'Iron Tail'])
    Squirtle = Water('Squirtle', 95, 26, 25, ['Water Gun', 'Tackle', 'Bite', 'Hydro Pump'])
    Charmander = Fire('Charmander', 95, 25, 30, ['Ember', 'Scratch', 'Flamethrower', 'Fire Punch'])
    Bulbasaur = Grass('Bulbasaur', 95, 22, 28, ['Vine Whip', 'Tackle', 'Razor Leaf', 'Poison Powder'])
    Jigglypuff = Normal('Jigglypuff', 100, 20, 22, ['Sing', 'Pound', 'Double Slap', 'Hyper Voice'])
     
    Electabuzz = Electric('Electabuzz', 100, 27, 28, ['Quick Attack', 'Screech', 'ThunderPunch', 'Thunder'])
    Goldeen = Water('Goldeen', 90, 25, 25, ['Peck', 'Tail Whip', 'Waterfall', 'Fury Attack'])
    Flareon = Fire('Flareon', 90, 32, 28, ['Fire Spin', 'Ember', 'Tackle', 'Bite'])
    Exeggutor = Grass('Exeggutor', 100, 22, 33, ['Leech Seed', 'Solar Beam', 'Barrage', 'Stomp'])
    Snorlax = Normal('Snorlax', 110, 30, 30, ['Headbutt', 'Hyper Beam', 'Body Slam', 'Double-Edge'])
    
    pokemon_list = (Electabuzz, Exeggutor, Goldeen, Flareon, Snorlax)
    opponent_pokemon = random.choice(pokemon_list)
    masterr = 0
    player_pokemon = Pikachu
   
    root = tk.Tk()
    app = BattleMenu(root,Pikachu,opponent_pokemon)
    root.mainloop()