"write a pattern for recognizing a string which must contain at least two of the following words: legal, Trump, policy"


import re

def check_orangeman(text:str)->bool:
    # Trump=r"Trump"
    # legal=r"Legal"
    # policy=r"policy"
    words="(Trump|legal|policy).*(?!\1)(Trump|legal|policy)"
       
    if(re.search(words,text)):
        return True
    else:
        return False
    
text=r"Mister Trump has adopted a new policy  where he only allows muricans to have two guns. Of course this policy has made all the rednecks crazy: How are we gonna kill kids in the schools? This is not legal "

if __name__ == "__main__":
    
    print(text)
    print(check_orangeman(text))
    