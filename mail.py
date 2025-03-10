import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

class MailSender:
    def __init__(self, sender_email = "mustafa.mgundogdu@gmail.com", sender_password = "pzcg mfls lwlc txaq", smtp_server = "smtp.gmail.com", smtp_port = 587):
        self.sender_email = sender_email
        self.sender_password = sender_password
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port

    def send_email(self, recipient_email, subject, message):
        try:
            msg = MIMEMultipart()
            msg['From'] = self.sender_email
            msg['To'] = recipient_email
            msg['Subject'] = subject
            msg.attach(MIMEText(message, 'plain'))

            server = smtplib.SMTP(self.smtp_server, self.smtp_port)
            server.starttls()
            server.login(self.sender_email, self.sender_password)
            server.sendmail(self.sender_email, recipient_email, msg.as_string())
            server.quit()
            return True
        except Exception as e:
            print(f"An error occurred: {e}")
            return False
    def create_ics_file(self, summary, start, end, description, location, ics_file_name = "appointment.ics"):
       # Create the ics file
        ics_content = f"""BEGIN:VCALENDAR
        VERSION:2.0
        CALSCALE:GREGORIAN
        METHOD:REQUEST
        BEGIN:VEVENT
        DTSTART:{start}
        DTEND:{end}
        SUMMARY:{summary}
        DESCRIPTION:{description}
        LOCATION:{location}
        STATUS:CONFIRMED
        SEQUENCE:0
        BEGIN:VALARM
        TRIGGER:-PT10M
        DESCRIPTION:Reminder
        ACTION:DISPLAY
        END:VALARM
        END:VEVENT
        END:VCALENDAR
        """
        # Save the ics file
        try:
            with open(ics_file_name, "w") as ics_file:
                ics_file.write(ics_content)
            return True
        except Exception as e:
            print(f"An error occurred: {e}")
            return False
    
    def send_appointment_email(self, recipient_email, subject, message, ics_file_path = "appointment.ics"):
        try:
            msg = MIMEMultipart()
            msg['From'] = self.sender_email
            msg['To'] = recipient_email
            msg['Subject'] = subject
            msg.attach(MIMEText(message, 'plain'))

            with open(ics_file_path, "rb") as attachment:
                part = MIMEBase("application", "calendar",method="REQUEST", filename=ics_file_path)
                part.set_payload(attachment.read())
                encoders.encode_base64(part)
                part.add_header("Content-Disposition", f"attachment; filename= {ics_file_path}")
                part.add_header("Content-Type", "text/calendar", method="REQUEST", name=ics_file_path)
                msg.attach(part)

                server = smtplib.SMTP(self.smtp_server, self.smtp_port)
                server.starttls()
                server.login(self.sender_email, self.sender_password)
                server.sendmail(self.sender_email, recipient_email, msg.as_string())
                server.quit()
                return True

        except Exception as e:
            print(f"An error occurred: {e}")
            return False

# Mail Send Function
def mail_send():
    sender_email = "mustafa.mgundogdu@gmail.com"
    sender_password = "pzcg mfls lwlc txaq"
    recipient_email = "mustafagundogdu.nl@gmail.com"
    subject = "Test Email"
    message = "This is a test email. \n if you read this mail, send mail is successful."
    mail_sender = MailSender(sender_email, sender_password)
    if mail_sender.send_email(recipient_email, subject, message):
        print("Email sent successfully.")
    else:
        print("Failed to send email.")

def appointment_mail_send():
    sender_email = "mustafa.mgundogdu@gmail.com"
    sender_password = "pzcg mfls lwlc txaq"
    recipient_email = "mustafagundogdu.nl@gmail.com"

    subject = "Appointment Event Invitation"
    summary = "Etkinlik"
    start = "20250422T180000"
    end = "20250422T190000"
    description = "This is a test appointment."
    location = "Google Meet"

    mail_content = f"""Hello,

    We invite you to "{summary}" event.

    Start: {start}
    Finish: {end}
    Location: {location}

    Please accept the invitation and add it to your calendar.

    Kind regards,
    {sender_email}
    """
    mail_sender = MailSender(sender_email, sender_password)
    mail_sender.create_ics_file(summary, start, end, description, location)
    mail_sender.send_appointment_email(recipient_email, subject, mail_content, ics_file_path="appointment.ics")

if __name__ == "__main__":
    #mail_send()
    appointment_mail_send()
    input("Press Enter to exit...")