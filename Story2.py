from Getter import *

# zeb waz heeer

def story2(debug= False):
    if debug: print "--In story1 function--"
    
    worker1= getWord("worker1: ", debug)
    object1 = getWord("object1: ", debug)
    body_part1 = getWord("body_part1: ", debug)
    place1 = getWord("place1: ", debug)
    emotion1 = getWord("emotion1: ", debug)
    animal1 = getWord("animal1: ", debug)
    verb1 = getIngWord("verb that ends in 'ing': ", debug)
    action1 = getWord("action1: ", debug)
    body_part1 = getWord("body_part1: ", debug)
    weapon1 = getWord("weapon1: ", debug)
    
    
    
    out = ""
    out += " After I left, the " + worker1
    out += " threw a " + object1
    out += " .which made a gash in my " + body_part1
    out += worker1 + " took me to. " + place1
    out += " once I woke up I was feeling " +emotion1
    out += " while I was bleeding I noticed there was a " +animal1
    out += " the anima1 started " +verb1
    out += " me while I was trying to " +action1
    out += " I had a huge gash and was bleeding from my " +body_part1
    out += " I was thinking of escaping but he/she had a " +weapon1

    return out
    
    
