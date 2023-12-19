import tkinter as tk
from tkinter import ttk
import tkinter.simpledialog as sd
import random
from abc import ABC, abstractmethod

from classPokemon import *
from classInheritance import *

class BattleMenu:
    def __init__(self, master, player_pokemon, opponent_pokemon):
        self.master = master
        self.window = tk.Toplevel(master)
        self.window.title("Pokémon Battle Menu")
        
        self.player_pokemon = player_pokemon
        self.opponent_pokemon = opponent_pokemon

        self.frame_main = tk.Frame(self.master)
        self.frame_main.pack()
        
        self.action_log = tk.Text(self.window, height=10, width=60)
        self.action_log.pack()

        self.moves_label = tk.Label(self.window, text="Moves:")
        self.moves_label.pack()

        self.move_listbox = tk.Listbox(self.window, height=4)
        for move in self.player_pokemon.move_damage.keys():
            self.move_listbox.insert(tk.END, move)
        self.move_listbox.pack()

        self.fight_button = tk.Button(self.window, text="Fight", command=self.fight)
        self.fight_button.pack()

        self.switch_button = tk.Button(self.window, text="Switch Pokémon", command=self.switch_pokemon)
        self.switch_button.pack()

        self.available_pokemon_label = tk.Label(self.window, text="Available Pokémon for Switching:")
        self.available_pokemon_label.pack()

        self.available_pokemon_listbox = tk.Listbox(self.window, height=4)
        for pokemon in self.get_available_pokemon():
            self.available_pokemon_listbox.insert(tk.END, pokemon.name)
        self.available_pokemon_listbox.pack()

        self.action_log.insert(tk.END, f"Player calls {player_pokemon.name}\n")
        self.action_log.insert(tk.END, f"Opponent calls {opponent_pokemon.name}\n")
        self.health_bar()
        self.window.mainloop()

    def update_display(self):
        self.action_log.delete(1.0, tk.END)
        self.action_log.insert(tk.END, f"{self.player_pokemon.name} HP: {self.player_pokemon._hp}\n")
        self.action_log.insert(tk.END, f"{self.opponent_pokemon.name} HP: {self.opponent_pokemon._hp}\n\n")

        # Update player's health bar
        self.player_health_bar["maximum"] = self.player_pokemon.max_hp
        self.player_health_bar["value"] = self.player_pokemon._hp
        self.label_player_pokemon.config(text=f"[User] {self.player_pokemon.name}: {self.player_pokemon._hp} HP")

        # Update opponent's health bar
        self.opponent_health_bar["maximum"] = self.opponent_pokemon.max_hp
        self.opponent_health_bar["value"] = self.opponent_pokemon._hp
        self.label_opponent_pokemon.config(text=f"{self.opponent_pokemon.name}: {self.opponent_pokemon._hp} HP")

    
    def health_bar(self):
        self.player_health_bar = ttk.Progressbar(self.frame_main, length=200, mode="determinate",
                                                maximum=self.player_pokemon.max_hp, value=self.player_pokemon._hp)
        self.player_health_bar.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        self.label_player_pokemon = tk.Label(self.frame_main, text=f"[User] {self.player_pokemon.name}: {self.player_pokemon._hp} HP")
        self.label_player_pokemon.grid(row=0, column=1, padx=10, pady=10, sticky="w")

        self.opponent_health_bar = ttk.Progressbar(self.frame_main, length=200, mode="determinate",
                                                   maximum=self.opponent_pokemon.max_hp, value=self.opponent_pokemon._hp)
        self.opponent_health_bar.grid(row=1, column=0, padx=10, pady=10, sticky="w")

        self.label_opponent_pokemon = tk.Label(self.frame_main, text=f"{self.opponent_pokemon.name}: {self.opponent_pokemon._hp} HP")
        self.label_opponent_pokemon.grid(row=1, column=1, padx=10, pady=10, sticky="w")

    def update_health_bar(self):
        # Update player's health bar
        self.player_health_bar["value"] = self.player_pokemon._hp

        # Update opponent's health bar
        self.opponent_health_bar["value"] = self.opponent_pokemon._hp
        
    
    def fight(self):
        player_move = self.move_listbox.get(tk.ACTIVE)
        opponent_move = random.choice(list(self.opponent_pokemon.move_damage.keys()))

        self.action_log.insert(tk.END, f"\nPlayer's {self.player_pokemon.name} uses {player_move}!\n")
        
        damage_to_opponent = self.calculate_damage(self.player_pokemon, self.opponent_pokemon, player_move)
        
        fainted_opponent = self.opponent_pokemon.take_damage(damage_to_opponent)
        
        self.action_log.insert(tk.END, f"\n{self.opponent_pokemon.name} takes {damage_to_opponent} damage! "
                                      f"\n{self.opponent_pokemon.name} Remaining HP: {self.opponent_pokemon._hp}\n")
        
        self.action_log.insert(tk.END, f"\nOpponent's {self.opponent_pokemon.name} uses {opponent_move}!\n")
        
        damage_to_player = self.calculate_damage(self.opponent_pokemon, self.player_pokemon, opponent_move)

        fainted_player = self.player_pokemon.take_damage(damage_to_player)

        self.action_log.insert(tk.END, f"\n{self.player_pokemon.name} takes {damage_to_player} damage! "
                                      f"\n{self.player_pokemon.name} Remaining HP: {self.player_pokemon._hp}\n\n")

        if fainted_opponent:
            self.action_log.insert(tk.END, f"{self.opponent_pokemon.name} has fainted!\n")
            self.action_log.insert(tk.END, f"{self.player_pokemon.name} WIN!\n")
            self.fight_button.config(state='disabled')
            self.switch_button.config(state='disabled')

        if fainted_player:
            self.action_log.insert(tk.END, f"{self.player_pokemon.name} has fainted!\n")
            self.action_log.insert(tk.END, f"{self.opponent_pokemon.name} WIN!\n")
            self.fight_button.config(state='disabled')
            self.switch_button.config(state='disabled')

        self.update_health_bar()
    
    def calculate_damage(self, attacker, defender, move):
        # Menggunakan damage yang disimpan di Pokemon.move_damage
        base_damage = attacker.move_damage[move]
        effectiveness = self.get_type_effectiveness(attacker.type_, defender.type_)
        
        # Perhitungan damage sesuai dengan rumus yang diinginkan
        damage = (attacker.attack * effectiveness) - (defender.defense // 4)

        # Tambahkan pesan ke log sesuai dengan efektivitas tipe
        if effectiveness > 1:
            self.action_log.insert(tk.END, f"Super Effective! {move} deals double damage!\n")
        elif effectiveness < 1:
            self.action_log.insert(tk.END, f"Not Very Effective! {move} deals half damage.\n")
        else:
            damage_message = ""

        return damage


    def get_type_effectiveness(self, attack_type, defense_type):
        type_effectiveness_chart = {
            "fire": {"water": 0.5, "grass": 2, "electric": 1},
            "water": {"fire": 2, "grass": 0.5, "electric": 1},
            "grass": {"fire": 0.5, "water": 2, "electric": 1},
            "electric": {"water": 2, "grass": 0.5, "fire": 1}
        }
        return type_effectiveness_chart.get(attack_type, {}).get(defense_type, 1)

    def switch_pokemon(self):
        new_pokemon = self.choose_pokemon_dialog()  # Function to choose a new Pokemon
        if new_pokemon:
            self.action_log.insert(tk.END, f"Player switches to {new_pokemon.name}!\n")
            self.player_pokemon = new_pokemon
            self.move_listbox.delete(0, tk.END)  # Clear existing moves
            for move in self.player_pokemon.move_damage.keys():
                self.move_listbox.insert(tk.END, move)
            self.available_pokemon_listbox.delete(0, tk.END)  # Clear existing available Pokemon
            for pokemon in self.get_available_pokemon():
                self.available_pokemon_listbox.insert(tk.END, pokemon.name)
            self.update_display()

    def choose_pokemon_dialog(self):
        # Create a simple dialog box to choose a Pokemon
        available_pokemon = self.get_available_pokemon()
        chosen_pokemon_index = sd.askinteger("Switch Pokemon", "Choose a Pokemon:", initialvalue=0, minvalue=0,
                                             maxvalue=len(available_pokemon) - 1, parent=self.window)

        # Find the chosen Pokemon by index
        chosen_pokemon = available_pokemon[chosen_pokemon_index]

        return chosen_pokemon

    def get_available_pokemon(self):
        # Return a list of available Pokemon for the player to choose from
        all_pokemons = [
            Electric('Pikachu', 95, 30, 30, ['Thunder Shock', 'Quick Attack', 'Thunderbolt', 'Iron Tail']),
            Fire('Charmander', 90, 25, 30, ['Ember', 'Scratch', 'Flamethrower', 'Fire Punch']),
            Grass('Bulbasaur', 80, 22, 28, ['Vine Whip', 'Tackle', 'Razor Leaf', 'Poison Powder']),
            Water('Squirtle', 88, 26, 25, ['Water Gun', 'Tackle', 'Bite', 'Hydro Pump']),
            Normal('Jigglypuff', 100, 20, 22, ['Sing', 'Pound', 'Double Slap', 'Hyper Voice']),
        ]
        return all_pokemons