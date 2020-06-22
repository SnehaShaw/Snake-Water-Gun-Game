#health management system
#3 clients-harry , Rohan and hammad
#make 6 files for food log and exercise look
#write a function that when execute takes as input client name
#[]retrieve the data
#successfully write
list=["harry","Rohan","hammad"]
import datetime
def getdate():
    return datetime.datetime.now()
def add():
    a = int(input("press 1 for harry\npress 2 for Rohan\npress 3 for hammad"))
    if a == 1:
        b = int(input("in which field you want to add about harry\nenter 1 for food lock\n enter 2 for exercise lock"))
        if b == 1 :
            m=input("enter your suggession")
            with open("harry_food_lock","a") as f :
                f.write(str([str(getdate())]) + ":" +m+ "\n")
                print("successfully added")
        else:
            m = input("enter your suggession")
            with open("harry_exercise_lock","a") as f :
                f.write(str([str(getdate())]) + ":" + m + "\n")
                print("successfully added")
    elif a==2:
        b = int(input("in which field you want to add about Rohan\nenter 1 for food lock\n enter 2 for exercise lock"))
        if b == 1:
            m = input("enter your suggession")
            with open("rohan_food_lock", "a") as f:
                f.write(str([str(getdate())]) + ":" + m + "\n")
                print("successfully added")
        else:
            m = input("enter your suggession")
            with open("rohan_exercise_lock", "a") as f:
                f.write(str([str(getdate())]) + ":" + m + "\n")
                print("successfully added")
    else:
        b = int(input("in which field you want to add about hammad\nenter 1 for food lock\n enter 2 for exercise lock"))
        if b == 1:
            m = input("enter your suggession")
            with open("hammad_food_lock", "a") as f:
                f.write(str([str(getdate())]) + ":" + m + "\n")
                print("successfully added")
        else:
            m = input("enter your suggession")
            with open("hammad_exercise_lock", "a") as f:
                f.write(str([str(getdate())]) + ":" + m + "\n")
                print("successfully added")
def retrieve():
    a = int(input("press 1 for harry\npress 2 for Rohan\npress 3 for hammad"))
    if a == 1:
        b = int(input("what do you want about harry\nenter 1 for food lock\n enter 2 for exercise lock"))
        if b == 1:
            with open("harry_food_lock") as f:
                content=f.read()
                print(content)
        else:
            with open("harry_exercise_lock") as f:
                content=f.read()
                print(content)
    elif a==2:
        b = int(input("what do you want about rohan\nenter 1 for food lock\n enter 2 for exercise lock"))
        if b == 1:
            with open("rohan_food_lock") as f:
                content = f.read()
                print(content)
        else:
            with open("rohan_exercise_lock") as f:
                content = f.read()
                print(content)
    else:
        b = int(input("what do you want about harry\nenter 1 for food lock\n enter 2 for exercise lock"))
        if b == 1:
            with open("hammad_food_lock") as f:
                content = f.read()
                print(content)
        else:
            with open("hammad_exercise_lock") as f:
                content = f.read()
                print(content)
s=int(input("what do you want either add data or retrieve\nenter 1 for adding\n enter 2 for retrive"))
if s==1:
    add()
else:
    retrieve()
