from operator import and_

#magicians =['Dark Magician', 'Dark Magician Girl', 'Dark Magician of Chaos']
#attacks =['Dark Magic Attack', 'Dark Burning Attack', 'Spell of Destruction - Death Ultima']

magicians = {'Dark Magician': 'Dark Magic Attack', 'Dark Magician Girl': 'Dark Burning Attack', 'Dark Magician of Chaos': 'Spell of Destruction - Death Ultima'}

def greet_user():
    """Display a simple greeting."""
print("Hello!")
greet_user()

def greet_user(username):
    """Display a simple greeting."""
    print("Hello, " + username.title() + "!")
greet_user('jesse')


def explanation(thingy):
    """explains what I'm learning about"""
    print("today I'm trying to understand " + thingy + ", I do not really get it :o")
explanation("functions")

def describe_pet(animal_type, pet_name): 
    """Display information about a pet."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")
describe_pet('hamster', 'harry')
describe_pet('dog', 'willie')

class Dog():
    """A simple attempt to model a dog."""
    def __init__(self, name, age):
        """Initialize name and age attributes."""
        self.name = name 
        self.age = age
    def sit(self):
        """Simulate a dog sitting in response to a command.""" 
        print(self.name.title() + " is now sitting.")
    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(self.name.title() + " rolled over!")
 
my_dog = Dog('willie', 6)
print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")

