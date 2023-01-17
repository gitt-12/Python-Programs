***1)Write a python program to display a user entered name followed by Good Afternoon using input() function.***
--->

name=input("Enter the name:\n")
print("Good afternoon, " +name)


///output:
  Enter the name:
Git hub fam!
Good afternoon, Git hub fam!
> 


***2)Write a python program to fill in a letter template given below with name and date
letter='''Dear<|NAME|>
                you're selected!
                <|DATE|>'''

--->

letter='''Dear <|NAME|>'
I'm happy to inform you that you're selected!
thanks and regards!
Git
<|DATE|>'''
name=input("Enter the name:\n")
date=input("Enter the date:\n")
letter=letter.replace("<|NAME|>",name)
letter=letter.replace("<|DATE|>",date)
print(letter)


///OUTPUT
Enter the name:
Swagata
Enter the date:
17/01/2023
Dear Swagata'
I'm happy to inform you that you're selected!
thanks and regards!
Git
17/01/2023
> 


***3)formatted letter
--->

letter="Hello Everyone! Stay safe and healthy! Stay happy :)"
print(letter)
print(' \n\n ')
formatted_letter="Hello Everyone!\n\tstay safe and healthy!\nStay happy :)"
print(formatted_letter)


///OUTPUT
Hello Everyone! Stay safe and healthy! Stay happy :)
 

 
Hello Everyone!
	stay safe and healthy!
Stay happy :)
> 
