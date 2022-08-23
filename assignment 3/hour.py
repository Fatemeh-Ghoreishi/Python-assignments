x = int(input('Select the desired option: \n1.hours to seconds \n2.seconds to hours\n'))

if x == 1:
    while True:
        hour = int(input('Enter your hours: '))
        minutes = int(input('Enter your minutes: '))
        second = int(input('Enter your seconds: '))
        if (hour < 24) and (minutes < 60) and (second < 60):
            hour = hour * 3600
            minutes = minutes * 60
            sum = hour + minutes + second
            print(sum, "seconds")
            break           
        else:
            print('Please enter a real number! (0 <= hour < 24),(0 <= minutes < 60),(0 <= second , 60)')
            continue

elif x == 2:
    while True:
        second = int(input('Enter your seconds: '))
        if second <= 86400 :
            minutes = int(second / 60)
            if minutes >= 60:
                hour = int(minutes / 60)
            new_minutes = int(minutes % 60)
            new_second = int(second % 60)
            print('hours:' ,hour, 'minutes:' ,new_minutes, 'seconds:' ,new_second)
            break
        else:
            print('Please enter a number less than 86400!')
            continue