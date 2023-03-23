from flask import Flask
from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, validators


app = Flask(__name__)

#task1
class RegistrationForm(FlaskForm):
    email = StringField(validators=[validators.InputRequired(), validators.Email()])
    phone = IntegerField(validators=[validators.InputRequired(),validators.NumberRange(min=1000000000, max=9999999999)])
    name = StringField(validators=[validators.InputRequired()])
    address = StringField(validators=[validators.InputRequired()])
    index = IntegerField(validators=[validators.InputRequired()])
    comment = StringField(validators=[validators.InputRequired()])

@app.route('/registration', methods=["POST"])
def registration():
    form = RegistrationForm()

    if form.validate_on_submit():
        email, phone = form.email.data, form.phone.data

        return f"Successfully registered user {email} with phone +7{phone}"

    return f"Invalid input, {form.errors}", 400


#task3




if __name__=="__main__":
    app.config["WTF_CSRF_ENABLED"] = False
    app.run(debug = True)