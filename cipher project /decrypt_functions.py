## Rohit Nawani
## Decrypt!!!!
## Functions!!!!

## This program is a list of functions mainly used for decryption purposes.

##IMPORT
import operator

## Constants
print_num = 10

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


###################################################################################################################
#######################                     END OF N-GRAM COUNTS 
###################################################################################################################

###################################################################################################################
#######################                     FIND E 
###################################################################################################################

## Define step1 --> Find e and replace it
def find_e(mystring, alpha):
    print("\nStep1\nLetter 'e' is the most frequently used letter in Englsih and so '",alpha[0],"'is 'e'")
    print("\nWe are going to replace all '",alpha[0],"' with 'e' as followed:\n")
    mystring = mystring.replace(alpha[0],"e") ## Replace e
    mystring_ = ""
    for ch in mystring:
        if ch.isupper():
            mystring_ += "_"
        else:
            mystring_ += ch
    print(mystring_)
    return mystring

###################################################################################################################
#######################                     FIND T H 
###################################################################################################################

## Define step2 --> Find t,h and replace it
def find_t_h(mystring, alpha):
    letters = ''
    for ch in alpha:
        if ch[2] == "e":
            letters += ch[:2]
    ttt = letters[0]
    hhh = letters[1]
    the = ttt+hhh+'e'
    print("\nStep2\n'the' is one of the most frequent trigram.")
    print("Since we have already solve 'e' and if we take a look at the trigram table, 'the' is '",the,"'")
    print("\nWe are going to replace all '",ttt,"' with 't' and '", hhh, "' with h as followed:\n")
    mystring_t = mystring.replace(ttt,"t") ## Replace t
    mystring_th = mystring_t.replace(hhh,"h") ## Replace h
    mystring_ = ""
    for ch in mystring_th:
        if ch.isupper():
            mystring_ += "_"
        else:
            mystring_ += ch
    print(mystring_)
    return mystring_th

###################################################################################################################
#######################                     FIND N 
###################################################################################################################

## Define step3 --> Find n and replace it
def find_n(mystring, alpha):
    letters = ''
    for ch in alpha:
        if ch[0] == "e" and ch[2] == "t":
            letters += ch[1]
    nnn = letters[0]
    ent = "e"+nnn+"t"
    print("\nStep3\n'ent' is the most frequent trigram of 'e(something)t'.")
    print("Since we have already solved 'e' and 't' and if we take a look at the trigram table, 'ent' is '",ent,"'")
    print("\nWe are going to replace all '",nnn,"' with 'n' as followed:\n")
    mystring_n = mystring.replace(nnn,"n") ## Replace n
    mystring_ = ""
    for ch in mystring_n:
        if ch.isupper():
            mystring_ += "_"
        else:
            mystring_ += ch
    print(mystring_)
    return mystring_n

###################################################################################################################
#######################                     FIND A
###################################################################################################################

## Define step4 --> Find a and replace it
def find_a(mystring, alpha):
    letters = ''
    for ch in alpha:
        if ch[0] == "t" and ch[1] == "h" and ch[3] == "t":
            letters += ch[2]
    aaa = letters[0]
    that = "t"+"h"+aaa+"t"
    print("\nStep4\n'that' is the most frequent 4-gram of 'th(something)t'.")
    print("Since we have already solved 't' and 'h' and if we take a look at the 4-gram table, 'that' is '",that,"'")
    print("\nWe are going to replace all '",aaa,"' with 'a' as followed:\n")
    mystring_a = mystring.replace(aaa,"a") ## Replace a
    mystring_ = ""
    for ch in mystring_a:
        if ch.isupper():
            mystring_ += "_"
        else:
            mystring_ += ch
    print(mystring_)
    return mystring_a

###################################################################################################################
#######################                     FIND D
###################################################################################################################

## Define step5 --> Find d and replace it
def find_d(mystring, alpha):
    letters = ''
    for ch in alpha:
        if ch[:2] == "an":
            letters += ch[2]
    ddd = letters[0]
    and_ = "a"+"n"+ddd
    print("\nStep5\n'and' is the most frequent trigram of 'an(something)'.")
    print("Since we have already solved 'a' and 'n' and if we take a look at the 3-gram table, 'and' is '",and_,"'")
    print("\nWe are going to replace all '",ddd,"' with 'd' as followed:\n")
    mystring_d = mystring.replace(ddd,"d") ## Replace d
    mystring_ = ""
    for ch in mystring_d:
        if ch.isupper():
            mystring_ += "_"
        else:
            mystring_ += ch
    print(mystring_)
    return mystring_d

###################################################################################################################
#######################                     FIND R 
###################################################################################################################

## Define step6 --> Find r and replace it
def find_r(mystring, alpha):
    letters = ''
    for ch in alpha:
        if ch[1] == "e" and ch[0].isupper():
            letters += ch[0]
    rrr = letters[0]
    re = rrr+"e"
    print("\nStep6\n're' is the most frequent bigram of '(something)e' excluding the bigrams that we have already decrypted.")
    print("Since we have already solved 'he' and 'te', hence if we take a look at the bigrams table, 're' is '",re,"'")
    print("\nWe are going to replace all '",rrr,"' with 'r' as followed:\n")
    mystring_r = mystring.replace(rrr,"r") ## Replace r
    mystring_ = ""
    for ch in mystring_r:
        if ch.isupper():
            mystring_ += "_"
        else:
            mystring_ += ch
    print(mystring_)
    return mystring_r

###################################################################################################################
#######################                     FIND O
###################################################################################################################

## Define step7 --> Find o and replace it
def find_o(mystring, alpha):
    letters = ''
    for ch in alpha:
        if ch[1] == "r" and ch[0].isupper():
            letters += ch[0]
    ooo = letters[0]
    or_ = ooo+"r"
    print("\nStep7\n'or' is the most frequent bigram of '(something)r' excluding the bigrams that we have already decrypted.")
    print("Since we have already solved 'er' and 'ar', hence if we take a look at the bigrams table, 'or' is '",or_,"'")
    print("\nWe are going to replace all '",ooo,"' with 'o' as followed:\n")
    mystring_o = mystring.replace(ooo,"o") ## Replace o
    mystring_ = ""
    for ch in mystring_o:
        if ch.isupper():
            mystring_ += "_"
        else:
            mystring_ += ch
    print(mystring_)
    return mystring_o

###################################################################################################################
#######################                     FIND I
###################################################################################################################

## Define step8 --> Find i and replace it
def find_i(mystring, alpha):
    letters = ''
    for ch in alpha:
        if ch[1] == "n" and ch[0].isupper():
            letters += ch[0]
    iii = letters[0]
    in_ = iii+"n"
    print("\nStep8\n'or' is the most frequent bigram of '(something)n' excluding the bigrams that we have already decrypted.")
    print("Since we have already solved 'an' , 'on' and 'en', hence if we take a look at the bigrams table, 'in' is '",in_,"'")
    print("\nWe are going to replace all '",iii,"' with 'i' as followed:\n")
    mystring_i = mystring.replace(iii,"i") ## Replace i
    mystring_ = ""
    for ch in mystring_i:
        if ch.isupper():
            mystring_ += "_"
        else:
            mystring_ += ch
    print(mystring_)
    return mystring_i



## THE END ##
