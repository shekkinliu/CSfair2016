
# Ken Liu and Rohit Nawani
# CS fair cryptograhy project

# This program is supposed to encrypt a message from the user's input to
# a output that no human beings can read.

import random

dafile = "long_passage.txt"

infile = open(dafile,"r")
dastring = infile.read()
infile.close()

orig_string = dastring.upper()


# a list of original order of the alphabets
alpha = []
for i in range(65,91):
    alpha.append(chr(i))
print("This is the list of alphabets in order:")
print(alpha)
print("\n")

# a list of shuffled order of the alphabets
shuffle = alpha.copy()
random.shuffle(shuffle)
print("This is the list of alphabets after shuffling:")
print(shuffle)
print("\n")

# making a key to convert
key = {}
for i in range(0,26):
    key[alpha[i]] = shuffle[i]
print("This is the key of what characters the message is being converted to:")
print(key)
print("\n")

# making a table to display the key in a better view
print("Original Alphabets ---> Encrypted Alphabets")
for i in range(26):
    print("\t",alpha[i],"\t   --->\t\t",key[alpha[i]])

print("\n"*5)

outfile = open("cipher_text.txt","w")
char = ""
da_msg = ""
for ch in orig_string:
    if ch.isalpha():
        char = key[ch]
        da_msg += char
        outfile.write(char)
    else:
        da_msg += ch
        outfile.write(ch)

print("Original message as followed:\n")
print(orig_string)

print("\n"*10)

print("Enrypted message as followed:\n")
print(da_msg)

outfile.close()
