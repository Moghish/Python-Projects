print("----------------------------------------------")
print("*****WELCOME TO STUDENT MANAGEMENT SYSTEM*****")
print("----------------------------------------------")



list=["Ram","Sita","Laksman","Amit"]

def view_name():
    for i in range(len(list)):
        print(list[i])

def add_name():
    a=input("Enter the New Student name : ")
    list.append(a)
    print("Student name added")

def remove_name():
    a=input("Search Student name : ")
    if a in list:
        list.remove(a)
        print("Removed Student name")
    else:
        print("Student not found")

def search_name():
    a=input("Search Student name : ")
    if a in list:
        print("Student found")
    else:
        print("Student not found")
        
while(True):
    print("Please choose any one opption")
    print()
    print("1. To view student list")
    print("2. To add new list")
    print("3. To remove the data")
    print("4. To search data")
    print("5. Exit")
    print()
    
    choice=int(input("Enter your choice(1/2/3/4/5):"))

    if choice==1:
        view_name()
        
    elif choice==2:
        add_name()

    elif choice==3:
        remove_name()

    elif choice==4:
        search_name()

    elif choice==5:
        exit()

    else:
        print("Wrong Entry")
    print()
    c=input("Do you want to continue(y/n):")
    if(c=='y'):
        continue
    elif(c=='n'):
        break



