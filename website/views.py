from flask import Blueprint, render_template
from flask_login import login_required, current_user
from .models import Services

views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    return render_template("home.html", user=current_user)


@views.route('/services', methods=['GET', 'POST'])
@login_required
def services():
    services = Services.query.all()
    return render_template("services.html", services=services, user=current_user)


@views.route('/photo', methods=['GET', 'POST'])
@login_required
def photo():
    return render_template("photo.html", user=current_user)


@views.route('/team', methods=['GET', 'POST'])
@login_required
def team():
    return render_template("team.html", user=current_user)
