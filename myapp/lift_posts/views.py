from flask import render_template, url_for, flash, request, redirect, Blueprint, abort
from flask_login import current_user, login_required
from myapp import db 
from myapp.models import Workout
from myapp.lift_posts.forms import LiftPostForm

lift_posts = Blueprint('lift_posts', __name__)