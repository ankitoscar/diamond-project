

# ---------------------------------------------------------------------------- #
#                                    IMPORTS                                   #
# ---------------------------------------------------------------------------- #


# ---------------- Imported the db initialization from package --------------- #
from main import db

# --- Imported Login manager from package that we created in initalization --- #
from main import login_manager

# ---------------------------- Imported UserMixin ---------------------------- #
from flask_login import UserMixin

# ---------------------------------------------------------------------------- #
# ---------------------------------------------------------------------------- #
# we created an instance of LoginManager in our init file and we are importing that instacne in here
#User Mixin is a class that inherits different properties like get id, is authenticated, is active, etc.
# ---------------------------------------------------------------------------- #
# ---------------------------------------------------------------------------- #






# ---------------------- Placed the login manager route ---------------------- #

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# ---------------------------------------------------------------------------- #






# ---------------------------------------------------------------------------- #
#                             CLASSES FOR DATABASE                             #
# ---------------------------------------------------------------------------- #



# -------------------------------- User Class -------------------------------- #

class User(db.Model, UserMixin):

    id = db.Column(db.Integer, primary_key=True)

    username = db.Column(db.String(120), unique=True, nullable=False)

    email = db.Column(db.String(20), unique=True, nullable=False)

    carat = db.Column(db.String(120), unique=False, nullable=False)

    cut = db.Column(db.String(120), unique=False, nullable=True)

    color = db.Column(db.String(120), unique=False, nullable=False)

    clarity = db.Column(db.String(120), unique=False, nullable=False)

    width = db.Column(db.String(120), unique=False, nullable=False)

    

    length = db.Column(db.String(120), unique=False, nullable=False)

    depth = db.Column(db.String(120), unique=True, nullable=False)


    password = db.Column(db.String(100), unique=False, nullable=False)


# ---------------------------------------------------------------------------- #

    
