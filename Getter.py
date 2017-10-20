def getMenuResponse(debug = False):
    if debug: print "--In getMenuResponse function--"
    goodInput = False
    while not goodInput:
        response = raw_input("Make a selection please: ")
        if (response == "1" or 
            response == "one" or 
            response == "story 1"):
                goodInput = True
                response = "1"
        elif (response == "2" or 
            response == "two" or 
            response == "story 2"):
                goodInput = True
                response = "2"
        elif (response == "3" or 
            response == "three" or 
            response == "story 3"):
                goodInput = True
                response = "3"
        elif (response == "q" or 
              response == "quit" or 
              response == "exit"):
            goodInput = True
            response = "q"
        elif (response == "zebbecool"):
            goodInput = True
            response = "zeb"
        else:
            print "Please enter a valid input!"
    return response
        
def getWord(prompt, debug):
    if debug: print "--In getWord function--"
    goodInput = False
    while not goodInput:
        response = raw_input(prompt)
        if isSwear(response):
            goodInput = False
            print "Don't go using that type of language here"
        elif response == "":
            goodInput = False
            print "Type something"
        else:
            goodInput = True
    return response
    
def getIngWord(prompt, debug):
    if debug: print "--In getIngWord function--"
    goodInput = False
    while not goodInput:
        response = raw_input(prompt)
        if isSwear(response):
            goodInput = False
            print "Don't go using that type of language here"
        elif response[-3:] == "ing":
            goodInput = True
        else:
            goodInput = False
            print "The word must end in 'ing'"
    return response
        
def getNumber(prompt, debug):
    if debug: print "--In getWord function--"
    goodInput = False
    numbers = "1234567890."
    while not goodInput:
        response = raw_input(prompt)
        goodInput = True    
        for letter in response:
            if letter not in numbers:
                goodInput = False
                print letter + " is not a number"
    return response 
            
def isSwear(word):
    swearList = ["fuck",
                 "shit",
                 "ass",
                 "Asshole", 
                 "A$$",
                 "BITCH",
                 "cunt",
                 "Nigger",
                 "Dick",
                 "Nipple",
                 "sean",
                 "CNN",
                 "Fake News",
                 "Fuck me",
                 "Carl Azus",
                 "sex",
                 "oral sex",
                 "fuck my ass",
                 "hump",
                 "dry hump",
                 "Breast" ,
                 "boner",
                 "Hoe",
                 "Male",
                 "Female",
                 "niglet",
                 "Hard dick",
                 "porn",
                 "pornstar",
                 "fuck me",
                 "Fuck you",
                 "Hell",
                 "god",
                 "Damn",
                 "Damnit",
                 "Shitty",
                 "Nutter fuckers",
                 "Porno",
                 "Fuck me in the ahole",
                 "Kiss",
                 "Butt",
                 "Blow job",
                 "blowjob",
                 "tiddies",
                 "Titties",
                 "Penis",
                 "Motherfucker",
                 "bastard",
                 "Beaver",
                 "Beef curtains",
                "Bellend",
                "Bloodclaat",
                "Clunge",
                 "Cock",
                "Dick",
               "Dickhead",
                "Fanny",
                "Flaps",
                "Gash",
                "Knob",
                "Minge",
                "Prick",
                "Punani",
               "Pussy",
                "Snatch",
                "Twat",
                "whore",
                "Fucking",
                
            ]
            
    if word.lower() in swearList:
        return True
    else:
        return False


def getSwear(prompt, debug):
    if debug: print "--In getSwear function--"
    goodInput = False
    while not goodInput:
        response = raw_input(prompt)
        if isSwear(response):
            goodInput = True
            print "Good sir, I will have you know that that is a very naughty word!"
        elif response == "":
            goodInput = False
            print "Pls type a answer. Thx."
        else:
            goodInput = False
            print "more of a swear than that"
        
        
    return response
        
