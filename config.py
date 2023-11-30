import dataclasses
import os

from dotenv import load_dotenv

load_dotenv()


@dataclasses.dataclass(frozen=True, kw_only=True, slots=True)
class AppConfig:
    db_engine: str = "django.db.backends.postgresql"
    db_name: str = "postgres"
    db_host: str = "localhost"
    db_port: int = 5432
    db_user: str = "postgres"
    db_password: str = "postgres"
    debug: bool = False
    admin_tg_id: str | None = None


def get_config() -> AppConfig:
    return AppConfig(
        db_engine=os.environ["DB_ENGINE"],
        db_name=os.environ["DB_NAME"],
        db_host=os.environ["DB_HOST"],
        db_port=int(os.environ["DB_PORT"]),
        db_user=os.environ["DB_USER"],
        db_password=os.environ["DB_PASSWORD"],
        debug=bool(os.environ["DEBUG"]),
        admin_tg_id=str(os.environ["ADMIN_TG_ID"]),
    )
