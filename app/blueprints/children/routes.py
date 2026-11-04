from datetime import datetime

from flask import Blueprint, flash, redirect, render_template, request, session, url_for

from app.models.child_model import ChildModel
from app.models.growth_model import GrowthModel
from app.services.ml_service import MLService

children_bp = Blueprint("children", __name__, url_prefix="/children")


def _login_required():
    return "user_id" in session


@children_bp.get("/")
def index():
    if not _login_required():
        return redirect(url_for("auth.login"))
    docs = ChildModel.get_by_user(session["user_id"])
    return render_template("children/index.html", children=docs["rows"])


@children_bp.post("/add")
def add_child():
    if not _login_required():
        return redirect(url_for("auth.login"))
    try:
        ChildModel.create(
            session["user_id"],
            request.form.get("nama_anak", "").strip(),
            request.form["tanggal_lahir"],
            int(request.form["jenis_kelamin"]),
        )
        flash("Data anak berhasil ditambahkan.", "success")
    except (KeyError, TypeError, ValueError) as exc:
        flash(f"Data anak tidak valid: {exc}", "danger")
    return redirect(url_for("children.index"))


@children_bp.post("/<child_id>/growth")
def add_growth_log(child_id):
    if not _login_required():
        return redirect(url_for("auth.login"))
    try:
        usia = int(request.form["usia_bulan"])
        berat = float(request.form["berat_badan"])
        tinggi = float(request.form["tinggi_badan"])
        jenis_kelamin = int(request.form.get("jenis_kelamin", 1))
        if not 0 <= usia <= 59 or jenis_kelamin not in (0, 1):
            raise ValueError("usia atau jenis kelamin di luar rentang")
        status, durasi = MLService.predict_stunting(usia, berat, tinggi, jenis_kelamin)
        GrowthModel.add_log(
            anak_id=child_id,
            tanggal_ukur=datetime.now().isoformat(),
            usia_bulan=usia,
            berat_badan=berat,
            tinggi_badan=tinggi,
            status_stunting=status,
            prediksi_durasi=durasi,
        )
        flash(f"Pencatatan berhasil. Status Gizi: {status}", "info")
    except (KeyError, TypeError, ValueError) as exc:
        flash(f"Data pengukuran tidak valid: {exc}", "danger")
    return redirect(url_for("children.index"))
