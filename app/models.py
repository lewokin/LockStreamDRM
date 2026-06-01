from app import db
from sqlalchemy.orm import Mapped, mapped_column

class Copies(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    uuid: Mapped[str] = mapped_column(unique=True)
    serial: Mapped[str] = mapped_column(nullable=False, unique=True)

class Versions(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    version : Mapped[str] = mapped_column(unique=True, nullable=False)
    sha256: Mapped[str] = mapped_column(unique=True, nullable=False)