def convert_num_into_time(num):
    hour = num//60
    hour1 = num%60
    minute = hour1%60

    print(hour, "hours", minute, "minutes")
num = int(input("Enter the number: "))

convert_num_into_time(num) 
