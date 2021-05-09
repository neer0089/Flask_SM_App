# Flask_SM_App
A simple social media REST API. Where users can post posts and eventually
like and comment on those posts. 

## Intstallation and Usage:

First install all the dependencies. Run:

`pip install requirements.txt`

This app stores data in a MongoDB database. You have to run a MongoDB
Instance on your own. And then you need to pass in the MongoDB host 
and port in the config.ini file which is found in the root directory.
Example:

`mongodb_host = localhost`

`mongodb_port = 27017`

A login secret should also be provided in the config.ini file.

Once configuration is properly done. Simply run:

`python run.py`

This will spwan a development server running the application.