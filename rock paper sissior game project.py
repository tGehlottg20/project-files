print("welcome to ws cube tech")
t1 = 0
t2 = 0
for i in range(1,4):
    print("round:",i)
    user1 = input("user1:rock,paper,sissior")
    user2 = input("user2:rock,paper,sissior")
    if user2 =="rock":
        if user1 == "rock":
            print("match tied")
        elif user1 == "paper":
            t1 =+1
            print("user1 win")
        elif user1 == "sissior":
            print("user1 win")
            t2 =+1
    elif user2 == "paper":
        if user1 == "paper":
            print("match tied")
        elif user1 == "sissior":
            print("user1 win")
            t1 =+1
        elif user1 == "rock":
            print("user1 win")
            t2 =+1
    elif user2 == "sissior":
        if user1 == "sissior":
            print("match tied")
        elif user1 == "rock":
            print("user1 win")
            t1+=1
        elif user1 == "paper":
            print("user1 win")
            t2+=1
print("final round")
if t1 == t2:
    print("match tied")
elif t1 > t2:
    print("match win",t1)
elif t1 < t2:
    print("match win",t2)