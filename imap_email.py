# Get email

import imaplib
import email

# It will work for every domain just follow instructions of those domains accordingly


############################### REQUIRED BEFORE EXECUATITION ###################################################
_EMAIL = ""
_KEY = ""
_HOST = ""
###############################################################################################################

with imaplib.IMAP4_SSL(_HOST, port=993) as mail:
    print("Connection... ", mail)

    ######################## Login #################

    print("\nLogin into email... ")
    response_code, response = mail.login(_EMAIL, _KEY)

    print("Response code... ", response_code)
    print("\nResponse... ", response)

    ################## Selecting mailbox ##############

    response_code, total_mail = mail.select("Inbox", readonly=True)



    ############### Retrive emails ####################

    response_code, emails = mail.search(None, "ALL")
    e_list = emails[0].decode('utf-8').split()
    print("\nEmail ID's... ", e_list)


    ############### Display emails ####################

    for email_id in e_list[-2:]: #if you want all email than just put [:] instead of [-2:]
        print(f"\n------------------------------ Email +++ {email_id} +++ Started---------------------------")
        response_code, mail_data = mail.fetch(email_id, "(RFC822)")
        message = email.message_from_bytes(mail_data[0][1])

        print(f"From         : {message.get('From')}")
        print(f"To           : {message.get('To')}")
        print(f"BCC          : {message.get('Bcc')}")
        print(f"Date         : {message.get('Date')}")
        print(f"Subject      : {message.get('Subject')}")

        print("Body... ")

        for part in message.walk():
            if part.get_content_type() == "text/plain":
                body_lines = part.as_string().split('\n')
                print("\n".join(body_lines[:12]))
        
        print(f"----------------------------- Ending +++ {email_id} +++ ----------------------------------------")


    ####################### Let's pack up, closing ###############################
    print("\nClosing email... ")
    mail.close()
