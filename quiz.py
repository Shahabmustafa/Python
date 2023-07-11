import time

timestamp = time.strftime('%H:%M:%S')
print(timestamp)

if(timestamp < "11:59:59"):
    print('GoodMorning')
elif(timestamp < ("19:59:59")):
    print('Good After Noon')
elif(timestamp > ("22:00:00")):
    print('Good Night')
