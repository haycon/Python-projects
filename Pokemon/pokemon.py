class Pokemon:
  
  def __init__(self, name, level, type, health, alive):
    self.name = name
    self.level = level
    self.type = type
    self.health = health
    self.knocked_out = False
    
    
  def __repr__(self):
      return self.name + " has got " + str(self.health) + "hp and is level "+ str(self.level) +"."
  
  def knock_out(self):
    self.knocked_out = True
    if(self.health!=0):
      self.health = 0
    
  def lose_health(self, damage):
    self.health -= damage
    if(self.health<=0):
      self.knock_out()
  
  
  def gain_health(self, healing):
    self.health += healing
    print(self.name + " now has " + str(self.health) + " health")
  
  

    
    
  def revive(self):
    self.knocked_out = False
    if(self.health==0):
      self.health = 1
    print(self.name+" was revived!")
  
  
  def attack(self, other_pokemon):
    if self.knocked_out:
        print("Your pokemon is knocked out.")
        return
    if( (self.type == "Fire" and other_pokemon.type == "Grass") or (self.type == "Water" and other_pokemon.type == "Fire") or (self.type == "Grass" and other_pokemon.type == "Water")):
      other_pokemon.lose_health(self.level*2)
      print("Highly effective! " + self.name +" dealt " + str(self.level*2) + " damage to " + other_pokemon.name)

    if( (self.type == "Fire" and other_pokemon.type == "Fire") or (self.type == "Water" and other_pokemon.type == "Water") or (self.type == "Grass" and other_pokemon.type == "Grass") ):
      other_pokemon.lose_health(self.level)
      print( "Normal damage, " + self.name + " dealt " + str(self.level) + " damage to " + other_pokemon.name )   
    
    if( (self.type == "Fire" and other_pokemon.type == "Water") or (self.type == "Water" and other_pokemon.type == "Grass") or (self.type == "Grass" and other_pokemon.type == "Fire") ):
      other_pokemon.lose_health(self.level*0.5)
      print( "Not effective! " + self.name + " dealt " + str(self.level*0.5) + " damage to " + other_pokemon.name)

class Trainer:
    def __init__(self, pokemon_list, num_potions, name):
        self.pokemons = pokemon_list
        self.potions = num_potions
        self.current_pokemon = 0
        self.name = name

    def __repr__(self):
        print(self.name + ", you have these pokemons: ")
        for pokemon in self.pokemons:
            print(pokemon)
        return "Your active pokemon is " + self.pokemons[self.current_pokemon].name + "\n"

    def switch_active_pokemon(self, new_active):
        if new_active < len(self.pokemons) and new_active >= 0:
            if self.pokemons[new_active].knocked_out:
                print( self.pokemons[new_active] + " is knocked out.")
            elif new_active == self.current_pokemon:
                print(self.pokemons[new_active] +" is already your active pokemon")
            else:
                self.current_pokemon = new_active
                print("Switched to " + self.pokemons[self.current_pokemon].name)

    def use_potion(self):
        if self.potions > 0:
            print("You used a potion on " + self.pokemons[self.current_pokemon].name + "\n")
            self.pokemons[self.current_pokemon].gain_health(30)
            self.potions -= 1
        else:
            print("You are out of potions")

    def attack_other_trainer(self, other_trainer):
        my_pokemon = self.pokemons[self.current_pokemon]
        other_pokemon = other_trainer.pokemons[other_trainer.current_pokemon]
        my_pokemon.attack(other_pokemon)
        
charmander = Pokemon("Charmander", 5, "Fire", 100, True)
squirtle = Pokemon("Squirtle", 5, "Water", 100, True)
bulbasar = Pokemon("Bulbasar", 5, "Grass", 100, True)

charizard = Pokemon("Charizard", 50, "Fire", 100, True)
blastoise = Pokemon("Blastoise", 50, "Water", 100, True)
venusaur = Pokemon("Venusaur", 50, "Grass", 100, True)

pokelist = [charmander, squirtle, bulbasar]
pokelist2 = [charizard, blastoise, venusaur]

trainer1 = Trainer(pokelist, 2, "Ash")
trainer2 = Trainer(pokelist2, 2, "Brock")


print("Pokebattle!\n"+trainer1.name + " VS "+trainer2.name +"\n")
print(trainer1)
print(trainer2)
print(trainer2.name + "'s turn to attack.")
trainer2.attack_other_trainer(trainer1)
print(trainer1.name + "'s turn to attack.")
trainer1.attack_other_trainer(trainer2)
trainer1.use_potion()
print(trainer1)
trainer1.switch_active_pokemon(2)
print(trainer1)
trainer2.attack_other_trainer(trainer1)
print(trainer1)

