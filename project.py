import os
#Function to delete from file
def deletefromfile():
        keyvalue=input("Enter the key")
        nameoffile=keyvalue
        try:
            os.remove(nameoffile)
            print("Deleted")       
        except Exception as e:
            print("Key doesn't exist")
        program()

#Function to split the data from file and retrive
def getvalue(d): 
    dictionary = dict() 
    allpairs = d.strip('{}').split(', ')
    for i in allpairs:
        induvidual_pair = i.split(': ')
        dictionary[induvidual_pair[0].strip('\'\'\"\"')] = induvidual_pair[1].strip('\'\'\"\"')
    return dictionary

#Function to read from file
def readfromfile():
    found=False
    keyinput=input("Enter the key")
    filename=keyinput
    try:
        newfile = open(filename, 'rt')
        inputline = newfile.read().split('\n')
        for i in inputline:
            if (i != ''):
                d=getvalue(i)
                for keys, value in d.items():
                    if keyinput==keys:
                        print("The Value is mentioned below")
                        print(d[keys])
                        flag=True; 
                        break
        if(flag==False):
            print("Key is invalid")
        newfile.close()
        program()
    except:
        print("Key not found")
        program()
#Functiom to create a new file
def createnewfile():
    dictionary={}
    keyinput=input("Enter the key with max 32 char and datatype as string ")
    if(len(keyinput)>32): #Length Limit
        print("Memory Error ! We will do again")
        createnewfile()
    elif(keyinput.isalpha())==False:
        print("Key must contain only String")
        createnewfile()
    valueinput=input("Enter the value for key with max 16 chars")
    if(len(dictionary)<(10742661120) and len(valueinput)>(16777216)): #10742661120 is 1GB in bits and 16777216 is 32 KB in bits
        print("Oops ! Memory is full")
        createnewfile()
    else:
        nameoffile=keyinput
        try:
            newfile= open(nameoffile, 'x')
            newfile.close()
        except:
            print("Key Exists")
            program()
        try:
            dictionary[keyinput]=valueinput
            newfile=open(nameoffile,'wt')
            newfile.write(str(dictionary))
            newfile.close()
            print("The Data has been Stored")
            program()
        except:
            print("Unable to store data")
            program()

#The Main program
def program():
    print("\n")
    print("1.Create\n2.Read\n3.Delete")
    c=int(input("Enter the choice"))
    if (c==1):
        createnewfile()
    elif (c==2):
        readfromfile()
    elif (c==3):
        deletefromfile()
    else:
        print("Wrong Input")
        program()
program()
