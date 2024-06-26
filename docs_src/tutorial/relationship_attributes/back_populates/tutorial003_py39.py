from typing import Optional

from sqldev import Field, Relationship, SQLDev, create_engine


class Weapon(SQLDev, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True)

    hero: "Hero" = Relationship(back_populates="weapon")


class Power(SQLDev, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True)

    hero_id: int = Field(foreign_key="hero.id")
    hero: "Hero" = Relationship(back_populates="powers")


class Team(SQLDev, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    headquarters: str

    heroes: list["Hero"] = Relationship(back_populates="team")


class Hero(SQLDev, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    secret_name: str
    age: Optional[int] = Field(default=None, index=True)

    team_id: Optional[int] = Field(default=None, foreign_key="team.id")
    team: Optional[Team] = Relationship(back_populates="heroes")

    weapon_id: Optional[int] = Field(default=None, foreign_key="weapon.id")
    weapon: Optional[Weapon] = Relationship(back_populates="hero")

    powers: list[Power] = Relationship(back_populates="hero")


sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

engine = create_engine(sqlite_url, echo=True)


def create_db_and_tables():
    SQLDev.metadata.create_all(engine)


def main():
    create_db_and_tables()


if __name__ == "__main__":
    main()
