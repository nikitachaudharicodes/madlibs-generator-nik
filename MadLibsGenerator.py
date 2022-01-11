#Mad Libs Generator in Python
#Project1

#import packages that are needed
from random import randint
#The randint() method returns an integer number selected element from the specified range.

import copy
#The copy() method is added to the end of a list object and so it does not accept any parameters. copy() returns a new list. 
# Python includes a built-in function to support creating a shallow copy of a list: copy(). You can use the copy() method to replicate a list and leave the original list unchanged.
from tkinter import *
import tkinter

#-----------
#TO CREATE DISPLAY WINDOW:

root=Tk()
#root is the name which we give to our window

root.geometry('600x600')
root.title('Mad Libs Generator in Python')
root.wm_attributes("-modified", True)

#pack organized widget in block
Button(root, text='Mad Libs Generator', font='arial 10 bold', bg='pink').pack()
Button(root, text='Click Any One option:', font='arial 15 bold', bg='pink').place(x=40,y=80)

#place() used when we want to place widgets in a specific position



#----------------

#DEFINE FUNCTION
def madlib1():
    animals= input('enter animal name:')
    profession=input('enter a profession name:')
    cloth=input('enter a cloth type:')
    things=input('mention one thing:')
    name=input('enter one name:')
    place=input('give the name of a place:')
    verb=input('give a verb in ing form:')
    food=input('name of your favorite food:')

    print('say ' + food + ', the photographer said as the camera flashed! ' + name + ' and I had gone to ' 
    + place +' to get our photos taken on my birthday. The first photo we really wanted was a picture of us dressed as ' + animals + ' pretending to be a ' 
    + profession + '. when we saw the second photo, it was exactly what I wanted. We both looked like ' + things + ' wearing ' + cloth + ' and ' + verb + ' --exactly what I had in mind')

#-----------

def madlib2():
    namelib= input('enter name of a library:')
    nameofboy=input('enter a boys name:')
    verb2=input('enter a verb in ing form:')
    things=input('mention one thing:')
    name=input('enter one group of people:')
    place=input('give the name of a place:')
    verb=input('give a verb form:')
    food=input('name of your favorite food:')
    animals=input('give the name of an animal:')

    print('Manika worked at a library called ' + namelib + '. She hated the' + name + ' that came to the library in the evening. All the' +name+' just came there to' 
    + verb +'. This irritated her a lot. They would make a lot of noise. So, to keep her company she got a ' + animals + 'as a pet. ' 
    + nameofboy + 'was a boy who came to the library everyday and he soon became friends with Manika. Together, they plotted revenge on the'+name+'by' + verb2 + ' the free cookies that the library gave and setting ' + things + ' at every corner.')

#--------

def madlib3():
    adjective= input('enter an adjective for a thing:')
    adjective2=input('enter a visual adjective')
    color=input('enter any color:')
    personadjective=input('mention an adjective to describe a person:')
    name=input('enter one name:')
    place=input('give a name(suitable for a place):')
    verb=input('give a verb in ing form:')
    time=input('give a number')
    adjective3=input('describe with one word(physical adjective):')
    

    print('One day as I was walking to school, a'+ adjective + 'thing caught my eye. It was'+ adjective2+' and glowing. I decided to take it with me. The moment I touched it, there was a flash of'+ color+'light and I was teleported to a strange place. As I frantically looked around, I noticed a'+personadjective+ 'looking being that was staring at me. It said ''Hello'+ name+', welcome to Planet'+place+'. We are very pleased to have you here.'' The being had a'+ adjective3 +'nose and flappy ears. It had sharp teeth and looked scary. I was so scared. I tried to'+ verb+ 'away but I realised I couldnt move. As I started screaming, everything turned'+ color+ 'and I woke up with a terrible headache.'
    'I was in my own bed and the alarm was ringing. It was' +time+' in the morning. I was late for school!')

#----------------------

#DEFINE BUTTONS

Button(root, text='The Photographer', font='arial 15', command=madlib1, bg='ghost white').place(x=60, y=120)

Button(root, text='Manika:The Librarian', font='arial 15', command=madlib2, bg='ghost white').place(x=60, y=160)

Button(root, text='The space surfer!', font='arial 15', command=madlib3, bg='ghost white').place(x=60, y=200)

root.mainloop()

#--------------------------