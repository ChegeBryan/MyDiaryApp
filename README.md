[![Build Status](https://travis-ci.com/ChegeBryan/MyDiaryApp.svg?branch=develop)](https://travis-ci.com/ChegeBryan/MyDiaryApp) [![Coverage Status](https://coveralls.io/repos/github/ChegeBryan/MyDiaryApp/badge.svg?branch=master)](https://coveralls.io/github/ChegeBryan/MyDiaryApp?branch=master) 

# MyDiaryApp
MyDiary is an online journal where users can pen down their thoughts and feelings.

## Getting started

Make sure you have the following:
- Python3
- Flask
- virtualenv

### Installation

1. #### Clone repo to your machine
    ```git clone https://github.com/ChegeBryan/MyDiaryApp```

2. #### Create a virtual environment
    ```virtualenv -p python3 Venv```
    ```source venv/bin/activate```

3. #### Install dependencies
    ```pip install -r requirements.txt```

4. #### Run the app
    ```flask run```

5. #### Run tests
    ```pytest```


### Viewing the endpoints on Postman

Append the following url on the server url:

1. #### View entries GET method
    ```api/v1/entries```

2. #### Create an entry POST method
    ```api/v1/entries```

3. #### Modify an entry PUT method
    ```api/v1/entries/1```

4. #### View entry by id GET method
    ```api/v1/entries/1```

