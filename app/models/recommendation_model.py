from appwrite.id import ID
from appwrite.query import Query

from app.services.appwrite_service import appwrite


class RecommendationModel:
    TABLE_ID = "ai_recommendations"

    @classmethod
    def get_by_child(cls, anak_id):
        return appwrite.db.list_rows(
            database_id=appwrite.db_id,
            table_id=cls.TABLE_ID,
            queries=[
                Query.equal("anak_id", anak_id),
                Query.order_desc("tanggal"),
            ],
        )

    @classmethod
    def create(cls, anak_id, tanggal, kategori, nama_rekomendasi):
        return appwrite.db.create_row(
            database_id=appwrite.db_id,
            table_id=cls.TABLE_ID,
            row_id=ID.unique(),
            data={
                "anak_id": anak_id,
                "tanggal": tanggal,
                "kategori": kategori,
                "nama_rekomendasi": nama_rekomendasi,
                "is_checked": False,
            },
        )
