def add_time(start, duration, date = False):
  
  
  day_of_the_week_ind = {"monday" : 0 , "tuesday" : 1, "wednesday" : 2, "thursday" : 3, "friday" : 4, "saturday" : 5, "sunday" : 6 }

  day_of_the_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

  duration_tup = duration.partition(":")
  duration_hours = int(duration_tup[0])
  duration_minutes = int(duration_tup[2])

  start_tup = start.partition(":")
  start_minutes_tup = start_tup[2].partition(" ")
  start_hours = int(start_tup[0])
  start_minutes = int(start_minutes_tup[0])
  AM_or_PM = start_minutes_tup[2]
  AM_PM_flip = {"AM": "PM", "PM": "AM"}
  

  minutes = start_minutes + duration_minutes
  if minutes >= 60 :
    start_hours+= 1
    minutes = minutes % 60
  amount_of_am_or_pm = int((start_hours + duration_hours) / 12)
  hours = (start_hours + duration_hours) % 12
  amount_of_days = int(duration_hours // 24)
  
  if minutes > 9 :
    minutes = minutes
  else:
    minutes = "0" + str(minutes)

  if amount_of_am_or_pm % 2 == 1 :
    AM_or_PM = AM_PM_flip[AM_or_PM]
  else:
    AM_or_PM = AM_or_PM

  if (AM_or_PM == "PM" and start_hours + (duration_hours % 12) >= 12 ):
    amount_of_days+= 1

  Format_time= str(hours) + ":" + str(minutes) + " " + AM_or_PM

  if (date) :
    days_of_the_week = day_of_the_week.lower()
    index = int((days_of_the_week_ind[day_of_the_week] + amount_of_days) % 7
    new_day = day_of_the_week[index]
    Format_time+= ", " + new_day

  if (amount_of_days == 1):
    return Format_time + " " + "(next day)"
  elif (amount_of_days > 1):
    return Format_time + " " + "(" + str(amount_of_days) + " days later)"
    
    
  
  

  
  

  
  
  
  
  
  
    
  
  

  
  
  
  
  
  






    