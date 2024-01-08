import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


HOST = "postgres"
PORT = 5432
DATABASE = os.getenv('POSTGRES_DB', 'fip')
USER = os.getenv('POSTGRES_USER', 'fip')
PASSWORD = os.environ['POSTGRES_PASSWORD']  # raises KeyError if not set


engine = create_engine(f'postgresql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}')
Session = sessionmaker(bind=engine)
