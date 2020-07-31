import time

houers = int(time.strftime('%H'))
minutes = int(time.strftime('%M'))
seconds = int(time.strftime('%S'))

def finishing_time(timertime):
#   houers = int(time.strftime('%H'))
#   minutes = int(time.strftime('%M'))
#   seconds = int(time.strftime('%S'))
    x = timertime + (houers * 3600) + (minutes * 60) + seconds
    m, s = divmod(x, 60)
    h, m = divmod(m, 60)
    finishing_time = str(h).zfill(2) + ":" + str(m).zfill(2) 
    return finishing_time

#print(finishing_time(9000))
# + ":" + str(s).zfill(2)

