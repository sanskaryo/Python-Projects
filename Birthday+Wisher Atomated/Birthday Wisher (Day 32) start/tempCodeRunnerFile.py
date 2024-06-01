import smtplib

my_email = "haarmonyhaus@gmail.com"
password = "lqqc ttaz ltws kvew"

connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()

connection.login(user=my_email, password=password)

connection.sendmail(from_aadr=my_email,to_addrs="sankhuzzy@gmail.com", msg ="sending email using python ")
connection.close()