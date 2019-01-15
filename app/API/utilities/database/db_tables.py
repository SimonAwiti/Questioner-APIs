"""creating tables for the database"""
users_table = """CREATE TABLE IF NOT EXISTS users
            (
                user_id serial PRIMARY KEY, 
                firstname NOT NULL,
                lastname NOT NULL,
                email UNIQUE NOT NULL,
                password NOT NULL,
                admin BOOLEAN NOT NULL
        )"""

meetups_table = """ CREATE TABLE IF NOT EXISTS meetups 
            (
                meetup_id SERIAL PRIMARY KEY,
                createdOn DATE,
                location NOT NULL,
                topic NOT NULL,
                happeningOn DATE,
                user_id INT REFERENCES users(user_id) ON DELETE CASCADE
        )"""

questions_table = """ CREATE TABLE IF NOT EXISTS questions
            (
                question_id SERIAL PRIMARY KEY,
                createdOn DATE,  
                createdBy INT REFERENCES users(user_id) ON DELETE CASCADE,
                meetup_id INT REFERENCES meetups(meetup_id) ON DELETE CASCADE, 
                title NOT NULL UNIQUE,
                body NOT NULL,
                votes INTEGER NOT NULL,
                comment NOT NULL
        )"""

queries = [users_table, meetups_table, questions_table]

droppings = [
                "DROP TABLE users CASCADE",
                "DROP TABLE meetups CASCADE",
                "DROP TABLE questions CASCADE"
            ]
