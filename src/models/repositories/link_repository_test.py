import pytest
import uuid
from .links_repository import LinksRepository
from src.models.settings.db_connection_handler import db_connection_handler

db_connection_handler.connect() 
link_id = str(uuid.uuid4())
trip_id = str(uuid.uuid4())

@pytest.mark.skip(reason='interação com o banco')
def test_registry_link():
    conn = db_connection_handler.get_connection()
    link_repository = LinksRepository(conn)

    link_infos = {
        "id": link_id,
        "trip_id": trip_id,
        "link": "clonacartao.com",
        "tittle": "cartoes"
    }

    link_repository.registry_link(link_infos)

@pytest.mark.skip(reason='interação com o banco')
def test_find_links_from_trip():
    conn = db_connection_handler.get_connection()
    link_repository = LinksRepository(conn)


    link = link_repository.find_links_from_trip(trip_id)
    print()
    print(link)
    assert isinstance(link, list)
    assert isinstance(link[0], tuple)



    