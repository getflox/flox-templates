from flask import Blueprint, render_template

main_bp = Blueprint('main_bp', __name__,
                    url_prefix="/",
                    template_folder='templates',
                    static_folder='static',
                    static_url_path='assets')


@main_bp.route("/")
def index():
    return render_template("index.html")
