"""creating tables for the database"""
users_table = """CREATE TABLE IF NOT EXISTS users
            (
                user_id serial PRIMARY KEY, 
                firstname VARCHAR (50) UNIQUE NOT NULL,
                lastname VARCHAR (50) UNIQUE NOT NULL,
                email VARCHAR (50) UNIQUE NOT NULL,
                password VARCHAR (50) UNIQUE NOT NULL,
                confirm VARCHAR (50) UNIQUE NOT NULL,
                admin BOOLEAN NOT NULL
        )"""

meetups_table = """ CREATE TABLE IF NOT EXISTS meetups 
            (
                meetup_id SERIAL PRIMARY KEY,
                createdOn DATE,
                location VARCHAR (50) UNIQUE NOT NULL,
                topic VARCHAR (50) UNIQUE NOT NULL,
                happeningOn DATE,
                user_id INT REFERENCES users(user_id) ON DELETE CASCADE
        )"""

questions_table = """ CREATE TABLE IF NOT EXISTS questions
            (
                question_id SERIAL PRIMARY KEY,
                createdOn DATE,  
                createdBy INT REFERENCES users(user_id) ON DELETE CASCADE,
                meetup_id INT REFERENCES meetups(meetup_id) ON DELETE CASCADE, 
                title VARCHAR (50) UNIQUE NOT NULL,
                body VARCHAR (70) UNIQUE NOT NULL,
                votes INTEGER NOT NULL,
                comment VARCHAR (50) UNIQUE NOT NULL
        )"""

queries = [users_table, meetups_table, questions_table]

droppings = [
                "DROP TABLE users CASCADE",
                "DROP TABLE meetups CASCADE",
                "DROP TABLE questions CASCADE"
            ]
