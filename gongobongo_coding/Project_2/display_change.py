import time

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


dis="Samaresh, Atrajit, Anshu, Soutam, Hrishav together make our family!"
print(len(dis))
i=0
while i<len(dis):
  print(dis[i],end="")
  i+=1
