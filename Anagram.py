# Name: Anagram.py
# Description: Checks two inputs to determine if they are anagrams of each other.
# Language: Python 2.7
# Date Created: 8/19/2014

def inputting():
    # Checks the user inputs to see if they are only 2 phrases, splits input into two variables
    incoming = raw_input("Please enter two phrases, separated by a comma. ")
    commacount = 0
    for letter in incoming:
        if letter is ",":
            commacount +=1

    if commacount is not 1:
        print "You do not have excatly one comma, fix it."
        inputting()
    else:    
        incoming = incoming.split(",")
        return incoming  

def IsAnagram(incoming):
    # Creates dictionaries to hold all letters of both words and checks to see if they are identical.
    first = incoming[0]
    second = incoming[1]
    first_working = first.replace(" ", "").lower().strip()
    second_working = second.replace(" ", "").lower().strip()
    
    tf = False;
    if len(first_working) != len(second_working):
        result(tf, first, second)
        
    else:
        dict1 = dict()
        dict2 = dict()
        for letter in first_working:
            if not dict1.has_key(letter):
                dict1[letter] = 1
            else: dict1[letter] +=1
            
        for letter in second_working:
            if not dict2.has_key(letter):
                dict2[letter] = 1
            else: dict2[letter] +=1
            
        if dict1 == dict2:
            tf = True
            result(tf, first, second)
        else:
            result(tf, first, second)
        

def result(tf, first, second):
    # Reads the results from IsAnagram and prints it out to the user
    if tf == True:
        print first.strip() + " and " + second.strip() + " are anagrams."
    else:
        print first.strip() + " and " + second.strip() + " are not anagrams."


def Master(i = 0):
    # The main function that calls all other functions
    if i == 0:
        print "Welcome to the 'Is It an Anagram?' function!"
    incoming = inputting()    
    IsAnagram(incoming)
    staphit = raw_input("To stop, please enter 'stop', otherwise, press the enter key. ")
    if staphit == 'stop':
        print "Thanks for using this program!"
    else:    
        Master(1)
        
    

Master()
