# Calculating time, which measure staff go to company early or late.
from datetime import datetime
from dateutil import parser
name_before, day_before = "", ""
staff = []
first_handle = False
def caltime_arrive(name):
    global name_before, staff, day_before, first_handle, fields, filename, csvwriter
    arr_data = []
    arr_data.append(name)
    past_now = datetime.now()  # get time now
    print("Now: ", past_now)
    hours = " 08:00:00"  # hour setup
    # past_hours = parser.parse(str(hours)[:8])
    past_day = parser.parse(str(past_now)[:10])   # get day:month:year
    day_now = str(past_now)[:10] # convert time to string
    arr_data.append(day_now)
    past_day = str(past_day)[:10] + hours # day and hour work
    past_day = parser.parse(str(past_day)[:])  # convert time from string to time
    delta_time = datetime.now() - past_day  # delta time
    time_arrive = delta_time
    delta_time = str(delta_time)
    thresh_time = "00:00:00"
    thresh_time  = parser.parse(thresh_time[:])
    try:
        delta_time = parser.parse(delta_time[:])
    except:
        delta_time = delta_time[-15:]
        delta_time  = parser.parse(delta_time[:])
        delta_time = thresh_time - delta_time
        delta_time = str(delta_time)
        delta_time = delta_time[-15:]
    
    try:
        if delta_time > thresh_time:
            state_arrive = "Muon"
            print("Muon: ", time_arrive)
        else:
            state_arrive = "Som"
            print("Som")
    except:
        state_arrive = "Som"
        print("Som: ", delta_time)
        time_arrive = delta_time
    arr_data.append(state_arrive)
    arr_data.append(str(time_arrive))
    for i in range(0, len(staff)):
        print("name: ", name, staff[i][0], day_before, day_now)
        if name != staff[i][0] and day_before == day_now:
            for i in range(0, len(staff)):
                if name == staff[i][0]:
                    break
                if i == len(staff) - 1:
                    staff.append(arr_data)
        if name == staff[i][0] and parser.parse(str(datetime.now() - parser.parse((staff[i][3])[:]))[:]) > parser.parse("00:00:01"[:]):
            leave = caltime_leave()
            if len(staff[i]) <=5:
                staff[i].append(str(leave[0]))
                staff[i].append(str(leave[1]))
                from source.writecsvlog import update_file
                update_file(staff[i])
            break
        else:
            print("End Staff")
    name_before = name
    day_before = day_now
    if first_handle == False:
        staff.append(arr_data)
        first_handle = True
    print("staff: ", staff)
    return staff     # day, delta_time, state

def caltime_leave():
    global name_before, staff, day_before
    leave = []
    past_now = datetime.now()  # get time now
    print("Now: ", past_now)
    hours = " 17:00:00"  # hour setup
    # past_hours = parser.parse(str(hours)[:8])
    past_day = parser.parse(str(past_now)[:10])   # get day:month:year
    day_now = str(past_now)[:10] # convert time to string
    past_day = str(past_day)[:10] + hours # day and hour work
    past_day = parser.parse(str(past_day)[:])  # convert time from string to time
    delta_time = datetime.now() - past_day  # delta time
    time_leave = delta_time
    delta_time = str(delta_time)
    thresh_time = "00:00:00"
    thresh_time  = parser.parse(thresh_time[:])
    try:
        delta_time = parser.parse(delta_time[:])
    except:
        delta_time = delta_time[-15:]
        delta_time  = parser.parse(delta_time[:])
        delta_time = thresh_time - delta_time
        delta_time = str(delta_time)
        delta_time = delta_time[-15:]
    
    try:
        if delta_time > thresh_time:
            state_leave = "Som"
            print("Early: ", time_leave)
        else:
            state_leave = "Muon"
            print("late")
    except:
        state_leave = "Muon"
        print("Late: ", delta_time)
        time_leave = delta_time
    leave.append(state_leave)
    leave.append(time_leave)
    return leave      # day, delta_time, state