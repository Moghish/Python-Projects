print("-------------------------------------------")
print("*****WELCOME TO BANK MANAGEMENT SYSTEM*****")
print("-------------------------------------------")

data={}
list1=["Name","Address","Mob","GovtID","Account_Type","amount"]

def newacc():
    acc_num=input("enter the account number:")

    for item in list1:
        list2.append(input("Enter %s: "%item))

    data[acc_num] = dict(zip(list1,list2))
    print("Account Open")
    print("-------------------------------")
    return

def option():
    ch=int(input("1. Check balance \n2. withdrawal \n3. deposit \nenter choice:"))

    if(ch==1):
        print("available balance:",data[acc_num]["amount"])
        print("------------------------------------------")
    elif(ch==2):
        amount=int(input("enter withdrawal amount:"))
        new_amt=int(data[acc_num]["amount"])-amount
        data[acc_num] ["Amount"]= new_amt
        print("withdrawal successful")
        print("available balance:",data[acc_num]["amount"])
    elif(ch==3):
        amount=int(input("enter deposit amount"))
        new_amt=int(data[acc_num]["amount"])+amount
        data[acc_num] ["Amount"]= new_amt
        print("deposit successful")
        print("available balance:",data[acc_num]["amount"])
    
while(True):
    list2=[]
    ch=int(input("1.New customer \n2. Existing Customer \n3.exit \nenter choice:"))
    if(ch==1):
        newacc()
    if(ch==2):
        acc_num=input("enter your account number:")
        if acc_num in data:
            print("record found")
            option()
        else:
            print("record not found")
            
    if(ch==3):
        break
    
