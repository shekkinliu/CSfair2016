## Rohit Nawani
## Decrypt!!!!
## Functions!!!!

## This program is a list of functions mainly used for decryption purposes.

##IMPORT
import operator

## Constants
print_num = 5

## Define gram1 --> letter counts
def gram1(mystring):
    ## One dictionary and two lists
    diction = {}
    alpha = []
    count = []

    ## Compute diction_alpha
    for ch in mystring:
        if ch not in diction and ch.isalpha():
            diction[ch] = 1
        elif ch in diction and ch.isalpha():
            diction[ch] += 1
    ## Compute two lists
    for key in diction:
        alpha.append(key)
        count.append(diction[key])
    ## Create new lists
    sorted_alpha = []
    sorted_count = []
    ## Sort diction by its values in reverse order
    sorted_diction = sorted(diction.items(), key=operator.itemgetter(1), reverse=True)
    for item in sorted_diction:
        sorted_alpha.append(item[0])
        sorted_count.append(item[1])

    ## Display frequency tables
    print("Letters Frequency")
    for i in range(len(sorted_alpha)):
        print(sorted_alpha[i], "\t", sorted_count[i])
        
    return diction, sorted_alpha, sorted_count

## Define gram2 --> Produce Bigram Table
def gram2(mystring):
    ## One dictionary and Two lists
    diction = {}
    alpha = []
    count = []
    print("\nStep2\nBigram counts chart:")
    print("P.S. Letter 'e' is been replaced already here.\n")
    ## Compute alpha and count
    for i in range(len(mystring)-1):
        ch = mystring[i]+mystring[i+1]
        if ch not in diction and ch.isalpha():
            diction[ch] = 1
        elif ch in diction and ch.isalpha():
            diction[ch] += 1
    ## Compute the lists
    for key in diction:
        alpha.append(key)
        count.append(diction[key])

    ## Create new lists
    sorted_alpha = []
    sorted_count = []
    ## Sort diction by its values in reverse order
    sorted_diction = sorted(diction.items(), key=operator.itemgetter(1), reverse=True)
    for item in sorted_diction:
        sorted_alpha.append(item[0])
        sorted_count.append(item[1])

    ## Display results
    print("Bigrams \t Frequency")
    for i in range(print_num):
        print(sorted_alpha[i],"\t","\t",sorted_count[i])
                   
    ## return values
    return diction, sorted_alpha, sorted_count

## Define gram3 --> Produce Trigram Table
def gram3(mystring):
    ## One dictionary and Two lists
    diction = {}
    alpha = []
    count = []
    print("\nStep3\nTrigram counts chart:")
    print("P.S. Letter 'e' is been replaced already here.\nBLA BLA BLA\n")
    ## Compute alpha and count
    for i in range(len(mystring)-2):
        ch = mystring[i]+mystring[i+1]+mystring[i+2]
        if ch not in diction and ch.isalpha():
            diction[ch] = 1
        elif ch in diction and ch.isalpha():
            diction[ch] += 1
    ## Compute the lists
    for key in diction:
        alpha.append(key)
        count.append(diction[key])

    ## Create new lists
    sorted_alpha = []
    sorted_count = []
    ## Sort diction by its values in reverse order
    sorted_diction = sorted(diction.items(), key=operator.itemgetter(1), reverse=True)
    for item in sorted_diction:
        sorted_alpha.append(item[0])
        sorted_count.append(item[1])

    ## Display results
    print("Trigrams \t Frequency")
    for i in range(print_num):
        print(sorted_alpha[i],"\t","\t",sorted_count[i])
                   
    ## return values
    return diction, sorted_alpha, sorted_count

## Define gram4 --> Produce 4-gram Table
def gram4(mystring):
    ## One dictionary and Two lists
    diction = {}
    alpha = []
    count = []
    print("\nStep4\n4-gram counts chart:")
    print("P.S. Letter 'e' is been replaced already here.\nBLA BLA BLA\n")
    ## Compute alpha and count
    for i in range(len(mystring)-3):
        ch = mystring[i]+mystring[i+1]+mystring[i+2]+mystring[i+3]
        if ch not in diction and ch.isalpha():
            diction[ch] = 1
        elif ch in diction and ch.isalpha():
            diction[ch] += 1
    ## Compute the lists
    for key in diction:
        alpha.append(key)
        count.append(diction[key])

    ## Create new lists
    sorted_alpha = []
    sorted_count = []
    ## Sort diction by its values in reverse order
    sorted_diction = sorted(diction.items(), key=operator.itemgetter(1), reverse=True)
    for item in sorted_diction:
        sorted_alpha.append(item[0])
        sorted_count.append(item[1])

    ## Display results
    print("4-grams \t Frequency")
    for i in range(print_num):
        print(sorted_alpha[i],"\t","\t",sorted_count[i])
                   
    ## return values
    return diction, sorted_alpha, sorted_count


#######################
## END OF N-GRAM COUNTS 
#######################

## Define step1 --> Find e and replace it
def find_e(mystring, alpha):
    print("\nStep1\nLetter 'e' is the most frequently used letter in Englsih and so '",alpha[0],"'is 'e'")
    print("\nWe are going to replace all '",alpha[0],"' with 'e' as followed:\n")
    mystring = mystring.replace(alpha[0],"e") ## Replace e
    mystring_ = ""
    for ch in mystring:
        if ch == "e":
            mystring_ += ch
        elif ch.isalpha():
            mystring_ += "_"
        else:
            mystring_ += ch
    print(mystring_)
    return mystring


## Define step2 --> Find t,h and replace it
def find_t_h(mystring, alpha):
    for ch in alpha[:5]:
        if ch[2] == "e":
            the = ch
            ttt = ch[0]
            hhh = ch[1]
    print("\nStep2\n'the' is one of the most frequent trigram.")
    print("Since we have already solve 'e' and if we take a look at the bigram table, 'the' is ","'",the,"'", sep="")
    print("\nWe are going to replace all '",ttt,"' with 't' and '", hhh, "' with h as followed:\n")
    mystring = mystring.replace(ttt,"t") ## Replace t
    mystring = mystring.replace(hhh,"h") ## Replace h
    mystring_ = ""
    for ch in mystring:
        if ch == "t":
            mystring_ += ch
        elif ch == "h":
            mystring_ += ch
        elif ch.isalpha():
            mystring_ += "_"
        else:
            mystring_ += ch
    print(mystring_)
    return mystring 







## THE END ##
