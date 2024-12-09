def create_key(keyphrase):
    key = [ord(char) for char in keyphrase]
    return key

def shakyceasar(pattern,message):
    newmessage = ""
    keyindex = 0
    for i,char in enumerate(message):
        ochar = ord(char)
        keyindex+= 1
        if keyindex > len(pattern)-1:
            keyindex = 0
        ochar += pattern[keyindex]
        while ochar > 256:
            ochar -= 256
        char = chr(ochar)
        newmessage += char
    return newmessage

def decrypt(pattern, message):
    newmessage = ""
    keyindex = 0
    for i, char in enumerate(message):
        ochar = ord(char)
        ochar -= pattern[keyindex]
        if ochar < 0:
            ochar += 256
        char = chr(ochar)
        newmessage += char
        
        keyindex += 1
        if keyindex >= len(pattern):
            keyindex = 0
    return newmessage
    
        
