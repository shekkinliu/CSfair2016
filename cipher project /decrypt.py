## Rohit Nawani
## Decrypt!!!!

## This program is designed to decrypt the secret message.
## Step 1 --> Find e

## Define myfile
myfile = "cipher_text.txt"







## Define step1 --> letter counts
def gram1(bla):
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
             
    ## Display results
    print("Letter \t Freq")
    for i in range(len(alpha)):
        print(alpha[i],"\t",count[i])
        
    ## return values
    return alpha, count








## Define step2 --> Find e and replace it
def step2(mystring):
    print("\nStep1\nLetter 'e' is the most frequently used letter in Englsih and so '",alpha1[count1.index(max(count1))],"'is 'e'")
    print("\nWe are going to replace all '",alpha1[count1.index(max(count1))],"' with 'e' as followed:\n")
    mystring = mystring.replace(alpha1[count1.index(max(count1))],"e") ## Replace e
    mystring_ = ""
    for ch in mystring:
        if ch == "e":
            mystring_ += ch
        elif ch.isalpha():
            mystring_ += "_"
        else:
            mystring_ += ch
    print(mystring_)
    return mystring, mystring_







## Define step3 --> Produce Bigram Table
def gram2(mystring):
    ## Two lists
    alpha = []
    count = [1]*(len(mystring)) ## Should fuck up here
    print("\nStep2\nBigram counts chart:")
    print("P.S. Letter 'e' is been replaced already here.\n")
    ## Compute alpha and count
    for i in range(len(mystring)-1):
        ch = mystring[i]+mystring[i+1]
        if ch not in alpha and ch.isalpha():
            alpha.append(ch)
        elif ch in alpha and ch.isalpha():
            num = alpha.index(ch)
            count[num] += 1

    ## Display results
    print("Bigrams \t Freq")
    for i in range(len(alpha)):
        print(alpha[i],"\t","\t",count[i])
                   
    ## return values
    return alpha, count







## open a file and read messages into a string
msg = open(myfile,"r")
mystring = msg.read()
msg.close()

## display the encrypted message
print("Here is the encrypted message:\n")
print(mystring)
print("\n"*5)

## Step 1 --> letter counts
alpha1, count1 = gram1(mystring)

## Step 2 --> Find e and replace it
mystring, mystring_ = step2(mystring)

## Step 3 --> Bigram counts
alpha2, count2 = gram2(mystring)


## THE END ##
