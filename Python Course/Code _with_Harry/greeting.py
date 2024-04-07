import time
name=input("Enter your name:").title()
current_time=time.strftime('%H:%M:%S')
print("Current time is:", current_time)
hour=int(time.strftime('%H'))
if hour<12 and hour>4:
 print("Good Morning, Mr./Mrs.",name)
elif hour>=12 and hour<16:
 print("Good Afternoon, Mr./Mrs",name)
elif hour>=16 and hour<20:
 print("Good Evening, Mr./Mrs",name)
else:
 print("Good Night, Mr./Mrs",name) 

