import smtplib

def send_email(sender_email, sender_password, receiver_email, subject, message):
    txt = f"Subject: {subject}\n\n{message}"

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(sender_email, sender_password)
    
    server.sendmail(sender_email, receiver_email, txt)
    #print("Email sent to " + receiver_email)

# Example usage
email = "laverna1914@gmail.com"
password = "xjqhdjkkxnemrhcv"
receivers_mail = "laverna1914@gmail.com"
subject = "Hack"
message = "Its working"

send_email(email, password, receivers_mail, subject, message)

