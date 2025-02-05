# class for a Superhero:

class Superhero:
    def __init__(self, name, superpower, strength):
        self.name = name
        self.superpower = superpower
        self.strength = strength

    def use_power(self):
        return f"{self.name} uses {self.superpower}!"

    def train(self):
        self.strength += 1
        return f"{self.name}'s strength increased to {self.strength}!"

class FlyingHero(Superhero):
    def __init__(self, name, superpower, strength, fly_speed):
        super().__init__(name, superpower, strength)
        self.fly_speed = fly_speed

    def use_power(self):
        return f"{self.name} flies at {self.fly_speed} mph and uses {self.superpower}!"
