#String Functions and how these work in python
story="hi, This is Git. And I'm practising python program. I'm stufying in IIT (ISM), Dhanbad. That's it!"
#string functions

print(len(story)) #length of the characters in the string

print(story.endswith("!")) #to check if it ends with the given character

print(story.count("o")) #to have the total number of letters in the string of the particular letter. also works for combination of letters

print(story.capitalize()) #capitalize the first letter of the string

print(story.find("And")) #it returns the position at which the word is there in the character. if it is not there, then it returns -1.

print(story.replace("I'm", "Git")) #replace each I'm by Git(oldword by new word)
