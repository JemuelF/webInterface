from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired
from wtforms import StringField, SubmitField, DecimalField, FloatField
from model import Model
import os

app = Flask(__name__)
bootstrap = Bootstrap(app)
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY
model = Model()

class DataForm(FlaskForm):
    # CRIM	ZN	INDUS	CHAS	NOX	RM	AGE	DIS	RAD	TAX	PTRATIO	B	LSTAT	MEDV
    CRIM = FloatField('CRIM: ', validators=[DataRequired()])
    ZN = FloatField('ZN: ', validators=[DataRequired()])
    INDUS = FloatField('INDUS: ', validators=[DataRequired()])
    CHAS = FloatField('CHAS: ')
    NOX = FloatField('NOX: ', validators=[DataRequired()])
    RM = FloatField('RM: ', validators=[DataRequired()])
    AGE = FloatField('AGE: ', validators=[DataRequired()])
    DIS = FloatField('DIS: ', validators=[DataRequired()])
    RAD = FloatField('RAD: ')
    TAX = FloatField('TAX: ', validators=[DataRequired()])
    PTRATIO = FloatField('PITRATIO: ', validators=[DataRequired()])
    B = FloatField('B: ', validators=[DataRequired()])
    LSTAT = FloatField('LSTAT: ', validators=[DataRequired()])
    submit = SubmitField('Submit')


@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = 0
    responses = [None]*13
    form = DataForm()
    if form.validate_on_submit():
        responses[0] = form.CRIM.data
        responses[1] = form.ZN.data
        responses[2] = form.INDUS.data
        responses[3] = form.CHAS.data
        responses[4] = form.NOX.data
        responses[5] = form.RM.data
        responses[6] = form.AGE.data
        responses[7] = form.DIS.data
        responses[8] = form.RAD.data
        responses[9] = form.TAX.data
        responses[10] = form.PTRATIO.data
        responses[11] = form.B.data
        responses[12] = form.LSTAT.data
        prediction = model.predict(responses)
        form.CRIM.data = 0
        form.ZN.data = 0
        form.INDUS.data = 0
        form.CHAS.data = 0
        form.NOX.data = 0
        form.RM.data = 0
        form.AGE.data = 0
        form.DIS.data = 0
        form.RAD.data = 0
        form.TAX.data = 0
        form.PTRATIO.data = 0
        form.B.data = 0
        form.LSTAT.data = 0
    return render_template('index.html', form=form, prediction=prediction)