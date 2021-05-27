def timeconvert(s):
    time = None
    x=s.split(":")
    hour = x[0]
    min = x[1]
    sec = x[2]
    if 'AM' in sec:
        sec = sec.replace('AM','')
        if hour == '12':
            hour = "0"+str(int(hour)-12)
    elif 'PM' in sec:
        sec = sec.replace('PM','')
        if hour == '12':
            hour = hour
        elif hour != '12':
            hour = int(hour)+12
        hour = str(hour)
    time=[hour,min,sec]
    time = ":".join(time)   
    print(time)
    # print(type(hour))
    # print(type(min))
    # print(type(sec))
timeconvert("12:45:54PM")