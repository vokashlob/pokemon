elements = [['Fire', [0, 0.5, 2]], ['Water', [2, 0, 0.5]], ['Grass', [0.5, 2, 0]]]


class Pokemon:
    def __init__(self, name, level, element, is_knocked_out=False):
        self.name = name
        self.level = level
        self.element = element
        self.max_health = level
        self.health = self.max_health
        self.is_knocked_out = is_knocked_out

    def __repr__(self):
        return self.name

    def knocked_out(self):
        self.is_knocked_out = True
        print(f'{self} is knocked_out!')

    def revive(self):
        self.health = self.max_health
        print(f'{self.name} now has {self.health} health')

    def lose_health(self, points):
        health = self.health - points
        self.health = max(health, 0)
        print(f'{self} now has {self.health} health')
        if self.health == 0:
            self.knocked_out()

    def gain_health(self, points):
        health = self.health + points
        self.health = min(health, self.max_health)
        print(f'{self} now has {self.health} health')

    def attack(self, target):
        for params in elements:
            if params[0] == target.element:
                target_index = elements.index(params)
        for params in elements:
            if params[0] == self.element:
                attacker_power = params[1][target_index]

        print(f'{self} attacks {target}!')
        print(f'{self} deals {attacker_power} damage.')
        target.lose_health(attacker_power)

class Trainer:
    def __init__(self, name, pokemons, potions, active=0):
      self.name = name
      self.pokemons = pokemons[:6] if len(pokemons) > 6 else pokemons
      self.potions = potions
      self.active = active
      self.pokemon = self.pokemons[self.active]

    def __repr__(self):
        print(f'{self.name} currently has the following pokemons:')
        for pokemon in self.pokemons:
            print(pokemon)
        return f'Current pokemon: {self.pokemon}'


    def heal(self):
        print(f"{self.name} heals {self.pokemon}")
        if self.potions > 0:
            self.pokemon.gain_health(1)
            self.potions -= 1
        else:
            print('Out of potions!')

    def attack(self, target):
        if self.pokemon.is_knocked_out:
            print(f"{self.pokemon} can't attack.")
            return
        self.pokemon.attack(target.pokemons[target.active])

    def switch(self, pokemon):
        if self.pokemon == pokemon:
            print("Can't switch on the same pokemon.")
        elif pokemon.is_knocked_out:
            print("Can't switch on knockouted pokemon")
        else:
            self.pokemon = pokemon
            print(f'{self.pokemon} is now active.')


pikachu = Pokemon("Pikachu", 3, "Fire", False)
bulbasaur = Pokemon("Bulbasaur", 3, "Grass", False)
squirtle = Pokemon("Squirtle", 3, "Water", False)

erika = Trainer('Erika', [pikachu], 2)
ramos = Trainer('Ramos', [bulbasaur, squirtle], 2)

erika.attack(ramos)
ramos.attack(erika)
ramos.heal()
erika.attack(ramos)
ramos.attack(erika)
ramos.switch(squirtle)
ramos.attack(erika)
erika.heal()
erika.heal()
erika.heal()

print(erika)