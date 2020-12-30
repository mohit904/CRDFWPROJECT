import os

class operation:
    def deletefromfile(self):
        keyvalue=input("Enter the key")
        nameoffile=keyvalue
        try:
            os.remove(nameoffile)
            print("Deleted")       
        except Exception as e:
            print("Key doesn't exist")
    def getvalue(self,d): 
        dictionary = dict() 
        allpairs = d.strip('{}').split(', ')
        for i in allpairs:
            induvidual_pair = i.split(': ')
            dictionary[induvidual_pair[0].strip('\'\'\"\"')] = induvidual_pair[1].strip('\'\'\"\"')
        return dictionary
    def readfromfile(self):
        found=False
        keyinput=input("Enter the key")
        filename=keyinput
        try:
            with open(filename,'rt') as newfile:
                inputline = newfile.read().split('\n')
                for i in inputline:
                    if (i != ''):
                        d=getvalue(i)
                        for keys, value in d.items():
                            if keyinput==keys:
                                print("The Value is mentioned below")
                                print(d[keys])
                                found=True; 
                                break
                if(found==False):
                    print("Key is invalid")
        except:
            print("Key not found")
    def createnewfile(self):
        dictionary={}
        keyinput=input("Enter the key")
        if(len(keyinput)>32): #Length Limit
            print("Memory Error ! We will do again")
            createnewfile()
        elif(keyinput.isalpha())==False:
            print("Key must contain only String")
            createnewfile()
        valueinput=input("Enter the value for key")
        if(len(dictionary)<(10742661120) and len(valueinput)>(16777216)): #10742661120 is 1GB in bits and 16777216 is 16 KB in bits
            print("Oops ! Memory is full")
            createnewfile()
        else:
            nameoffile=keyinput
            try:
                with open(nameoffile, 'x') as newfile:
                    print("File Created")
            except:
                print("Key Exists")
            try:
                dictionary[keyinput]=valueinput
                with open(nameoffile,'wt') as newfile:
                    newfile.write(str(dictionary))
                    print("The Data has been Stored")
            except:
                print("Unable to store data")
    
