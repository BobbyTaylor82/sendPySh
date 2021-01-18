import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import os.path

### Note I generated a fake email for this script ###
email = 'bltxr9999@gmail.com' # Your email
password = 'Bxt.109$$$$' # Your email account password
#userEmail = input('Enter in the receivers email? ')
userEmail = "bobby.taylor@broadcom.com"
send_to_email = "bltxr9@gmail.com" # Who you are sending the message to



messageSP = "\n "
message0 ='**************************** Jenkins Data *************************************'
message1 ='\nDescription: This application allows the user to send a report to user(s) email(s).'



messageC = message0 + messageSP + message1 


#------------------------------------------------------------------------------------
file_location = 'send.txt'
#------------------------------------------------------------------------------------


msg = MIMEMultipart()
msg['From'] = email
msg['To'] = send_to_email
msg['Subject'] = "Jenkins INFO"

msg.attach(MIMEText(messageC, 'plain'))

#------------------------------------------------------------------------------------
# Setup the attachment
filename = os.path.basename(file_location)
attachment = open(file_location, "rb")
part = MIMEBase('application', 'octet-stream')
part.set_payload(attachment.read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename= %s" % filename)

# Attach the attachment to the MIMEMultipart object
msg.attach(part)
#------------------------------------------------------------------------------------



server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(email, password)
text = msg.as_string()
server.sendmail(email, send_to_email, text)
server.quit()