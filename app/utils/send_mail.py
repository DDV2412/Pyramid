import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from app.config import SMTP_SERVERS


def send_email(mail: dict):
    for recipient in mail.pop("recipients", ""):
        for contact in recipient.contacts:
            msg = MIMEMultipart()
            msg['From'] = f"{mail.get('from_name', '')} <{mail.get('from_mail', '')}>"
            msg['To'] = f'{contact.firstname} {contact.lastname} <{contact.email}>'
            msg['Subject'] = mail.get('subject', '')
            msg['X-MC-Preview'] = mail.get('preview_line', '')

            # Add the message body
            body = MIMEText(mail.get("design", ""), 'html')
            msg.attach(body)

            for server in SMTP_SERVERS:
                try:
                    smtp = smtplib.SMTP_SSL(server['host'], server['port'])
                    smtp.login(server['username'], server['password'])

                    # Send the email with return_path set to the sender's email
                    return_path = server['username']
                    smtp.sendmail(mail.get("from_mail", ""), contact.email, msg.as_string(),
                                  rcpt_options=f"SMTPUTF8 RETURN-PATH={return_path}")

                    smtp.quit()

                    print(f'Email sent successfully to {contact.email}.')
                    break  # Exit the loop if email is sent successfully
                except smtplib.SMTPException as e:
                    print(f'An error occurred while sending the email to {contact.email} via {server["host"]}: {str(e)}')
