# core/views.py 

from flask import render_template, request, Blueprint
from myapp.models import Workout

core = Blueprint('core', __name__)

@core.route('/')
def index():
    page = request.args.get('page', 1, type=int)
    lift_posts = Workout.query.order_by(Workout.date.desc()).paginate(page=page, per_page=5)
    return render_template('index.html', lift_posts=lift_posts)

@core.route('/info')
def info():
    return render_template('info.html')