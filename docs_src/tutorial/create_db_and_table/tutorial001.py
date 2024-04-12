from typing import Optional

from sqldev import Field, SQLDev, create_engine


class Hero(SQLDev, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    secret_name: str
    age: Optional[int] = None


sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

engine = create_engine(sqlite_url, echo=True)

SQLDev.metadata.create_all(engine)
