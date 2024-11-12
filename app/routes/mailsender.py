import yagmail


event_name = "Dawah Youth Camp 2024"
event_date = "24th - 29th December 2024"
location = "Taqwa School, Ifako Ijaye"
subject = "Registration Confirmation"


port = 465

# sender = "fabosedesidiqat@gmail.com"
# password = "gjkqvxnnolnjeawd"

sender = "nasfatlagosyouthzone2@gmail.com"
password = "rqzuobvgllursjjk"


def send_confirmation_email(name, email):
    msg = """\
    hello {0},
    Welcome To Nasfat Youth Wing Lagos zone 2 {1}'

    Event Details:
    - Date: {2}
    - Location: {3}

    regards
     he Committee

    Mozzie
    """.format(name, event_name, event_date, location)
    try:
        yag = yagmail.SMTP(sender, password)
        yag.send(email, subject, msg)
        print("mail successfully sent")
        
    except:
        print("email not sending")
send_confirmation_email("Bose", "fabosedesidiqat@gmail.com")
