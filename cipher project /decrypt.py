## Rohit Nawani
## Decrypt!!!!

## This program is designed to decrypt the secret message.
## Step 1 --> Find e

## Define myfile
myfile = "cipher_text.txt"







## Define a function to find out the frequency of all letters
def freq(bla):
    ## Two lists
    alpha = []
    count = [1]*(len(bla))

    ## Compute alpha and count
    ## Only keep alphabetical values in the lists
    for ch in bla: 
        if ch not in alpha and (ch.isalpha() or ch == "{"): ## I cheated
            alpha.append(ch)
        elif ch in alpha and (ch.isalpha() or ch == "{"): ## I cheated
             num = alpha.index(ch)
             count[num] += 1

    ## return values
    return alpha, count








## Define step 1 --> Find e and replace it
def step1(mystring):
    print("\nStep1 \nLetter 'E' is the most frequently used letter in Englsih and so '",alpha[count.index(max(count))],"'is 'E'")
    print("\nWe are going to replace all '",alpha[count.index(max(count))],"' with 'e' as followed:\n")
    mystring = mystring.replace(alpha[count.index(max(count))],"e")
    print(mystring)







#### Define step 2 --> 
##def step2(mystring):







## open a file and read messages into a string
msg = open(myfile,"r")
mystring = msg.read()
msg.close()

## display the encrypted message
print(mystring)
print("\n"*10)

## display the frequency of all letters
alpha, count = freq(mystring)
print("Letter \t Freq")
for i in range(len(alpha)):
    print(alpha[i],"\t",count[i])

## step 1
step1(mystring)

## step 2


## THE END ##
