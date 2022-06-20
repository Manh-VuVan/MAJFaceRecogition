# Calculating time, which measure staff go to company early or late.
from datetime import datetime
from dateutil import parser
def caltime():
    past_now = datetime.now()
    print("Bây giờ là: ", past_now)
    hours = " 08:00:00"
    past_hours = parser.parse(str(hours)[:8])
    past_day = parser.parse(str(past_now)[:10])
    past_day = str(past_day)[:10] + hours
    past_day = parser.parse(str(past_day)[:])
    delta_time = datetime.now() - past_day
    delta_time1 = delta_time
    delta_time = str(delta_time)
    print("delta: ", delta_time)
    delta_time = parser.parse(delta_time[:])
    thresh_time = "00:00:00"
    thresh_time  = parser.parse(thresh_time[:])
    if delta_time > thresh_time:
        print("Bạn đến muộn: ", delta_time1)
    else:
        print("Chúc mừng, bạn đến sớm")

