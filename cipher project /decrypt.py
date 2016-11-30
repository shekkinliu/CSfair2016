## Rohit Nawani
## Decrypt!!!!

## This program is designed to decrypt the secret message.

## IMPORT
import decrypt_functions

## Define myfile
myfile = "cipher_text.txt"

## open a file and read messages into a string
msg = open(myfile,"r")
mystring = msg.read()
msg.close()

## display the encrypted message
print("Here is the encrypted message:\n")
print(mystring)
print("\n"*5)

## letter counts
diction1, alpha1, count1 = decrypt_functions.gram1(mystring)

## Step 1 --> Find e and replace it
## e
mystring_1 = decrypt_functions.find_e(mystring, alpha1)

## Bigram counts
diction2, alpha2, count2 = decrypt_functions.gram2(mystring)

## Trigram counts
diction3, alpha3, count3 = decrypt_functions.gram3(mystring)

## 4-gram counts
diction4, alpha4, count4 = decrypt_functions.gram4(mystring)

## Step 2 --> Find t,h and replace it
## e
## t h
mystring_2 = decrypt_functions.find_t_h(mystring_1, alpha3)

## THE END ##
