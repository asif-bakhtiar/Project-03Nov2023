# Project-03Nov2023

---> This is the project which has a single model and CRUD operation API's are made in that.

0- Before running the project, fix the credentials of database in the .env file located at ..src/.env

1- Create a new virtual environment and activate that.

2- Install the project requirements in the virtual environment:
$ pip install -r requirements.txt

3- To run this project, make the migrations first using the below commands:
$ flask db init
$ flask db migrate
$ flask db upgrade

4- Run the project with the below command from the root of the .../src directory.
$ flask run

==================================================
# Endpoints details
To create a project record, you can send the payload in the form body ('title', 'description', 'completed') at URL '/'.

To GET all the records, just call the [GET] request at '/'.
To GET the record by id, call the [GET] method with URL '/[projectId]'

To Update the record, send the 'projectId' in the [PUT] request at URL ('/[projectId]') and the content in the form body ('title', 'description', 'completed') at URL '/'.

To Delete the record, just send the 'projectId' in the [DELETE] request at URL ('/[projectId]').
