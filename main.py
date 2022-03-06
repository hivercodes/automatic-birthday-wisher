import random
import pandas
import smtplib
import datetime


APPS = "apps@groundwave.se"
PW = ""

today = datetime.datetime.now()
today_tuple = (today.month, today.day)


df = pandas.read_csv("birthdays.csv")

birthday_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in df.iterrows()}

if today_tuple in birthday_dict:

    letter_number = random.randint(1,3)

    with open(f"letter_templates/letter_{letter_number}.txt") as letter:
        let = letter.read()


    #Edits the letter with the name

    final_letter = let.replace("[NAME]", birthday_dict[today_tuple]["name"])

    #sends email

    with smtplib.SMTP(host="mail.groundwave.se", port=587) as connection:
        connection.starttls()
        connection.login(user=APPS, password=PW)
        connection.sendmail(from_addr=APPS,
                            to_addrs=birthday_dict[today_tuple]["email"],
                            msg=f"Subject:Happy Birthday!\n\n{final_letter}")


