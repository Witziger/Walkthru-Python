stuff = list()
stuff.append('python')
stuff.append('chuck')
stuff.sort()
print (stuff[0])
print (stuff.__getitem__(0))
print (list.__getitem__(stuff,0))

print(dir(stuff))

class PartyAnimal:
    x = 0
    def party(self) :
        self.x = self.x + 1
        print("So far", self.x)
an = PartyAnimal()
an.party()
an.party()
an.party()
PartyAnimal.party(an)
