from Getter import *

# zeb waz heeer

def story1(debug= False):
    if debug: print "--In story1 function--"
    
    device1 = getWord("device1: ", debug)
    mythicalBeast1 = getWord("mythicalbeast1: ", debug)
    swear1 = getSwear("A swear: ", debug)
    place1 = getWord("A place: ", debug)
    
    out = ""
    out += "When the" + device1
    out += "shut   down,the " + mythicalBeast1
    out += "got upset and " + swear1 
    out += "ran out of ." + place1
    
      
    
    
    
    return out
    
    
