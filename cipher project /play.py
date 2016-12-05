## Rohit Nawani
## Decrypt!!!!

## This program is designed to decrypt the secret message.

msg = ""
openfile = "dic/txt/a.txt"

## open file
infile = open(openfile, "r")
myfile = infile.read()
infile.close()

## Process
alist = myfile.spilt("\n")
print(len(alist))


## THE END ##
