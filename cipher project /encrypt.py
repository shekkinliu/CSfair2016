## Rohit Nawani
## Encrypt!!!!

## This program is designed to encrypt and display your secret message
## , then display the encrypted message with the key.

## Define myfile
myfile = "word.txt"
shift_amount = 2
    
## Main Function
def main():

    ## open a file and read messages into a string
    infile = open(myfile,"r")
    istring = infile.read()
    infile.close()

    ## Modify all alphabets to lower case
    mystring = istring.upper()

    ## outfile the encrypted message
    outfile = open("cipher_text.txt","w")

    ## Encrypt the message
    newmsg = ''
    for ch in mystring:
        if ch.isalpha():   ## Change the alphabetical values
            val = ord(ch) + shift_amount
            char = chr(val)
            newmsg += char
            outfile.write(char)
        elif ch.isalnum() or ch.isspace():   ## Keep space and digits, but reject others
            newmsg += ch
            outfile.write(ch)            
       
    ## Print the encrypted message in script just for reference
    print("Your message needs to be modified in order to proceed.")
    print("Modification includes:")
    print("1. Remove all values that are not alphabets, space or digits")
    print("2. Modify the message to all upper cases\n")
    print("Modified message as followed:\n")
    print(mystring)
    print("\n"*10)
    print("Enrypted message as followed:\n")
    print(newmsg)

    ## Close outfile 
    outfile.close()

## Invoke main function
main ()

## THE END ##
