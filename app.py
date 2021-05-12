from flask import Flask, render_template, session, redirect, request
# from flask_admin import Admin
from flask_mail import Mail, Message
# import os
from config import mail_password, mail_username
app = Flask(__name__)
mail = Mail(app)
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
# app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = mail_username
app.config['MAIL_PASSWORD'] = mail_password

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/skills')
def skills():
    return render_template('skills.html')

# @app.route('/projects')
# def projects():
#     return render_template('projects.html')


@app.route('/contact' , methods=['GET', 'POST'])
def contact():
    if request.method == "POST":
        # name = request.form.get('name')
        # email = request.form.get('email')
        # phone = request.form.get('phone')
        # subject = request.form.get('subject')
        # message = request.form.get('message')
        # msg = Message(
        #     subject=f"Message from WEBsite \n\n Mail from {name}", body=f"Name: {name}\nE-Mail: {email}\nPhone: {phone}\n Subject: {subject}\n\n\n{message}", sender={email}, recipients=['iamssss@protonmail.com'])
        # mail.send_message(msg)
        # return "success"
        return render_template('contact.html',success=True)

    return render_template('contact.html')

if __name__ == "__main__":
    app.run(debug=True)
