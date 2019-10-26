import getpass
from string import Template
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def main():


    print("reciever details:\n")
    er= input("email id:")
    pr=getpass.getpass()

    # set up the SMTP server
    s = smtplib.SMTP(host='smtp.gmail.com', port=587)
    s.starttls()
    print("sender details:\n")
    es=input("email id: ")
    ps=getpass.getpass()
    s.login(es,ps)


    msg = MIMEMultipart()       # create a message

    # add in the actual person name to the message template
    message = "hi this is ReemaSEbi <3 Varshini"

    # Prints out the message body for our sake
    print(message)

    # setup the parameters of the message
    msg['From']=es
    msg['To']=er
    msg['Subject']="hello"

    # add in the message body
    msg.attach(MIMEText(message, 'plain'))

    # send the message via the server set up earlier.
    s.send_message(msg)
    del msg
        
    # Terminate the SMTP session and close the connection
    s.quit()

if __name__ == '__main__':
    main()
