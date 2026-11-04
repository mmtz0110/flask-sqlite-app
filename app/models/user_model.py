from app.services.appwrite_service import appwrite


class UserModel:
    TABLE_ID = "users"

    @classmethod
    def create_profile(
        cls, user_id: str, nama_orang_tua: str, email: str,
        nomor_telepon: str, role: str
    ):
        return appwrite.db.create_row(
            database_id=appwrite.db_id,
            table_id=cls.TABLE_ID,
            row_id=user_id,
            data={
                "nama_orang_tua": nama_orang_tua,
                "email": email,
                "nomor_telepon": nomor_telepon,
                "role": role,
            },
        )

    @classmethod
    def get_by_id(cls, user_id: str):
        try:
            return appwrite.db.get_row(
                database_id=appwrite.db_id,
                table_id=cls.TABLE_ID,
                row_id=user_id,
            )
        except Exception:
            return None
