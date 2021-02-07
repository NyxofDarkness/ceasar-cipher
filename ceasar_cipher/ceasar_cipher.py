# text = input("Please enter your text to encrypt")
# key = input("Please enter your key: ")
import nltk

nltk.download('words', quiet=True)

from nltk.corpus import words

word_list = words.words()
# print(word_list)
def encrypt(message, key):
    """[that takes in a plain text phrase and a numeric shift]
    Args:
        message ([str]): [user given message]
        key ([int]): [intravels to change the letter to]

    Returns:
        [str]: [encryted message]
    """
    encrypted_text = ''
    # for loop
    for i in range(len(message)):
        char = message[i]
        if not char.isalpha():
            encrypted_text = encrypted_text + char
        #encrypts uppercase letters-set to 27 so that we can't just put 26 and get back the message unencrypted!
        if(char.isupper()):
            encrypted_text += chr((ord(char) + key-65) % 27 +65)

        # Now encrypt the lowercase!
        else:
            if(char.islower()):
                encrypted_text += chr((ord(char) + key - 97) % 27 + 97)
    
    return encrypted_text

def decrypt(message, key):
    """[that takes in an encryted message and a numeric shift to decode]
    Args:
        message ([str]): [encryted user given message]
        key ([int]): [intravelkey to solve]

    Returns:
        [str]: [unencryted message, numbers and punctuation intact]
    """
    decrypted_text = encrypt(message, -key)
    return decrypted_text

def crack(test, key_temp):
    """[decode the cipher so that an encrypted message can be transformed into its original state WITHOUT access to the key.]

    Args:
        message ([str]): [cipher that needs decoding]
    """
    # # get first encrypted word in message
    # for word in range(len(test)):
    #     # key_temp = 
        
    #     word = decrypt(test, key_temp)
    #     print(word)
    #     for word in word_list:
    #         if word is not :
    #         # return word
    #             print(word)
    #         elif word is not word_list:
    #             key_temp2 = key_temp + 1
    #             return key_temp2
    # print(key_temp)
        
    # start at key 1, check against word list
    # if not in list, increment key +1
    # if in list, return Key #
    # use Key number in decrypt()
    # return solution

message = 'It was the best of times, it was the worst of times.'
# Why are there extra letters when I just run it as key 26?
print(f'{message}')
# print(f'{key}')
key = 1
key_temp = 1
test = encrypt(message, key)
answer = crack(test, key_temp)
print(f'Ceasar Cypher: {encrypt(message, key_temp)}')
# print(f'Ceasar Cypher Decryption: {decrypt(test, key)}')
print(f'Unknown Cipher solution: Key is: {key_temp} and the message is: {answer}')