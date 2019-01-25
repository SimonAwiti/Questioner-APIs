"""creating tables for the database"""
users_table = """CREATE TABLE IF NOT EXISTS users
            (
                user_id SERIAL PRIMARY KEY, 
                firstname VARCHAR(50) NOT NULL,
                lastname VARCHAR(50) NOT NULL,
                othername VARCHAR(50),
                email VARCHAR(50) NOT NULL UNIQUE,
                password VARCHAR (300) NOT NULL,
                registered TIMESTAMP DEFAULT NOW(),
                isadmin BOOLEAN DEFAULT FALSE
        )"""

meetups_table = """ CREATE TABLE IF NOT EXISTS meetups 
            (
                meetup_id SERIAL PRIMARY KEY NOT NULL,
                createdOn DATE,
                location VARCHAR (50) NOT NULL,
                topic VARCHAR (50) NOT NULL,
                happeningOn DATE

        )"""

questions_table = """ CREATE TABLE IF NOT EXISTS questions
            (
                question_id SERIAL PRIMARY KEY NOT NULL,
                createdOn TIMESTAMP DEFAULT NOW(),  
                user_id INTEGER NOT NULL,
                meetup_id INTEGER NOT NULL, 
                title VARCHAR (50) NOT NULL,
                body VARCHAR (300) NOT NULL,
                FOREIGN KEY (meetup_id) REFERENCES meetups (meetup_id) ON DELETE CASCADE,
                FOREIGN KEY (user_id) REFERENCES users (user_id) ON DELETE CASCADE,
                votes integer DEFAULT 0

        )"""

comments_table = """ CREATE TABLE IF NOT EXISTS comments 
           (
                comment_id SERIAL PRIMARY KEY NOT NULL,
                user_id INTEGER NOT NULL,
                question_id INTEGER NOT NULL,
                title VARCHAR (50) NOT NULL,
                comment VARCHAR (300) NOT NULL,
                createdOn TIMESTAMP DEFAULT NOW(), 
                FOREIGN KEY (question_id) REFERENCES questions (question_id) ON DELETE CASCADE,
                FOREIGN KEY (user_id) REFERENCES users (user_id) ON DELETE CASCADE
        )"""
rsvps_table = """ CREATE TABLE IF NOT EXISTS rsvps 
           (
                rsvp_id SERIAL PRIMARY KEY NOT NULL,
                user_id INTEGER NOT NULL,
                meetup_id INTEGER NOT NULL,
                response VARCHAR (50) NOT NULL,
                FOREIGN KEY (meetup_id) REFERENCES meetups (meetup_id) ON DELETE CASCADE,
                FOREIGN KEY (user_id) REFERENCES users (user_id) ON DELETE CASCADE
        )"""

upvotes_table = """ CREATE TABLE IF NOT EXISTS upvotes(
                question_id INTEGER NOT NULL,
                user_id INTEGER NOT NULL,
                UNIQUE(question_id, user_id),
                FOREIGN KEY (question_id) REFERENCES questions(question_id) ON UPDATE CASCADE ON DELETE CASCADE,
                FOREIGN KEY(user_id) REFERENCES users(user_id) ON UPDATE CASCADE ON DELETE CASCADE
        )"""

downvotes_table = """ CREATE TABLE IF NOT EXISTS downvotes(
                question_id INTEGER NOT NULL,
                user_id INTEGER NOT NULL,
                UNIQUE(question_id, user_id),
                FOREIGN KEY (question_id) REFERENCES questions(question_id) ON UPDATE CASCADE ON DELETE CASCADE,
                FOREIGN KEY(user_id) REFERENCES users(user_id) ON UPDATE CASCADE ON DELETE CASCADE
        )"""

queries = [users_table, meetups_table, questions_table, comments_table, rsvps_table, upvotes_table, downvotes_table]

droppings = [
                "DROP TABLE users CASCADE",
                "DROP TABLE meetups CASCADE",
                "DROP TABLE questions CASCADE",
                "DROP TABLE comments CASCADE",
                "DROP TABLE rsvps CASCADE",
                "DROP TABLE upvotes CASCADE",
                "DROP TABLE downvotes CASCADE"
            ]
