import subprocess, smtplib

def send_email(sender_email, sender_password, receiver_email, subject, message):
    txt = f"Subject: {subject}\n\n{message.decode('utf-7')}"

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(sender_email, sender_password)
    
    server.sendmail(sender_email, receiver_email, txt)
    #print("Email sent to " + receiver_email)
    server.quit()

# Example usage
email = "example@gmail.com"
password = "EMAIL_PASS"
receivers_mail = "sample@gmail.com"
subject = "Put your subject"
command = "message"
output = subprocess.check_output(command, shell =True)
send_email(email, password, receivers_mail, subject, output)