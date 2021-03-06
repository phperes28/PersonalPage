from flask import Flask, render_template, redirect, url_for, flash, request, abort
from flask_bootstrap import Bootstrap
from flask_ckeditor import CKEditor
from flask_mail import Mail, Message
import os
from forms import ContactForm
import smtplib




app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv("SECRET_KEY") or "8BYkEfBA6O6donzWlSihBXox7C0sKR6b"


mail = Mail(app)
ckeditor = CKEditor(app)
Bootstrap(app)



@app.route("/",  methods=["GET", "POST"])
def home():
    form = ContactForm(request.form)

    if request.method == "POST" and form.validate_on_submit():
        name = request.form.get("name")
        email = request.form.get("email")
        subject = request.form.get("subject")
        message = request.form.get("message")
        print("post")
        if form.validate() == False:
            flash('Preencha todos os campos')
            return render_template('/', form=form)
        else:

            print('Sending the Mail..')
            try:
                server = smtplib.SMTP("smtp.gmail.com", 587)
                server.starttls()
                server.login("pedro.tramit@gmail.com", os.getenv("PASSWORD"))
                mensagem = (f'Subject: {subject} \n\n{name} {email}\nEnviou a seguinte mensagem: {message}').encode("utf-8")
                server.sendmail(from_addr= "pedro.tramit@gmail.com",
                                to_addrs="pedrodev28@gmail.com",
                                msg= mensagem,

                                mail_options="SMTPUTF8"
                                )
                print("message sent")
                server.quit()
                flash("Your message was sent! :)")
            except Exception as e :
                flash('Error sending the message :(')
                print(e)

            finally:
                return redirect("/#contact")


    return render_template("index.html",  form=form)

@app.route("/automation01")
def automation():
    return render_template("portfolio-details.html")

@app.route("/automation02")
def automation02():
    return render_template("portfolio-details2.html")

@app.route("/automation03")
def automation03():
    return render_template("portfolio-details3.html")






if __name__ == "__main__":
    app.run(debug=True)
