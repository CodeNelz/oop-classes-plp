class Superhero:
    def __init__(self, name, alias, power, city):
        self.__name = name  
        self.__alias = alias  
        self.__power = power
        self.__city = city  

    def get_name(self):
        return self.__name

    def get_alias(self):
        return self.__alias

    def get_power(self):
        return self.__power

    def get_city(self):
        return self.__city
    def set_name(self, name):
        self.__name = name

    def set_alias(self, alias):
        self.__alias = alias

    def set_power(self, power):
        self.__power = power

    def set_city(self, city):
        self.__city = city

    def introduce(self):
        print(f"Hello, I am {self.__name}, also known as {self.__alias}.")
        print(f"My superpower is {self.__power}, and I protect {self.__city}.")
class FlyingHero(Superhero):
    def __init__(self, name, alias, power, city, flying_speed):
        super().__init__(name, alias, power, city) 
        self.flying_speed = flying_speed  
    def introduce(self):
        super().introduce() 
        print(f"I can fly at a speed of {self.flying_speed} km/h!")

hero1 = Superhero("Bruce Wayne", "Batman", "Intelligence", "Gotham")
hero1.introduce()

hero2 = FlyingHero("Clark Kent", "Superman", "Super Strength", "Metropolis", 1000)
hero2.introduce()
