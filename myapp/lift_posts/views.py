from flask import render_template, url_for, flash, request, redirect, Blueprint, abort
from flask_login import current_user, login_required
from myapp import db 
from myapp.models import Workout
from myapp.lift_posts.forms import LiftPostForm

lift_posts = Blueprint('lift_posts', __name__)

@lift_posts.route('/create', methods=['GET', 'POST'])
@login_required
def create_post():
    form = LiftPostForm()
    if form.validate_on_submit():
        lift_post = Workout(title=form.title.data, text=form.text.data, user_id=current_user.id)
        db.session.add(lift_post)
        db.session.commit()
        flash('Lift Post Created')
        print('Workout was created')
        return redirect(url_for('core.index'))
    return render_template('create_post.html', form=form)

@lift_posts.route('/<int:lift_post_id>')
def lift_post(lift_post_id):
    lift_post = Workout.query.get_or_404(lift_post_id) 
    return render_template('lift_post.html', title=lift_post.title, date=lift_post.date, post=lift_post)