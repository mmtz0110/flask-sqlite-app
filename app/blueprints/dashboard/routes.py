from flask import Blueprint, redirect, render_template, session, url_for

dashboard_bp = Blueprint("dashboard", __name__)


@dashboard_bp.get("/")
def index():
    if "user_id" not in session:
        return redirect(url_for("auth.login"))
    return render_template("dashboard/index.html")
