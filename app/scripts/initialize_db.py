from sqlalchemy import create_engine
from app.models import Base


def main():
    # Url Connection Dengan Database PostgreSQL
    db_url = 'postgresql://root:123456@localhost:5432/postgres'
    engine = create_engine(db_url)

    Base.metadata.create_all(engine)


if __name__ == '__main__':
    main()
