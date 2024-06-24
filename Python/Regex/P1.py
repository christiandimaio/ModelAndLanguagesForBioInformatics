"write a pattern for recognizing a legal email address (imagining that the address can only end with .it or .com or .org)"
import re


def email(address:str)->bool:
   it=r"@(.+?).it$"
   com=r"@(.+?).com$"
   org=r"@(.+?).org$"
    
   if(re.search(it,address) or re.search(com,address) or
      re.search(org,address)):
       return True
   else:
       return False
