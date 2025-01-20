import time
timestamp=time.strftime('%H.%M.%S')
print(timestamp)
hrs=time.strftime('%H')
print(hrs)
min=time.strftime('%M')
print(min)
sec=time.strftime('%S')
print(sec)
hour=int(time.strftime('%H')) #strftime used for time function
name=input("Enter your name:")
if(4<=hour<12):
  print("Goood morning",name)
elif(12<=hour<16):
  print("Good afternoon",name)
elif(16<=hour<20):
  print("Good evening",name)
else:
  print("Good night",name)