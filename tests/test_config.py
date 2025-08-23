from pytest import fixture
from fastapi.testclient import TestClient
from db import create_engine, SessionLocal, sessionmaker, Base, get_db
from config import settings
from sqlalchemy.pool import StaticPool
from main import app


@fixture(scope="module")
def override_db_engine():
    
    engine = create_engine(
        settings.TESTS_DATABASE_URL,
        connect_args={"check_same_thread": False},
        poolclass=StaticPool
    )
    
    Base.create_all(engine)
    
    return engine

@fixture(scope="module")
def client_instance(override_db_engine):
    
    SessionLocal = sessionmaker(bind=override_db_engine, autoflush=False, autocommit=False)
    
    def override_db():
        db = SessionLocal()
        
        try:
            yield db
        finally:
            db.close()
            
    app.dependency_overrides[get_db] = override_db
    
    client = TestClient(app)
    
    return client