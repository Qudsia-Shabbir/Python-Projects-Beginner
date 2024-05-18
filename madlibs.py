# Mad Libs Game

# Getting inputs from the user
animal = input("Enter an animal: ")
person_name = input("Enter a person's name: ")
fruit = input("Enter a fruit: ")
flower = input("Enter a flower: ")
country = input("Enter a country: ")

# Creating the story using the inputs
story = f"One day, {person_name} was walking through the jungle when they stumbled upon a {animal}. \
The {animal} was munching on a {fruit}, which seemed very unusual. \
Surprised, {person_name} asked the {animal} where it found the {fruit}. \
The {animal} pointed to a nearby tree full of {flower}s and said, 'In {country}, everything is possible!' \
Together, {person_name} and the {animal} went on an adventure to find more amazing things in {country}."

# Printing the story
print("\nHere is your Mad Libs story:")
print(story)
