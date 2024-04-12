from sqlalchemy import inspect
from sqlalchemy.engine.reflection import Inspector
from sqldev import create_engine

from ....conftest import needs_py310


@needs_py310
def test_tutorial001(clear_sqldev):
    from docs_src.tutorial.connect.create_tables import tutorial001_py310 as mod

    mod.sqlite_url = "sqlite://"
    mod.engine = create_engine(mod.sqlite_url)
    mod.main()
    insp: Inspector = inspect(mod.engine)
    assert insp.has_table(str(mod.Hero.__tablename__))
    assert insp.has_table(str(mod.Team.__tablename__))
