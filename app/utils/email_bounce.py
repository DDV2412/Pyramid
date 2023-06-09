import imaplib
from app.config import IMAP


def read_email():
    try:
        mail = imaplib.IMAP4_SSL(IMAP.get("host"))
        mail.login(IMAP.get('username'), IMAP.get('password'))

        mail.select("INBOX")

        _, message_numbers = mail.search(None, 'SUBJECT "Building Mail Campaign Service"')

        message_numbers = message_numbers[0].split()

        for num in message_numbers:
            # _, data = mail.fetch(num, "(BODY[HEADER.FIELDS (SUBJECT)])")
            # subject = data[0][1].decode("utf-8")
            # print("Email Subject:", subject)

            _, data = mail.fetch(num, "(BODY[HEADER])")

            print(data)

        for num in message_numbers:
            mail.store(num, "+FLAGS", "\\Seen")

        mail.close()
        mail.logout()
    except imaplib.IMAP4.error as e:
        print("Error:", str(e))


read_email()
