import smtplib
import datetime as dt
import random

now = dt.datetime.now()
day_of_week = now.weekday()  # day 0 is monday, 1 is tuesday, etc...

if day_of_week == 2:
    with open("quotes.txt") as file:
        all_quotes = file.readlines()
        random_quote = random.choice(all_quotes)

    sender = "Private Person <from@example.com>"
    receiver = "A Test User <to@example.com>"
    username = "6e9cda1e96c233"
    password = "f79a7290f26ade"

    message = f"""\
    Subject: Quote of the day!
    To: {receiver}
    From: {sender}
    
    {random_quote}"""

    with smtplib.SMTP("smtp.mailtrap.io", 587) as connection:
        connection.starttls()
        connection.login(user=username, password=password)
        connection.sendmail(from_addr=sender, to_addrs=receiver, msg=message)
