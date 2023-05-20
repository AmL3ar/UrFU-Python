from flask import Flask, request
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, validators
from subprocess import Popen, PIPE, TimeoutExpired
import shlex

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret_key'


class CodeForm(FlaskForm):
    code = StringField('Code', validators=[validators.DataRequired()])
    timeout = IntegerField('Timeout', validators=[validators.DataRequired(), validators.NumberRange(min=1, max=30)])


@app.route('/execute', methods=['POST'])
def execute_code():
    form = CodeForm(request.form)
    if form.validate():
        code = form.code.data
        timeout = form.timeout.data
        try:
            command = f"python -c {shlex.quote(code)}"
            process = Popen(command, shell=True, stdout=PIPE, stderr=PIPE)
            try:
                output, error = process.communicate(timeout=timeout)
                result = output.decode().strip()
                if result:
                    response = {'result': result}
                    status_code = 200
                else:
                    response = {'message': 'Execution completed.'}
                    status_code = 200
            except TimeoutExpired:
                process.kill()
                response = {'message': 'Execution timed out.'}
                status_code = 500
        except Exception as e:
            response = {'error': str(e)}
            status_code = 500
    else:
        response = {'error': form.errors}
        status_code = 400

    return response, status_code


if __name__ == '__main__':
    app.run()