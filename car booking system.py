detabase = {}
print("welcome to car booking system")
c_n_m = input("enter total number of car:")
while True:

   u = input("""
   option1: Book a car
   option2.return car
   option3 exit the program""")
   e_n = input("enter your number")


   if u =="1":

      print("""

                      1.Adher Card is Mandatory
                      2. Driving is Mandatory""")


      ys = input("yes/:no")
      num_cars = input("enter number of cars:")
      e_cname = input("enter car name:")
      r_pt = int(input("enter rent per day"))
      ent_nday = input("enter number of day:")
      i_c = input("enter proof code")
      e_name = input("enter your name:")
      en_num = input("enter your number:")
      y_s = input("conform:yes/no")



      def book_car():

         r_pt = 100
         enter_nday =4

         print("total rent:", r_pt * enter_nday, "\nbooked:")


      book_car()

      if u in detabase:
         pass

      else:
         detabase[u]={}
         detabase[u]=[num_cars,e_cname,r_pt,ent_nday,i_c,e_name,en_num]



      p = open("demo.txt","w")
      v = p.write("""welcome to car booking system
                  user name = Tarun Gehlot
                  phone number = 9694828249
                  car name = maruti
                  number of cars = 3
                  number of days = 4
                  user proof code =tg123
                  total rent = 500
                  carbooked
                  sucess""")
      p.close()
   elif u =="2":

      i_c = input("enter proof code:")
      num_cars = input("enter number of cars:")
      if i_c in detabase:
         print("thankyou")
      else:
         print("wrong input")
      if num_cars  in detabase:
         pass
      else:

         detabase = {i_c,num_cars,}

      def returncar():
         c_n_m= 5
         num_cars =3
         print(c_n_m-num_cars,"remaining car")
      returncar()


   elif u == "3":
      print("exit the car rental system. thankyou")

      break

   else:
      print("wrong input")
   print(detabase)



