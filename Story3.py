from Getter import *

# zeb waz heeer

def story3(debug= False):
    if debug: print "--In story1 function--"
    
    object1 = getWord("object1: ", debug)
    weapon1 = getWord("weapon1: ", debug)
    place1 = getWord("place1: ", debug)
    emotion = getWord("emotion1: ", debug)
    animal1 = getWord("animal1: ", debug)
    verb1 = getIngWord("verb that ends in 'ing': ", debug)
    body_part1 = getWord("body_part1: ",debug)
    famous_person1 = getword(famous_person1: ",debug)
    
    
    
    out = "I was walking down the" + place1
    out += " ,until a " + animal1
    out += " jumped on me and dragged me to " + place2
    out += " once we stopped, there was a man that threw a " + weapon1
    out += " at me.When I tried to run but a " + object1
    out += " fell out of the sky and impaled in my  " +body_part1
    out += " I was getting nautious until " + famous_person1
    out += " swooped me up and threw me down a" + place3
    out += ""
    
    return out
    
    
