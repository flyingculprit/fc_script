import smtplib

def send_email(sender_email, sender_password, receiver_email, subject, message):
    txt = f"Subject: {subject}\n\n{message}"

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(sender_email, sender_password)
    
    server.sendmail(sender_email, receiver_email, txt)
    #print("Email sent to " + receiver_email)

# Example usage
email = "example@gmail.com"
password = "EMAIL_PASS"
receivers_mail = "sample@gmail.com"
subject = "Put your subject"
command = "message"

send_email(email, password, receivers_mail, subject, message)

