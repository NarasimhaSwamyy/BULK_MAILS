import smtplib
import csv
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

smtpServer = "smtp.gmail.com"
smtpPort = 587
emailAddress = "sender@gmail.com"
emailPassword = "senderPassword"

def sendEmail(toAddress, subject, body):
    try:
        server = smtplib.SMTP(smtpServer, smtpPort)
        server.starttls()
        server.login(emailAddress, emailPassword)

        msg = MIMEMultipart()
        msg['From'] = emailAddress
        msg['To'] = toAddress
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        server.sendmail(emailAddress, toAddress, msg.as_string())
        print(f"Email sent to {toAddress}")
        server.quit()

    except Exception as e:
        print(f"Failed to send email to {toAddress}: {str(e)}")

def sendEmailsFromCsv(csvFile):
    try:
        with open(csvFile, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                toAddress = row['email']
                subject = row['subject']
                body = row['message']
                sendEmail(toAddress, subject, body)
    except Exception as e:
        print(f"Error reading CSV file: {str(e)}")

csvFilePath = 'email_data.csv'
sendEmailsFromCsv(csvFilePath)
