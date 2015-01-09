#Sean Nicholls
#Functions Christmas Work

def get_mode():
    while True:
        mode = input('Do you wish to encrypt or decrypt a message?  ')
        mode = mode.lower()
        return mode

def get_message():
    message = input('Enter your message: ')
    return message

def get_key():
    key = 0
    while True:
        key = int(input('Enter the key number (1-25): '))
        if (key >= 1 and key <= 25):
            return key

def Get_Translated_Message(mode, message, key):
    if mode[0] == 'd':
        key = -key
    translated = ''
    for symbol in message:
        if symbol.isalpha():
            num = ord(symbol)
            num += key
            if symbol.isupper():
                if num > ord('Z'):
                    num -= 26
                elif num < ord('A'):
                    num += 26
            elif symbol.islower():
                if num > ord('z'):
                    num -= 26
                elif num < ord('a'):
                    num += 26
            translated += chr(num)
        else:
            translated += symbol
    return translated

#Main Program

mode = get_mode()
message = get_message()
key = get_key()
final = Get_Translated_Message(mode, message, key)
print('Your translated text is: "{0}"'.format(final))



