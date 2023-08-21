#defined a function and gave it parameters#
def convertTo24Hour(hour, minute, period):
    #used conditional statements #
    if period == "am" and hour == 12:
        hour_24 = 0
    elif period == "pm" and hour != 12:
        hour_24 = hour + 12
    else:
        hour_24 = hour
    #used the return statement#
    return f"{hour_24:02d}{minute:02d}"

print(convertTo24Hour(9, 30, "am"))  
print(convertTo24Hour(9, 30, "pm")) 
