[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Coverage Status](https://coveralls.io/repos/github/SimonAwiti/Questioner-APIs/badge.svg?branch=develop)](https://coveralls.io/github/SimonAwiti/Questioner-APIs?branch=develop)
[![Build Status](https://travis-ci.org/SimonAwiti/Questioner-APIs.svg?branch=develop)](https://travis-ci.org/SimonAwiti/Questioner-APIs)
[![Maintainability](https://api.codeclimate.com/v1/badges/b661f5121ff42ce67210/maintainability)](https://codeclimate.com/github/SimonAwiti/Questioner-APIs/maintainability)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/6f724a002c364f729b23d069afbbe6eb)](https://www.codacy.com/app/SimonAwiti/Questioner-APIs?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=SimonAwiti/Questioner-APIs&amp;utm_campaign=Badge_Grade)


# Questioner Application
# Questioner application endpoints

## The following are API endpoints enabling one to: 
* Create account and log in
* Create a meetup record
* Create get single and all question
* Get a specific meetup record
* Get all meetup records
* Upvote or downvote a question.
* Rsvp for a meetup.
* comment on a question.
* View all the questions for a specific meetup


## Here is a list of the functioning endpoints

| EndPoint                      | Functionality                    |  Actual routes                |
| :---                          |     :---:                        |    :---:              |
| GET / Meetups/ <meetupid>     | Get a specific meetup  record     |  /api/v1/meetups/<meetup-id>     |
| GET /meetups/upcoming         | Fetch all meetup records         |  /api/v1/meetups            |
| POST / meetups                | Create a meetup record           |  /api/v1/meetups/           |
| POST / questions              | Create a question record         |  /api/v1/questions/         |
|POST /meetups/<meetup-id>/rsvps|Respond to meetup RSVP.           |  /api/v1/<meetupid>rspvs/   |
|PATCH /questions/<question-id>/upvote| Upvote a specific question| /api/v1/questions/<questionid> /upvote            |
|PATCH /questions/<question-id>/downvote| Downvote a specific question|  /api/v1/questions/<questionid>/downvote             |
| POST /users                   | User log in                      |  /api/v1/users/login          |
| POST /users                   | User registration                |  /api/v1/users/register       |
| POST / meetups                | Create a meetup record           |  /api/v2/meetups              |
| GET / Meetups/ <meetupid>     | Get a specific meetup  record     |  /api/v2/meetups/<meetup-id> |
| GET /meetups/upcoming         | Fetch all meetup records         |  /api/v2/meetups              |
| GET /meetups/upcoming/questions  | Fetch all meetup records with questions        |  /api/v2/meetups/<meetupid>/questions      |
 POST / questions              | Create a question record         |  /api/v2/questions         |
 |PATCH /questions/<question-id>/upvote| Upvote a specific question| /api/v2/questions/<questionid> /upvote            |
|PATCH /questions/<question-id>/downvote| Downvote a specific question|  /api/v2/questions/<questionid>/downvote             |
| POST /users                   | User log in                      |  /api/v2/users/login          |
| POST /users                   | User registration                |  /api/v2/users/register       |
|POST /meetups/<meetup-id>/rsvps|Respond to meetup RSVP.           |  /api/v2/<meetupid>rspvs/   |
| POST / comments                | Create a meetup record           |  /api/v1/comments/           |
| POST / comments                | Create a meetup record           |  /api/v1/questions/<questionid>comments       |



## Testing the endpoints

* Install python then using pip install .. install flask
* clone the repo
* Ensure that postman is installed
* From your terminal locate the repo and run: python run.py
* open postman and test the endpoints
* Use unittest to run the the tests

## Setting up and how to start the application

* Install python then using pip instal .. install flask
* clone the repo
* From your terminal Ensure that the virtual environment is activated
* From your terminal Ensure that the urls are entered according to the .env file
* From the terminal locate the repo and run: python run.py

# How to get started


Login into your github account and open the project folder then follow the instruction on how to clone the existing project. It should be something similar to:

```
git clone https://github.com/SimonAwiti/Questioner-APIs.git
```

Next, install the requirements by typing:
```

## Create a Python Virtual Environment for our Project

Since we are using Python 3, create a virtual environment by typing:

```
virtualenv -p python3 venv
```

Before we install our project's Python requirements, we need to activate the virtual environment. You can do that by typing:

```
source venv/bin/activate
```
Export all the environments settings and database URLs

Run the app by typing flask run
'''

## Unit Testing
To test the endpoints ensure that the following tools are available the follow steps below
   ### Tools:
     Postman

## Technology used

* Python 3.6
* Flask framework
* Unittest for testing

## Background context 

Published POSTMAN documentation

# Written by: Simon Awiti
#### Copyright © Andela 2019

