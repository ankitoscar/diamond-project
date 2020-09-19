# ---------------------------------------------------------------------------- #
#                                    IMPORTS                                   #
# ---------------------------------------------------------------------------- #


# --------------------- Imported the wtforms requirements -------------------- #
from flask_wtf import FlaskForm, RecaptchaField
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField, Form, RadioField, SelectField, ValidationError, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo
from wtforms.fields.html5 import DateField


# ---------------------------- Imported the models --------------------------- #
from main.models import User



# ------------------ Imported current user from flask login ------------------ #
from flask_login import current_user


# ---------------- Imported pycountry for Selectfield country ---------------- #
import pycountry
#This is done for the updateform

# ---------------------------------------------------------------------------- #




# ---------------------------------------------------------------------------- #
#                             FIELD CLASS CREATION                             #
# ---------------------------------------------------------------------------- #


# ---------------------- Created the Country Field Class --------------------- #
class CountrySelectField(SelectField):
    def __init__(self, *args, **kwargs):
        super(CountrySelectField, self).__init__(*args, **kwargs)
        self.choices = [(country.alpha_2, country.name) for country in pycountry.countries]





# ---------------------------------------------------------------------------- #
#                             FORM CLASSES CREATION                            #
# ---------------------------------------------------------------------------- #




# -------------------------------- SIGNIN FORM ------------------------------- #
class signinform(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')

    submit = SubmitField('Sign In')



# ---------------------------------------------------------------------------- #



# -------------------------------- SIGNUP FORM ------------------------------- #
class signupform(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])

    carat = StringField('Carat Weight')


    cut = SelectField("Cut", choices=[
        ('Fair', 'Fair'), ('Good', 'Good'), ('Very Good', 'Very Good'), ('Premium', 'Premium'), ('Ideal', 'Ideal')
    ])

    color = StringField('Color')

    clarity = SelectField("Clarity", choices=[
        ('I1', 'I1 (Worst)'), ('SI2', 'SI2'), ('SI1', 'SI1'), ('VS2', 'VS2'), ('VVS2', 'VVS2'), ('VVS1', 'VVS1'),('IF', 'IF (Best)')
    ])


    length = StringField('Length')

    email = StringField('Email',
                        validators=[DataRequired(), Email()])

    width = StringField('Width')

    depth = StringField('Depth')
    


    



    password = PasswordField('Password', validators=[DataRequired()])

    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])



    submit = SubmitField('Sign Up')

# ---------------------------------------------------------------------------- #


# ----------- SignUpForm Custom Validators for Existing User Check ----------- #
    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('The username already exists.')
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('The email already exists.')
    def validate_rollno(self, rollno):
        user = User.query.filter_by(rollno=rollno.data).first()
        if user:
            raise ValidationError('The Roll No already exists.')

#we imported current user so that:
#incase someone wants to update without some changes to their stuff
#the validators below will show error because those unchnaged values exist in our database and wont let us submit
#hence we import curnt user and apply conditions that the conditional work only if different calues are input





# ---------------------------------------------------------------------------- #



# -------------------------------- UPDATE FORM ------------------------------- #
class updateform(FlaskForm):
    
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])

    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    carat = StringField('Carat Weight')


    cut = SelectField("Cut", choices=[
        ('Fair', 'Fair'), ('Good', 'Good'), ('Very Good', 'Very Good'), ('Premium', 'Premium'), ('Ideal', 'Ideal')
    ])

    color = StringField('Color')

    clarity = SelectField("Clarity", choices=[
        ('I1', 'I1 (Worst)'), ('SI2', 'SI2'), ('SI1', 'SI1'), ('VS2', 'VS2'), ('VVS2', 'VVS2'), ('VVS1', 'VVS1'),('IF', 'IF (Best)')
    ])


    length = StringField('Length')

    

    width = StringField('Width')

    depth = StringField('Depth')
    

    submit = SubmitField('Update')

# ---------------------------------------------------------------------------- #


# ----------- UpdateForm Custom Validators for Existing User Check ----------- #
    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('The username already exists.')
    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('The email already exists.')
    def validate_rollno(self, rollno):
        if rollno.data != current_user.rollno:
            user = User.query.filter_by(rollno=rollno.data).first()
            if user:
                raise ValidationError('The Roll No already exists.')
#added  if rollno.data != current_user.rollno: these in our validator functions so that we can submit our own preexisting values



# ---------------------------------------------------------------------------- #



# ---------------- Created form instances for the Explore Page --------------- #

# ---------------------------- Country Select Form --------------------------- #
class exploreform(FlaskForm):

    question1 = CountrySelectField('Country')

    submit = SubmitField('Search')
# ---------------------------------------------------------------------------- #


# ---------------------------- Branch Select Form ---------------------------- #
class exploreform2(FlaskForm):
    question2 = StringField('Branch', validators=[Length(max=50)])

    submit2 = SubmitField('Search')
# ---------------------------------------------------------------------------- #

# ---------------------------- Branch Select Form ---------------------------- #
class exploreform3(FlaskForm):
    question3 = StringField('Username', validators=[Length(max=50)])

    submit3 = SubmitField('Show Details')
# ---------------------------------------------------------------------------- #


    





