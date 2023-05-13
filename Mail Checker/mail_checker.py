import imaplib
import email


imap_server = "imap.gmail.com"
email_address = input("Enter Your Email address")
password = input("Enter Your password")
# print(email_address)
# print(password)

imap = imaplib.IMAP4_SSL(imap_server)
imap.login(email_address, password)

imap.select("Inbox")

_, msgnums = imap.search(None, "ALL")

for msgnum in msgnums[0].split():
    _, data = imap.fetch(msgnum, "(RFC822)")
    
    #print(data)
    message = email.message_from_bytes(data[0][1])
    
    print("Message Number: {msgnum}")
    print(f"From: {message.get('From')}")
    print(f"To: {message.get('To')}")
    print(f"BCC: {message.get('BCC')}")
    print(f"Date: {message.get('Date')}")
    print(f"Subject: {message.get('Subject')}")
    
    print("Content:")
    for part in message.walk():
        if part.get_content_type() == "text/plain":
            print(part.as_string())
            
imap.close()














