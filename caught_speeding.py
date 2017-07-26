speed = int(input("please input your speed to check which ticket:"))
is_birthday = bool(input("please input true/false if it is your birthday:"))

if is_birthday == True:
    if speed < 31:
        print("no ticket")
    elif speed > 30 and speed < 51:
        print('small ticket')
    else:
        print('big ticket')
else:
    if speed < 36:
        print("no ticket")
    elif speed > 35 and speed < 56:
        print("small ticket")
    else:
        print("big ticket")
    
