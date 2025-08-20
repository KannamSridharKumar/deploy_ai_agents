import os
from sqlalchemy import create_engine, text
from dotenv import load_dotenv
load_dotenv()

PG_DATABASE = os.getenv("PG_DATABASE")
PG_USERNAME = os.getenv("PG_USERNAME")
PG_PASSWORD = os.getenv("PG_PASSWORD")
PG_HOST = os.getenv("PG_HOST")
PG_PORT = os.getenv("PG_PORT")
DATABASE_URL = f"postgresql+psycopg2://{PG_USERNAME}:{PG_PASSWORD}@{PG_HOST}:{PG_PORT}/{PG_DATABASE}"

engine = create_engine(DATABASE_URL)
with engine.connect() as conn:
    result = conn.execute(text("SELECT * FROM order_status LIMIT 5;"))
    for row in result:
        print(row)