#part1

class Musician:
    def __init__(self,name,instrument,skill_level):
        self.name = name
        self.instrument = instrument
        self.skill_level = skill_level

    def play(self):
        return f"{self.name} plays the {self.instrument}"

    def get_info(self):
        return f"{self.name} plays the {self.instrument} at skill level {self.skill_level}"

    def practice(self):
        self.skill_level +=1
        

musician1 = Musician("Aoife", "fiddle", 7)
print(musician1.play())
print(musician1.get_info())
musician1.practice()
print(musician1.get_info())

#past2

class Session:
    def __init__(self,musicians, location):
        self.__musicians = []
        self.__location = location

    def add_musician(self,musician):
        self.__musicians.append(musician)

    def remove_musician(self,musician):
        if musician in self.__musicians:
            self.__musicians.remove(musician)
            print(f"{musician.name} removed")
        else:
            print(f"{musician.name} wasn't found")

    def get_musician_count(self):
        count = len(self.__musicians)
        return count

    def list_musicians(self):
        for musician in self.__musicians:
            print(f"{musician.name} is playing")

    def get_location(self):
        location = self.__location
        return location

session = Session("The Cobblestone", 5)
session.add_musician(musician1)
session.add_musician(Musician("Liam", "guitar", 6))
session.list_musicians()
print(f"Musicians in session: {session.get_musician_count()}")


#part 3

class LeadMusician(Musician):
    def __init__(self, name, instrument, skill_level,specialty):
        super().__init__(name, instrument, skill_level)
        self.specialty = specialty

    def play(self):
        return f"{self.name} leads the session with {self.specialty} on {self.instrument}"

    def start_tune(self,tune_name):
        return f"{self.name} starts playing {tune_name}"

class BeginnersMusician(Musician):
    def __init__(self, name, instrument, skill_level):
        super().__init__(name, instrument, skill_level)
        self.learning = True
        

    def play(self):
        return f"{self.name} is learning to play the {self.instrument}"
    
    def graduate(self,musician):
        if self.learning is True:
            self.skill_level +=2

lead = LeadMusician("Máire", "flute", 9, "slip jigs")
beginner = BeginnersMusician("Tom", "bodhrán", 3)

print(lead.play())
print(lead.start_tune("The Butterfly"))
print(beginner.play())
beginner.graduate(Musician)
print(f"{beginner.name} skill level: {beginner.skill_level}")

#part4

def hold_session(musicians):
    print("---Session Starting---")
    for musician in musicians:
        print(musician.play())


musicians = [
    Musician("Aoife", "fiddle", 7),
    LeadMusician("Máire", "flute", 9, "slip jigs"),
    BeginnersMusician("Tom", "bodhrán", 3)
]

hold_session(musicians)