
def changeDate(DOB):
    
    day = DOB.split('-')[0]
    mon = DOB.split('-')[1]
    year = DOB.split('-')[2]

    # Remove 0 on the days
    if day.startswith('0'):
        day = day[1:]

    # Remove 0 on the months
    if mon.startswith('0'):
        mon = mon[1:]

    # Putting position on day
    if day.endswith('11') or day.endswith('12') or day.endswith('13'):
        day += 'th'
    elif day.endswith('1'):
        day += 'st'
    elif day.endswith('2'):
        day += 'nd'
    elif day.endswith('3'):
        day += 'rd'
    else:
        day += 'th'

    mon_short_word = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

    mon_Sht = mon_short_word[int(mon)-1]
        
    
    print(f'{day}-{mon_Sht}-{year}')
    return f'{day}-{mon_Sht}-{year}'
