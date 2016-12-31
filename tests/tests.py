import pytest
import sqlalchemy

"""
database tests
"""


@pytest.fixture
def database_connection():
    import sqlalchemy
    #create dbconnection for further tests


def test_backup_exists():
    #check to see if a backup exists of the current data

def test_schema_ver(database_connection):
    #test to see if db is on correct version

def test_tables_exist(database_connection):
    #test to see if all of the tables were created successfully and report back which ones were not

def test_indexs_exist(database_connection):
    #test to see if all of the indexes were created and report their current status
    #make sure to put in logic to check if they are rebuilding and wait for them to finish and log the time it took to rebuild

def test_triggers_exits(database_connection):
    #check to see if the triggers exist

def test_create_player(database_connection):
    #create a new set of test player in the database_connection

def test_create_event(database_connection):
    #create a new event

def test_create_tournament_3_round(database_connection):
    #create a new 3 round tournament

def test_create_tournament_6_round(database_connection):
    #create a new 5 round tournament

def test_create_tournament_8_round(database_connection):
    #create a new 7 round tournament

def test_create_team_tournament(database_connection):
    #create a new 6 round, 64 5 man team event