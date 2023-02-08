'''
Mono-Alphabetic Encryptor/Decryptor
By: Mohamed Tarek
GitHub: https://github.com/motarekk
LinkedIn: https://www.linkedin.com/in/mohamed-tarek-159a821ba/
'''

import sys

#----VARIABLES----#
description = "++ Mono-Alphabetic Substitution Cipher ++\n"
usage = "Usage: '-e' to Encrypt\n       '-d' to Decrypt"
alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
#fixed key, you can changed it with your key
key = ['Y','I','R','E','V','J','S','Z','O','M','A','H','Q','N','C','G','K','B','X','F','W','L','D','T','P','U']

if len(sys.argv) < 2:
    print(description + usage)

#----ENCRYPTION----#
elif sys.argv[1] == '-e':

    #take plaintext from user
    plain = input("Please Enter Plaintext to Encrypt:\n")

    #put plaintext in an array
    plainArr = [''] * len(plain)

    for i in range(0, len(plain)):
        plainArr[i] = plain[i].upper()

    #Encrypt
    ciphered = [''] * len(plainArr)
    exists = False
    for p in range(0, len(plainArr)):
        for a in range(len(alphabet)):
            if plainArr[p] == alphabet[a]:
                ciphered[p] = key[a]
                exists = True
                break
            else:
                exists = False

        if not exists:
            ciphered[p] = plainArr[p]

    #print ciphertext
    print("Ciphertext:" , end=" ")
    for n in range(len(plainArr)):
        print(ciphered[n], end="")
    print('\n')

#----DECRYPTION----#
elif sys.argv[1] == '-d':

    #take plaintext from user
    cipher = input("Please Enter Ciphertext to Decrypt:\n")

    #put ciphertext in an array
    cipherArr = [''] * len(cipher)

    for i in range(0, len(cipher)):
        cipherArr[i] = cipher[i].upper()

    #Decrypt
    plained = [''] * len(cipherArr)
    exists = False
    for c in range(0, len(cipherArr)):
        for a in range(len(alphabet)):
            if cipherArr[c] == key[a]:
                plained[c] = alphabet[a]
                exists = True
                break
            else:
                exists = False

        if not exists:
            plained[c] = cipherArr[c]

    #print ciphertext
    print("Plaintext:" , end=" ")
    for n in range(0, len(plained)):
        print(plained[n], end="")

    print('\n')

else:
    print(usage)
