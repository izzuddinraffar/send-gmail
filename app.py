from flask import Flask
from flask import request
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


@app.route('/send-mail/', methods=['POST'])
def hello():
    name_recipient = request.args.get('name','')
    email_recipient = request.args.get('email','')
    subject_recipient = request.args.get('subject','')
    message_recipient = request.args.get('message','')
    with app.app_context():
        try:
            msg = Message(subject=name_recipient +' : '+ subject_recipient,
                        sender=app.config.get("MAIL_USERNAME"),
                        # replace with your email for testing
                        recipients=[email_recipient],
                        body=message_recipient)
            mail.send(msg)
            return 'Mail sent!'
        except Exception as e:
            return(str(e))
