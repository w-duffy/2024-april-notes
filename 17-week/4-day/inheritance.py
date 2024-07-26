class Creature:
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def speak(self):
        return f"{self.name} makes a generic sound."

    def attack(self):
        return f"{self.name} attacks with a basic move."


class Dragon(Creature):
    def __init__(self, name, level, wing_span):
        super().__init__(name, level)
        self.wing_span = wing_span

    def speak(self):
        return f"{self.name} roars loudly!"

    def attack(self):
        return f"{self.name} breathes fire!"

    def __str__(self):
        return f"< {self.name} is a Level {self.level} Dragon with a {self.wing_span}m wingspan >"


class Elf(Creature):
    def __init__(self, name, level, bow_type):
        super().__init__(name, level)
        self.bow_type = bow_type

    def speak(self):
        return f"{self.name} says 'For the Elven Kingdom!'"

    def attack(self):
        return f"{self.name} shoots an arrow using their {self.bow_type} bow!"

    def __str__(self):
        return f"< {self.name} is a Level {self.level} Elf wielding a {self.bow_type} bow >"


class Golem(Creature):
    def __init__(self, name, level, material):
        super().__init__(name, level)
        self.material = material

    def speak(self):
        return f"{self.name} grumbles."

    def attack(self):
        return f"{self.name} punches with immense force!"

    def __str__(self):
        return f"< {self.name} is a Level {self.level} Golem made of {self.material} >"


spyro = Dragon("Spyro", 25, 5)
legolas = Elf("Legolas", 15, "Yew")
rocky = Golem("Rocky", 30, "Stone")

#Polymorphism is shown by each derived class providing its version of the speak and attack methods.
def creature_action(creature):
    print(creature)
    print(creature.speak())
    print(creature.attack())
    print("-----")

creature_action(spyro)
creature_action(legolas)
creature_action(rocky)


