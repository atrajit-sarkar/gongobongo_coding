from gongobongo_coding.calculator import calculator



def cal_body():
   x=float(input("x= "))
   sym=input(" ")
   y=float(input("y="))
   calculator(x,sym,y)

   while sym not in ["+","-","*","/","%"]:
     print("Invalid symbol. Please try again.")
     x=float(input("x= "))
     sym=input(" ")
     y=float(input("y= "))
     calculator(x,sym,y)
   next_cal=input("Do you want to continue? (yes/no): ")
   while next_cal == "yes":
     x=float(input("x= "))
     sym=input(" ")
     y=float(input("y= "))
     calculator(x,sym,y)
     while sym not in ["+","-","*","/","%"]:
       print("Invalid symbol. Please try again.")
       x=float(input("x="))
       sym=input("")
       y=float(input("y= "))
       calculator(x,sym,y)
     next_cal=input("Do you want to continue? (yes/no): ")
   if next_cal=="no":
     print("Thank you for using the calculator!")
