from sqlalchemy import create_engine, text

print("Checking orders_sqlite.db")
engine = create_engine('sqlite:///./orders_sqlite.db')
with engine.connect() as conn:
    result = conn.execute(text("SELECT * FROM order_status LIMIT 5;"))
    for row in result:
        print(row)

print("--------------------------------")
print("Checking agent_sqlite.db")
engine = create_engine('sqlite:///./agent_sqlite.db')
with engine.connect() as conn:
    result = conn.execute(text("SELECT * FROM agent_sessions LIMIT 5;"))
    for row in result:
        print(row)

# engine = create_engine('sqlite:///./chinook_sqlite.db')
# with engine.connect() as conn:
#     result = conn.execute(text("SELECT * FROM artist LIMIT 5;"))
#     for row in result:
#         print(row)






