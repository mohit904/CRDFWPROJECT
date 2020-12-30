from crdoperation import operation
def program():
    print("\n")
    print("1.Create\n2.Read\n3.Delete")
    c=int(input("Enter the choice"))
    variable=operation()
    if (c==1):
        variable.createnewfile()
    elif (c==2):
        variable.readfromfile()
    elif (c==3):
        variable.deletefromfile()
    else:
        print("Wrong Input")
        program()
program()
