#snake water gun Game
import random
list=[["Snake","s"],["Water","w"],["Gun","g"]]
list1 = ["s","w","g"]
computer_point=0
your_point=0
d=10
print("you have total",d,"chance for playing game")
print("what do you want to choice")
for i in range (0, 10 , +1):
    choice = random.choice(list1)
    for item, s in list:
        print("press", s, "for", item)
    a= input()
    if choice==list1[0] and a==list1[1]:
        c = f"computer choose {choice} you choose {a} "
        print(c)
        print("computer got 1 point")
        computer_point=computer_point+1
        print("computer point is",computer_point,"\n","your point is",your_point)
        d = d - 1
        print("you have",d,"chance")
    elif choice == list1[1] and a == list1[0]:
        c = f"computer choose {choice} you choose {a} "
        print(c)
        print("you got 1 point")
        your_point=your_point+1
        print("computer point is",computer_point,"\n","your point is",your_point)
        d = d - 1
        print("you have",d,"chance")
    elif choice==list1[0] and a==list1[2]:
        c = f"computer choose {choice} you choose {a} "
        print(c)
        print("you got 1 point")
        your_point = your_point + 1
        print("computer point is",computer_point,"\n","your point is",your_point)
        d = d - 1
        print("you have", d, "chance")
    elif choice==list1[2] and a==list1[0] :
        c = f"computer choose {choice} you choose {a} "
        print(c)
        print("computer got 1 point")
        computer_point = computer_point+1
        print("computer point is",computer_point,"\n","your point is",your_point)
        d = d - 1
        print("you have", d, "chance")
    elif choice==list1[1] and a==list1[2]:
        c = f"computer choose {choice} you choose {a} "
        print(c)
        print("computer got 1 point")
        computer_point=computer_point+1
        print("computer point is",computer_point,"\n","your point is",your_point)
        d = d - 1
        print("you have", d, "chance")
    elif choice==list1[2] and a==list1[1]:
        c = f"computer choose {choice} you choose {a} "
        print(c)
        print("you got 1 point")
        your_point = your_point + 1
        print("computer point is",computer_point,"\n","your point is",your_point)
        d = d - 1
        print("you have", d, "chance ")
    else:
        c = f"computer choose {choice} you also choose {a} "
        print(c)
        print("both entered same that's why you both get 0 point")
        print("computer point is",computer_point,"\n","your point is",your_point)
        d = d - 1
        print("you have", d, "chance")
if computer_point>your_point :
    print("computer won and you loss the game")
else:
    print("you won and computer loss the game")
print("your total point",your_point,"\n","computer total point",computer_point)
