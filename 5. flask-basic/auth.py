from flask import Flask, Blueprint, render_template

# Declare a Flask App
app = Flask(__name__)


# Created a Blueprint
auth_controller = Blueprint(
    "auth_controller",
    __name__,
    url_prefix="/",
    template_folder="social-network-theme/template",
    static_folder="social-network-theme/assets",
    static_url_path="assets"
)

@auth_controller.route('/', methods=['GET'])

# actions of controler
@auth_controller.route('/login', methods=['GET'])
def login():
    return render_template("veiw/login.html")


@auth_controller.route('/registration', methods=['GET'])
def registration():
    return render_template("veiw/registration.html")


@auth_controller.route('/forget-password', methods=['GET'])
def dashboard():
    return render_template("veiw/forget-password.html")


@auth_controller.route('/set-password', methods=['GET'])
def dashboard():
    return render_template("veiw/set-password.html")


@auth_controller.route('/otp', methods=['GET'])
def dashboard():
    return render_template("veiw/otp.html")


# Register the Blueprint
app.register_blueprint(auth_controller)


if __name__ == '__main__':
    app.run(debug=True)