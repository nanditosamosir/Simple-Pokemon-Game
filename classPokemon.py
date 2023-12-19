import tkinter as tk
from tkinter import ttk
import tkinter.simpledialog as sd
import random
from abc import ABC, abstractmethod

class Pokemon:
    def __init__(self, name, hp, attack, defense, moves, type_):
        self.name = name
        self._hp = hp
        self.max_hp = hp
        self.attack = attack
        self.defense = defense
        self.type_ = type_

        # Dictionary untuk menyimpan damage setiap move
        self.move_damage = {move: random.randint(15, 25) for move in moves}

    @abstractmethod
    def take_damage(self, damage):
        self._hp -= damage
        if self._hp <= 0:
            self._hp = 0
            return True  # Pokemon has fainted
        return False