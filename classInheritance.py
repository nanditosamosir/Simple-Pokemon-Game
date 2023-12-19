import tkinter as tk
from tkinter import ttk
import tkinter.simpledialog as sd
import random
from abc import ABC, abstractmethod

from classPokemon import *

class Electric(Pokemon):
    def __init__(self, name, hp, attack, defense, moves):
        self.type_ = type_ = 'electric'
        self.name = name
        self._hp = hp
        self.max_hp = hp
        self.attack = attack
        self.defense = defense
        
        self.move_damage = {move: random.randint(15, 25) for move in moves}
    
class Normal(Pokemon):
    def __init__(self, name, hp, attack, defense, moves):
        self.type_ = type_ =  'normal'
        self.name = name
        self._hp = hp
        self.max_hp = hp
        self.attack = attack
        self.defense = defense
        
        self.move_damage = {move: random.randint(15, 25) for move in moves}

class Fire(Pokemon):
    def __init__(self, name, hp, attack, defense, moves):
        self.type_ = type_ =  'fire'
        self.name = name
        self._hp = hp
        self.max_hp = hp
        self.attack = attack
        self.defense = defense
        
        self.move_damage = {move: random.randint(15, 25) for move in moves}

class Water(Pokemon):
    def __init__(self, name, hp, attack, defense, moves):
        self.type_ = type_ =  'water'
        self.name = name
        self._hp = hp
        self.max_hp = hp
        self.attack = attack
        self.defense = defense
        
        self.move_damage = {move: random.randint(15, 25) for move in moves}

class Grass(Pokemon):
    def __init__(self, name, hp, attack, defense, moves):
        self.type_ = type_ =  'grass'
        self.name = name
        self._hp = hp
        self.max_hp = hp
        self.attack = attack
        self.defense = defense
        
        self.move_damage = {move: random.randint(15, 25) for move in moves}