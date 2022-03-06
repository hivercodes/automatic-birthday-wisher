import random
import pandas
import smtplib
import datetime


APPS = "apps@groundwave.se"
PW = ""


##################### Hard Starting Project ######################

# 1. Update the birthdays.csv with your friends & family's details. 
# HINT: Make sure one of the entries matches today's date for testing purposes. 

# 2. Check if today matches a birthday in the birthdays.csv
# HINT 1: Only the month and day matter. 
# HINT 2: You could create a dictionary from birthdays.csv that looks like this:
# birthdays_dict = {
#     (month, day): data_row
# }
#HINT 3: Then you could compare and see if today's month/day matches one of the keys in birthday_dict like this:
# if (today_month, today_day) in birthdays_dict:

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
# HINT: https://www.w3schools.com/python/ref_string_replace.asp

# 4. Send the letter generated in step 3 to that person's email address.
# HINT: Gmail(smtp.gmail.com), Yahoo(smtp.mail.yahoo.com), Hotmail(smtp.live.com), Outlook(smtp-mail.outlook.com)

todays_date = datetime.datetime.now()
todays_month = todays_date.month
todays_day = todays_date.day

#extract the month and test for todays date

with open("birthdays.csv") as bithday_file:
    df = pandas.read_csv(bithday_file)

contains_month = df[df['month'] == todays_month]

month_list = contains_month.values.tolist()

try:
    real_list = month_list[0]
except IndexError:
    real_list = []


#imports random letter


letter_number = random.randint(1,3)

with open(f"letter_templates/letter_{letter_number}.txt") as letter:
    let = letter.read()



#Edits the letter with the name

final_letter = let.replace("[NAME]", real_list[0])


#Checks if todays date match the infor in the list

if real_list[4] == todays_day and real_list[3] == todays_month:
    with smtplib.SMTP(host="mail.groundwave.se", port=587) as connection:
        connection.starttls()
        connection.login(user=APPS, password=PW)
        connection.sendmail(from_addr=APPS,
                            to_addrs=real_list[1],
                            msg=f"Subject:Quote of the week\n\n{random_quote}")


