def add_time(start, duration):
  
  
  day_of_the_week_ind = {"monday" : 0 , "tuesday" : 1, "wednesday" : 2, "thursday" : 3, "friday" : 4, "saturday" : 5, "sunday" : 6 }

  day_of_the_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

  duration_tup = duration.partition(":")
  duration_hours = int(duration_tup[0])
  duration_minutes = int(duration_tup[2])

  start_tup = start.partition(":")
  start_minutes_tup = start_tup[2].partition(" ")
  start_hours = int(start_tup[0])
  start_minutes = int(start_tup[2])
  
  
  






    