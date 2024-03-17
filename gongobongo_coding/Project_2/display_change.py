import time
#My thoughts:


# while True:
#   t=int(time.strftime("%S"))
#   while t<=10:
#     print("Samaresh          \r",end="")
#     t=int(time.strftime("%S"))
#   while 10<t<=20:
#     print("Atrajit           \r",end="")
#     t=int(time.strftime("%S"))
#   while 20<t<=30:
#     print("Anshu             \r",end="")
#     t=int(time.strftime("%S"))
#   while 30<t<=40:
#     print("Soutam            \r",end="")
#     t=int(time.strftime("%S"))
#   while 40<t<=50:
#     print("Hrishav           \r",end="")
#     t=int(time.strftime("%S"))
#   while 50<t<=60:
#     print("Our family is here\r",end="")
#     t=int(time.strftime("%S"))

#Taken help from the internet and used time.sleep function.


# dis="Samaresh, Atrajit, Anshu, Soutam, Hrishav, Our family is here"
# i=0
# while i<len(dis):
#   print(dis[i],end="",flush=True)
#   i+=1
#   time.sleep(0.3)


#Now using time.sleep function we will recreat the above display method easily.

# dis=["Samaresh          ","Atrajit           ","Anshu             ","Soutam            ",
#      "Hrishav           ","Our family is here"]

# while True:
#   for i in dis:
#     print(i,"\r",end=" ")
#     time.sleep(1)



#Final Formatting of the display:



dis=["Samaresh          ","Atrajit           ","Anshu             ","Soutam            ",
   "Hrishav           ","Our family is here     "]

while True:
  for i in dis:
    for j in i:
      print(j,end="",flush=True)
      time.sleep(0.3)
    print("\r                  \r",end="")  