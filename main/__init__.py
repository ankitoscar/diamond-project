# ---------------------------------------------------------------------------- #
#                                    IMPORTS                                   #


# ---------------------------- Imported Flask App ---------------------------- #
from flask import Flask

# ---------------------------- Imported SQLAlchemy --------------------------- #
from flask_sqlalchemy import SQLAlchemy

# ------------------------ Imported The Login Manager ------------------------ #
from flask_login import LoginManager

import sklearn
# ---------------------------------------------------------------------------- #
# ---------------------------------------------------------------------------- #





# ---------------------------------------------------------------------------- #
#                                  INITIATION                                  #
# ---------------------------------------------------------------------------- #





# ------------------------------- Initiated APP ------------------------------ #
app = Flask(__name__)

# --------------------- Created Secret key for CSRF Thing -------------------- #
app.config['SECRET_KEY'] = '356c2f03e9fd4d3c4287a1366c97fa34'


# ------------------------ Copy Pasted Recaptcha Keys ------------------------ #
app.config['RECAPTCHA_PUBLIC_KEY'] = '6LeliOkUAAAAALX3eKwlCvJOl0sLp7ZmjTw_3Cl5'
app.config['RECAPTCHA_PRIVATE_KEY'] = '6LeliOkUAAAAAAGneP7hgqYgwbn7L-daVuK8G_wT'


# ------- Created the database cretaion instance in relative directory ------- #
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'


# -------------------------- Created the db instance ------------------------- #
db = SQLAlchemy(app)


# ------------------ Made Use of the Login Manager Instance ------------------ #
login_manager = LoginManager(app)
login_manager.login_view = 'signin'
login_manager.login_message_category = 'info'
# ---------------------------------------------------------------------------- #




# ---------------------------------------------------------------------------- #
#                         Route Imports ALWAYS AT LAST                         #
# ---------------------------------------------------------------------------- #

from main import routes