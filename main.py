from flask import Flask, request, redirect
from flask_cors import CORS
import smtplib
from email.message import EmailMessage

app = Flask(__name__)
app.secret_key = 'iamfuckingcreazy'
CORS(app)


message = EmailMessage()


@app.route('/contactform/template1/<user>', methods=['POST'])
def contact(user):
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        if name == "" or email == "":
            return redirect(request.referrer)
        else:
            # # print(name, email, subject, message)
            # cursor.execute("INSERT INTO contactform (name,email,subject,message) VALUES (%s,%s,%s,%s)",
            #                (name, email, subject, message))
            # mydb.commit()
            # print("Not executed")
            # return redirect(request.referrer)
            name = request.form['name']
            email = request.form['email']
            subject = request.form['subject']
            msg = request.form['message']

            message["Subject"] = "Contact form submission on " + request.referrer
            message["From"] = "youremailaddress"
            message["To"] = user

            data = "<div class='container'> <div class='row'> <div class='col'> <p><b>Name </b>:" + name + " </p> </div> <div class='col'> <p><b>Email</b> : " + email + " </p> </div> <div class='col'> <p><b>Subject</b> : " + request.form['subject'] + "</p> </div> <div class='col'> <p><b>Message</b> : " + request.form['message']+"</p> </div> </div> </div> </div>"

            message.add_alternative(data, subtype='html')

            try:
                with smtplib.SMTP_SSL("hostaddress", 465) as smtp:
                    smtp.login("youremailaddress", "password")
                    smtp.send_message(message)
                    smtp.quit()
            except Exception as e:
                print(e)
            else:
                print("message sent")

        return redirect(request.referrer)

    else:
        return False


if '__main__' == __name__:
    app.run(debug=True)
