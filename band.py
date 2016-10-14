class Band(object):
    def __init__(self):
        self.members = []
    def hire_musician(self, member):
        self.members.append(member)
        for member in self.members:
            print(member.name)
    def fire_musician(self, member):
        self.members.remove(member)
        for member in self.members:
            print(member.name)
    def play_song(self):
        Guitarist.tune(self)
        print("HERE WE GOOOO")
        Drummer.count(self)
        Guitarist.solo((Guitarist(self)), 8)
        Bassist.solo((Bassist(self)), 12)
        Drummer.combust(self)

class Musician(Band):
    def __init__(self, name, sounds):
        self.name = name
        self.sounds = sounds
    def solo(self, length):
        for i in range(length):
            print(self.sounds[i % len(self.sounds)], end=" ")
        print()

class Bassist(Musician): # The Musician class is the parent of the Bassist class
    def __init__(self, name):
        # Call the __init__ method of the parent class
        super().__init__(name, ["Twang", "Thrumb", "Bling"])

class Guitarist(Musician):
    def __init__(self, name):
        # Call the __init__ method of the parent class
        super().__init__(name, ["Boink", "Bow", "Boom"])

    def tune(self):
        print("Be with you in a moment")
        print("Twoning, sproing, splang")

class Drummer(Musician):
    def __init__(self, name):
        # Call the __init__ method of the parent class
        super().__init__(name, ["Tiss", "Kick", "Splash"])
        
    def count(self):
        print("One, two, three, four!")
    
    def combust(self):
        print("That's it! I'm done, I'm outta here!")

Danny = Drummer('Danny')
Adam = Guitarist('Adam')
Justin = Bassist('Justin')
Tool = Band()
Tool.hire_musician(Danny)
Tool.hire_musician(Adam)
Tool.hire_musician(Justin)
Tool.play_song()
Tool.fire_musician(Danny)

#why does this happen? print(Tool.members)
