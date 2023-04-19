from flask import Flask
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, validators, ValidationError
import subprocess

app = Flask(__name__)
app.config['WTF_CSRF_ENABLED'] = False


#task 2
def number_length(form, field):
    if len(str(field.data)) != 10:
        raise ValidationError("Dlina nomera ne ravna 10")

class NumberLength:
    def __call__(self, form, field):
        if len(str(field.data)) != 10:
            raise ValidationError("Dlina nomera ne ravna 10")



class RegistrationForm(FlaskForm):
    email = StringField(validators=[validators.InputRequired(), validators.Email()])
    phone = IntegerField(validators=[validators.InputRequired(), validators.NumberRange(min=1000000000, max=9999999999)])
    name = StringField(validators=[validators.InputRequired()])
    address = StringField(validators=[validators.InputRequired()])
    index = IntegerField(validators=[validators.InputRequired(), validators.NumberRange(min=0)])
    comment = StringField()
    #task 2    phone = IntegerField(validators=[validators.InputRequired(), number_length])
    #task 2    phone = IntegerField(validators=[validators.InputRequired(), NumberLength()])


@app.route("/registration", methods=["POST"])
def registration():
    form = RegistrationForm()

    if form.validate_on_submit():
        email, phone = form.email.data, form.phone.data

        return f"Successfully registered user {email} with phone +7{phone}"

    return f"Invalid input, {form.errors}", 400

#task 4
@app.route("/uptime", methods = ['GET'])
def uptime():
    value = subprocess.run(["uptime", "-p"], stdout=subprocess.PIPE)
    UPTIME = value.stdout.decode().strip()
    return f"Current uptime is {UPTIME}"


if __name__ == "__main__":
    app.config['WTF_CSRF_ENABLED'] = False
    app.run(debug=True)
