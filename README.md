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
* From the terminal locate the repo and run: python run.py

# How to get started

Start by making a directory where we will work on. Simply Open your terminal and then:

```
mkdir Questioner-APIs
```

Afterwhich we go into the directory:

```
cd Questioner-APIs
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

## Clone and Configure a Flask Project

Login into your github account and open the project folder then follow the instruction on how to clone the existing project. It should be something similar to:

```
git clone https://github.com/SimonAwiti/Questioner-APIs.git
```

Next, install the requirements by typing:

```
pip install -r requirements.txt
```

## How to run the app

```
flask run
```

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

