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
diction2, alpha2, count2 = decrypt_functions.gram2(mystring_1)

## Trigram counts
diction3, alpha3, count3 = decrypt_functions.gram3(mystring_1)

## 4-gram counts
diction4, alpha4, count4 = decrypt_functions.gram4(mystring_1)

## Step 2 --> Find t,h and replace it
## e
## t h
mystring_2 = decrypt_functions.find_t_h(mystring_1, alpha3)


########################
## NEXT STEP ##
########################


## Bigram counts
diction2, alpha2, count2 = decrypt_functions.gram2(mystring_2)

## Trigram counts
diction3, alpha3, count3 = decrypt_functions.gram3(mystring_2)

## 4-gram counts
diction4, alpha4, count4 = decrypt_functions.gram4(mystring_2)

## Step 3 --> Find n and replace it
## e
## t h
## n
mystring_3 = decrypt_functions.find_n(mystring_2, alpha3)


########################
## NEXT STEP ##
########################


## Bigram counts
diction2, alpha2, count2 = decrypt_functions.gram2(mystring_3)

## Trigram counts
diction3, alpha3, count3 = decrypt_functions.gram3(mystring_3)

## 4-gram counts
diction4, alpha4, count4 = decrypt_functions.gram4(mystring_3)

## Step 4 --> Find a and replace it
## e
## t h
## n
## a
mystring_4 = decrypt_functions.find_a(mystring_3, alpha4)

########################
## NEXT STEP ##
########################


## Bigram counts
diction2, alpha2, count2 = decrypt_functions.gram2(mystring_4)

## Trigram counts
diction3, alpha3, count3 = decrypt_functions.gram3(mystring_4)

## 4-gram counts
diction4, alpha4, count4 = decrypt_functions.gram4(mystring_4)

## Step 5 --> Find d and replace it
## e
## t h
## n
## a
## d
mystring_5 = decrypt_functions.find_d(mystring_4, alpha3)

########################
## NEXT STEP ##
########################


## Bigram counts
diction2, alpha2, count2 = decrypt_functions.gram2(mystring_5)

## Trigram counts
diction3, alpha3, count3 = decrypt_functions.gram3(mystring_5)

## 4-gram counts
diction4, alpha4, count4 = decrypt_functions.gram4(mystring_5)

## Step 6 --> Find r and replace it
## e
## t h
## n
## a
## d
## r
mystring_6 = decrypt_functions.find_r(mystring_5, alpha2)

########################
## NEXT STEP ##
########################


## Bigram counts
diction2, alpha2, count2 = decrypt_functions.gram2(mystring_6)

## Trigram counts
diction3, alpha3, count3 = decrypt_functions.gram3(mystring_6)

## 4-gram counts
diction4, alpha4, count4 = decrypt_functions.gram4(mystring_6)

## Step 7 --> Find o and replace it
## e
## t h
## n
## a
## d
## r
## o
mystring_7 = decrypt_functions.find_o(mystring_6, alpha2)

########################
## NEXT STEP ##
########################


## Bigram counts
diction2, alpha2, count2 = decrypt_functions.gram2(mystring_7)

## Trigram counts
diction3, alpha3, count3 = decrypt_functions.gram3(mystring_7)

## 4-gram counts
diction4, alpha4, count4 = decrypt_functions.gram4(mystring_7)

## Step 7 --> Find i and replace it
## e
## t h
## n
## a
## d
## r
## o
## i
mystring_8 = decrypt_functions.find_i(mystring_7, alpha2)
## THE END ##
