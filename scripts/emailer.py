import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
from dotenv import load_dotenv

class Emailer:
    """
    A class used to send a message obtained via the Contact Me form to 
    my email address.

    """
    
    def __init__(self, name, email, number, subject, body, method):
        """
        Constructs all necessary attributes for the Emailer object.

        Parameters
        ----------
        name : str
            the user's name
        email : str
            the user's email address
        number : str, optional
            the user's phone number
        subject : str
            the subject of the message
        body : str
            the body of the message
        method : str
            the user's preferred contact method (default is email)
        """

        self.name = name
        self.email = email
        self.number = number
        self.subject = subject
        self.body = body
        self.method = method

        load_dotenv()
        self.SENDER_EMAIL = os.getenv("SENDER_EMAIL")
        self.RECEIVER_EMAIL = "baileystarrc4@gmail.com"

    def _create_email(self):
        message = MIMEMultipart("alternative")
        message["Subject"] = self.subject
        message["From"] = self.SENDER_EMAIL
        message["To"] = self.RECEIVER_EMAIL

        text = (f"Name: {self.name} \n"
                f"Contact: {self.email}, {self.number}\n"
                f"Contact Method : {self.method}\n"
                f"{self.body}")
        
        email = MIMEText(text, "plain")
        message.attach(email)

        return message.as_string()

    def send_email(self):
        """
        Sends an email with information obtained via the contact me 
        form to my email address.
        """

        email_message = self._create_email()
        with smtplib.SMTP_SSL(
            "smtp.gmail.com", 465, context=ssl.create_default_context()
        ) as email:
            email.login(self.SENDER_EMAIL, os.getenv("SENDER_KEY"))
            email.sendmail(self.SENDER_EMAIL, self.RECEIVER_EMAIL, 
                           email_message)