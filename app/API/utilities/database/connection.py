import os
import psycopg2


from app.API.utilities.database.db_tables import queries, droppings

def dbconnection():
    """making a connection to the db"""
    url = os.getenv('DATABASE_URL')
    return psycopg2.connect(url)


def initializedb():
    try:
        """starting the database"""
        connection = dbconnection()
        connection.autocommit = True

        """activate cursor"""
        cursor = connection.cursor()
        for query in queries:
            cursor.execute(query)
        connection.commit()

    except (Exception, psycopg2.DatabaseError) as error:
        print("DB Error")
        print(error)

def generate_admin():
    """Generate the default admin and add to db"""
    gen_admin = """
                INSERT INTO
                users (firstname, lastname, email, password, admin)
                VALUES ('main', 'admin', 'admin12@gmail.com', 'passadmin', true)
                ON CONFLICT (lastname) DO NOTHING
                """
    connection = dbconnection()
    cursor = connection.cursor()
    cursor.execute(gen_admin)
    connection.commit()


def drop_tables():
    """Drops all tables"""
    connection = dbconnection()
    cursor = connection.cursor()
    for drop in droppings:
        cursor.execute(drop)
        connection.commit()