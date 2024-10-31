from flask import Blueprint, render_template

cursor_composer_bp = Blueprint('cursor_composer', __name__)

@cursor_composer_bp.route('/cursor-composer')
def cursor_composer():
    return render_template('cursor_composer.html')
