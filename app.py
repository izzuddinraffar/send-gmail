from flask import Flask
from flask import request
from flask import jsonify
from flask_cors import CORS, cross_origin
from flask_mail import Mail, Message
import os

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

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
@cross_origin()
def sendMail():
    name_sender = request.args.get('name','')
    email_sender = request.args.get('email','')
    subject_sender = request.args.get('subject','')
    message_sender = request.args.get('message','')
    with app.app_context():
        try:
            msg = Message(subject=email_sender +' : '+ subject_sender,
                        sender=email_sender,
                        # replace with your email for testing
                        recipients=[app.config.get("MAIL_USERNAME")],
                        body=name_sender +' : '+ message_sender)
            mail.send(msg)
            return jsonify({'status':True, 'message': 'Email send successfully'})
        except Exception as e:
            return jsonify({'status':False, 'message': str(e)})
