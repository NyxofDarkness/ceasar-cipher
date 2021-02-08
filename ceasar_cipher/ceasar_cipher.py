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

def crack(message):
    """[decode the cipher so that an encrypted message can be transformed into its original state WITHOUT access to the key.]

    Args:
        message ([str]): [cipher that needs decoding]
    """
    cipher = []
    cipher_string = ''
    for i in range(26):
        message_data = decrypt(message, i)
        word_split = message_data.split()
        cipher.append(word_split)

    for j in range(len(cipher)):
        current = cipher[j]
        for a in current:
            if a in word_list:
                cipher_string += a

    print(cipher_string)


# if __name__ == "__main__":
