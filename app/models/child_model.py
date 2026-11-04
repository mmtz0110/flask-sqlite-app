from appwrite.id import ID
from appwrite.query import Query

from app.services.appwrite_service import appwrite


class ChildModel:
    TABLE_ID = "children"

    @classmethod
    def create(cls, user_id, nama_anak, tanggal_lahir, jenis_kelamin):
        return appwrite.db.create_row(
            database_id=appwrite.db_id,
            table_id=cls.TABLE_ID,
            row_id=ID.unique(),
            data={
                "user_id": user_id,
                "nama_anak": nama_anak,
                "tanggal_lahir": tanggal_lahir,
                "jenis_kelamin": int(jenis_kelamin),
            },
        )

    @classmethod
    def get_by_user(cls, user_id):
        return appwrite.db.list_rows(
            database_id=appwrite.db_id,
            table_id=cls.TABLE_ID,
            queries=[Query.equal("user_id", user_id)],
        )

    @classmethod
    def get_by_id(cls, child_id):
        return appwrite.db.get_row(
            database_id=appwrite.db_id,
            table_id=cls.TABLE_ID,
            row_id=child_id,
        )
