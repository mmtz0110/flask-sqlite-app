from appwrite.client import Client
from appwrite.services.account import Account
from appwrite.services.tables_db import TablesDB
from appwrite.services.users import Users

from app.config import Config


class AppwriteService:
    def __init__(self) -> None:
        if not Config.APPWRITE_PROJECT_ID:
            raise RuntimeError("APPWRITE_PROJECT_ID belum dikonfigurasi")
        if not Config.APPWRITE_API_KEY:
            raise RuntimeError("APPWRITE_API_KEY belum dikonfigurasi")

        self.client = (
            Client()
            .set_endpoint(Config.APPWRITE_ENDPOINT)
            .set_project(Config.APPWRITE_PROJECT_ID)
            .set_key(Config.APPWRITE_API_KEY)
        )
        self.db = TablesDB(self.client)
        self.users = Users(self.client)
        self.db_id = Config.APPWRITE_DATABASE_ID

        account_client = (
            Client()
            .set_endpoint(Config.APPWRITE_ENDPOINT)
            .set_project(Config.APPWRITE_PROJECT_ID)
        )
        self.account = Account(account_client)


appwrite = AppwriteService()
