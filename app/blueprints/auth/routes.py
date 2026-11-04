from flask import Blueprint, flash, redirect, render_template, request, session, url_for
from appwrite.id import ID

from app.models.user_model import UserModel
from app.services.appwrite_service import appwrite

auth_bp = Blueprint("auth", __name__, url_prefix="/auth")


@auth_bp.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        nama = request.form.get("nama", "").strip()
        email = request.form.get("email", "").strip()
        password = request.form.get("password", "")
        phone = request.form.get("phone", "").strip()
        role = request.form.get("role", "orang_tua")
        try:
            account_res = appwrite.users.create(
                user_id=ID.unique(), email=email, password=password, name=nama
            )
            UserModel.create_profile(
                account_res["$id"], nama, email, phone, role
            )
            flash("Registrasi berhasil! Silakan login.", "success")
            return redirect(url_for("auth.login"))
        except Exception as exc:
            flash(f"Gagal mendaftar: {exc}", "danger")
    return render_template("auth/register.html")


@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        try:
            email = request.form.get("email", "").strip()
            password = request.form.get("password", "")
            account = appwrite.account.create_email_password_session(email, password)
            profile = UserModel.get_by_id(account["userId"])
            session["user_id"] = account["userId"]
            session["user_name"] = profile["nama_orang_tua"] if profile else email
            session["user_role"] = profile["role"] if profile else "orang_tua"
            flash("Berhasil masuk!", "success")
            return redirect(url_for("dashboard.index"))
        except Exception as exc:
            flash(f"Login gagal: {exc}", "danger")
    return render_template("auth/login.html")


@auth_bp.get("/logout")
def logout():
    session.clear()
    flash("Anda telah keluar.", "info")
    return redirect(url_for("auth.login"))
