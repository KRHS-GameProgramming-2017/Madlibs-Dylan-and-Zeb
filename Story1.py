from Getter import *

# zeb waz heeer

def story1(debug= False):
    if debug: print "--In story1 function--"
    
    device1 = getWord("device1: ", debug)
    mythicalbeast1 = getWord("mythicalbeast1: ", debug)
    swear1 = getSwear("A swear: ", debug)
    place1 = getWord("A place: ", debug)
    candybar1= getWord("a candy bar: ", debug)
    name1 = getWord("name: ", debug)
   
   
    out = ""
    out += "When the " + device1
    out += " shut down,the " + mythicalbeast1
    out += " got upset and " + swearEndingWithIng 
    out += " ran out of the " + place1
    
    out = ""
    out += "Who fucking ate that " + candybar1
    out += " bar? was it you " + name1
    out += "? I swear to god  " + name1
    out += "if it was you... " 
    
    
    
    
    return out
    
    
