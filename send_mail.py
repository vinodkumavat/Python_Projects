import smtplib


def send_mail(to, message):
    # 1st always enable the less secure app for google and turn off 2 step verification
    
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    
    #self mail and password
    _from = "mail@gmail.com"
    password = "password"
    
    server.login(_from, password)
    # sendmail(from, to, message)
    server.sendmail(_from, to, message)
    server.quit()
    
send_mail("toWhomesend@gmail.com", "Message to send")
