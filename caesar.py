def alphabet_position(letter):
    alphabet_position = {'A':0,'a':0,'B':1,'b':1,'C':2,'c':2,'D':3,'d':3,'E':4,'e':4,'F':5,'f':5,'G':6,'g':6,'H':7,'h':7,'I':8,'i':8,'J':9,'j':9,'K':10,'k':10,'L':11,'l':11,'M':12,'m':12,'N':13,'n':13,'O':14,'o':14,'P':15,'p':15,'Q':16,'q':16,'R':17,'r':17,'S':18,'s':18,'T':19,'t':19,'U':20,'u':20,'V':21,'v':21,'W':22,'w':22,'X':23,'x':23,'Y':24,'y':24,'Z':25,'z':25}
    position = alphabet_position[letter]
    return position

def char_from_position(position_number, upper):
    character = chr(position_number + 65)
    if upper:
        return character
    else:
        return character.lower()
    

def rotate_character(char, rot):
    if not(char.isalpha()):
        return char
    
    ''' add rot to rotate, then % 26 to remove extra if 
    it cycles past z '''
    rotated_position = (alphabet_position(char) + rot) % 26  
     
    
    ''' that returns position. need to convert to character
    from the position number '''
    if char.isupper():
        return char_from_position(rotated_position, True)
    else: 
        return char_from_position(rotated_position, False)
    

def encrypt(text, rot):
    encrypted_text = ""
    for i in list(text):
        encrypted_text += rotate_character(i, rot)
    return '<h1>form.format(encrypted_text)</h1>'

def main():
    message = input("Type a message:")
    rotate = input("Rotate by:")
    print(encrypt(message,int(rotate)))



if __name__ == "__main__":
    main()






