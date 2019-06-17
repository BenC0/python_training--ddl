# ------------------------------------------------------------------------------
# Exercise
# 1. Loop through the props list and store it, alongisde the corresponding value
# in the internetAnimalNamesDictionary.

# 3. Now that the internetAnimalNamesDictionary is defined, we want to make it
# usable. Write the code to take a users input and return the internet translation
# for example, inputting "Python" should return "Danger Noodle"
# ------------------------------------------------------------------------------

# Exercise
# 1. Loop through the props list and store it, alongisde the corresponding value,
# in the internetAnimalNamesDictionary.

props = ["Python", "Ferret", "Grizzly Bear", "Skunk", "Racoon"]
values = ["Danger Noodle", "Cat Snake", "Sir Huggles Von Deathcuddle", "Fart Squirrel", "Trash Panda"]

internetAnimalNamesDictionary = {}

print(internetAnimalNamesDictionary)

# Exercise
# 2. Declare a function that will return the internet translation of an animals
# name and "Translation not found" when the translation is not found. 
# for example, "Python" should return "Danger Noodle" and "Dog" should return
# "Translation not found"

def internetTranslation(input):
	internetAnimalNamesDictionary = {'Python': 'Danger Noodle', 'Ferret': 'Cat Snake', 'Grizzly Bear': 'Sir Huggles Von Deathcuddle', 'Skunk': 'Fart Squirrel', 'Racoon': 'Trash Panda'}
	pass


# Exercise
# 3. Now that the internetTranslation() is defined, we want to make it
# usable. Write the code to take a users input and return the internet translation
# The logged message should be along the lines of:
# 	"The internet translation of Racoon is Trash Panda"