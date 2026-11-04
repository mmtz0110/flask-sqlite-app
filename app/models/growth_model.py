from appwrite.id import ID
from appwrite.query import Query

from app.services.appwrite_service import appwrite


class GrowthModel:
    TABLE_ID = "growth_logs"

    @classmethod
    def add_log(
        cls, anak_id, tanggal_ukur, usia_bulan, berat_badan, tinggi_badan,
        status_stunting, prediksi_durasi
    ):
        data = {
            "anak_id": anak_id,
            "tanggal_ukur": tanggal_ukur,
            "usia_bulan": int(usia_bulan),
            "berat_badan": float(berat_badan),
            "tinggi_badan": float(tinggi_badan),
            "status_stunting": status_stunting,
        }
        if prediksi_durasi is not None:
            data["prediksi_durasi"] = float(prediksi_durasi)
        return appwrite.db.create_row(
            database_id=appwrite.db_id,
            table_id=cls.TABLE_ID,
            row_id=ID.unique(),
            data=data,
        )

    @classmethod
    def get_by_child(cls, anak_id):
        return appwrite.db.list_rows(
            database_id=appwrite.db_id,
            table_id=cls.TABLE_ID,
            queries=[
                Query.equal("anak_id", anak_id),
                Query.order_desc("tanggal_ukur"),
            ],
        )
