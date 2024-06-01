import smtplib

my_email = "haarmonyhaus@gmail.com"
password = "lqqc ttaz ltws kvew"

with  smtplib.SMTP("smtp.gmail.com") as connection :
   connection.starttls()
   
   connection.login(user=my_email, password=password)
   
   connection.sendmail(from_addr=my_email,to_addrs="krishu.ganguly46@gmail.com", msg ="Subject:Hello\n\n Hi Rupam,I hope you're doing great. I wanted to express my sincere gratitude for your outstanding contributions to the project - Harmony Haus., we are gonna rock Your dedication and hard work have been truly remarkable, and we have full confidence that you will continue to achieve wonders with even greater determination and effort. Thank you once again for all that you do (python).  ")

# import datetime as dt 

# now = dt.datetime.now()
# year = now.year
# month = now.month
# day_of_week = now.weekday()
# print(day_of_week)

# day_of_birth = dt.datetime(year= 1995, month= 9, day= 12,hour=12 )
# print(day_of_birth)


connection.close()