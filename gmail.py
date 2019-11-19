from flask import Flask
from flask_mail import Mail, Message
import os

app = Flask(__name__)

mail_settings = {
    "MAIL_SERVER": 'smtp.gmail.com',
    "MAIL_PORT": 465,
    "MAIL_USE_TLS": False,
    "MAIL_USE_SSL": True,
    "MAIL_USERNAME": os.environ['GMAIL_USERNAME'],
    "MAIL_PASSWORD": os.environ['GMAIL_SECRET']
}

app.config.update(mail_settings)
mail = Mail(app)

if __name__ == '__main__':
    app.debug = True
    app.run()


@app.route('/send-mail/')
def hello():
    with app.app_context():
        try:
            msg = Message(subject="Hello Jeppp",
                        sender=app.config.get("MAIL_USERNAME"),
                        # replace with your email for testing
                        recipients=["izzuddinraffar905@gmail.com"],
                        body="This is a test email I sent with Gmail and Python!")
            mail.send(msg)
            return 'Mail sent!'
        except Exception as e:
            return(str(e))
