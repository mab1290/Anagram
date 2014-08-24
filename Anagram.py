def result(tf, first, second):
    if tf == True:
        print first.capitalize() + " and " + second.capitalize() + " are anagrams."
    else:
        print second.capitalize() + " and " + second.capitalize() + " are not anagrams."

def IsAnagram(incoming):
    first = incoming[0]
    second = incoming[1]
    first_working = first.replace(" ", "")
    second_working = second.replace(" ", "")
    
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
        
def inputting():
    incoming = raw_input("Please enter two phrases, separated by commas ")
    commacount = 0
    for letter in incoming:
        if letter is ",":
            commacount +=1

    if commacount == 0:
        print "No commas in your input, fix that."
        inputting()
    elif commacount > 1:
        print "More than one comma detectd, fix that."
        inputting()
    else:    
        incoming = incoming.split(",")
        return incoming  

def runner(i = 0):    
    if i == 0:
        print "Welcome to the is it an anagram thing"
    incoming = inputting()    
    IsAnagram(incoming)
    print "To stop, please enter 'stop', otherwise,"
    runner(1)
        
    

runner()
