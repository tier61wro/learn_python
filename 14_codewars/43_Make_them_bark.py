'''
train_date: 04.05.2022
kata link: https://www.codewars.com/kata/5535572c1de94ba2db0000f6
points: 7 kyu
type: OOP
-------------
DESCRIPTION:
#Make them bark

You have been hired by a dogbreeder to write a program to keep record of his dogs.

You've already made a constructor Dog, so no one has to hardcode every puppy.

The work seems to be done. It's high time to collect the payment.

..hold on! The dogbreeder says he wont pay you, until he can make every dog object .bark().
Even the ones already done with your constructor. "Every dog barks" he says. He also refuses to rewrite them, lazy as he is.

You can't even count how much objects that bastard client of yours already made.
He has a lot of dogs, and none of them can .bark().

Can you solve this problem, or will you let this client outsmart you for good?
Practical info:

    The .bark() method of a dog should return the string 'Woof!'.

    The contructor you made (it is preloaded) looks like this:

class Dog(object):
    def __init__(self, name, breed, sex, age):
        self.name  = name
        self.breed = breed
        self.sex   = sex
        self.age   = age

    Hint: A friend of yours just told you about how javascript handles classes diferently from other programming
    languages. He couldn't stop ranting about "prototypes", or something like that. Maybe that could help you...


-------------
TRANSLATION:
-------------
===TRAINED====
-------------
'''

import codewars_test as test


#===TESTS====
print('Can you make newly created dogs bark?')
apollo = Dog('Apollo', 'Dobermann', 'male', '4')
zeus = Dog('Zeus', 'Dobermann', 'male', '4')

test.assert_equals(apollo.bark(), 'Woof!')
test.assert_equals(zeus.bark(), 'Woof!')