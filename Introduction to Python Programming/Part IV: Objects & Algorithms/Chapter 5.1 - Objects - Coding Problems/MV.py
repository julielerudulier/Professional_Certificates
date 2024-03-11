#Write a class called Thing. The constructor for Thing should
#have two required parameters: its mass and its volume, in
#that order. These should be saved as the object's mass and
#volume attributes, respectively.
#
#Additionally, the object should have two other attributes,
#weight and density. weight should be calculated by multiplying
#the mass by the gravity on earth, 9.8, and rounding to the
#nearest tenth. density should be calculated by dividing mass
#by volume and rounding to the nearest tenth.
#
#When the constructor has finished initalizing the object, it
#should thus have four attributes: mass, volume, weight, and
#density. mass and volume will have the same values given to
#the constructor, and weight and density will be calculated
#based on those values.


#Add your class here!
class Thing:
    def __init__(self, mass, volume):
        self.mass = mass
        self.volume = volume
        self.weight = round(mass * 9.8, 1)
        self.density = round(mass / volume, 1)


#The following lines of code will test your object. If it
#is written correctly, they will print:
#10
#5
#98.0
#2.0
#14.0
#75.0
#137.2
#0.2
thing_1 = Thing(10.0, 5.0)
thing_2 = Thing(14.0, 75.0)

print(thing_1.mass)
print(thing_1.volume)
print(thing_1.weight)
print(thing_1.density)
print(thing_2.mass)
print(thing_2.volume)
print(thing_2.weight)
print(thing_2.density)
