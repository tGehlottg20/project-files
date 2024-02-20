print("welcome to Ws cube tech-E School")
database = {}
while True:
     op = input("""
 1.school_admission
2.student's fee
3.principal_Access
4.exit: """)
     if op=="1":
         print("welcome to student Admission")
         st_name = input("enter your name: ")
         f_name = input("enter your Father name: ")
         M_name = input("enter your Mother name: ")
         phone = int(input("enter your number: "))
         card_no = input("enter card no: ")
         s_class = input("enter class: ")
         if s_class in database :
             if card_no in database[s_class]:
                 print("Ar")
             else:
                 database[s_class][card_no]=[st_name,f_name,M_name,phone,0]
         else:
             database[s_class]={}
             database[s_class][card_no]=[st_name,f_name,M_name,phone,0]

     elif op =="2":
         s_class = input("enter your class: ")
         card_no = input("enter your card no: ")
         if(s_class in database) and (card_no in database[s_class]):
             st_fee= int(input("enter your fee: "))
             if st_fee>0:
                 database[s_class][card_no][-1]+=st_fee
             else:
                 print("wrong input")
         else:
             print("wrong input")

     elif op == "3":
        print("principal Accesses")
        pc = input("enter principal code")
        Esnumber = input("enter student Card no:")
        cod = "123"
        if pc in cod:
            print("code is match")
            database[s_class][card_no] = [st_name, f_name, M_name, phone,st_fee ]



        else:
            print("invalid code")
            database ={}




     elif op == "4":
         break

     else:
         print("wrong input: ")

     print(database)


