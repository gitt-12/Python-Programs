#String Functions and how these work in python
story="hi, This is Git. And I'm practising python program. I'm stufying in IIT (ISM), Dhanbad. That's it!"
#string functions

print(len(story)) #1length of the characters in the string

print(story.endswith("!")) #2to check if it ends with the given character

print(story.count("o")) #3to have the total number of letters in the string of the particular letter. also works for combination of letters

print(story.capitalize()) #4capitalize the first letter of the string

print(story.find("And")) #5it returns the position at which the word is there in the character. if it is not there, then it returns -1.

print(story.replace("I'm", "Git")) #6replace each I'm by Git(oldword by new word)




***OUTPUT***
1)98
2)True
3)2
4)Hi, this is git. and i'm practising python program. i'm stufying in iit (ism), dhanbad. that's it!
5)17
6)hi, This is Git. And Git practising python program. Git stufying in IIT (ISM), Dhanbad. That's it!
> 
