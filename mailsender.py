import random
import yagmail
import math
# import os
#from dotenv import load_dotenv

# load_dotenv()

randit = str(math.floor(random.random() * 7652196 + 1))
value = int(randit[0:5])
otp = value

port = 465

# sender = "fabosedesidiqat@gmail.com"
# password = "gjkqvxnnolnjeawd"

sender = "nasfatlagosyouthzone2@gmail.com"
password = "rqzuobvgllursjjk"


# this function send otp to confirm user
def Send_token(email,name):
    msg = """\
    hello {0},
    To verify/reset your cryptpay account, please use the following OTP:

                        {1}

    regards

    Mozzie
    """.format(name,otp)
    try:
        yag = yagmail.SMTP(sender, password)
        yag.send(email, 'Email Verification', msg)
        print("mail successfully sent")
        
    except:
        print("email not sending")

Send_token("gen2soul11@gmail.com", "simeon")