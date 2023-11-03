import os
from flask import request, jsonify, Response
from . import db
from .models import Projects

# App Initialization
from . import create_app # from __init__ file
app = create_app(os.getenv("CONFIG_MODE"))


# Get the project detail, all projects will be returned if the projectId isn't supplied in the URL.
@app.route('/<int:projectId>', methods=['GET'])
@app.route('/', methods=['GET'])
def GetProject(projectId=None):
    try:
        if projectId:
            objProject = Projects.query.get(projectId)
            if objProject:
                response = objProject.toDict()
                return response
            else:
                return Response({'message':'Record not found.'}, status=204, content_type='application/json')
        else:
            projects = Projects.query.all()
            # Convert the list of SQLAlchemy objects to a list of dictionaries
            projects_data = [
                {
                    'id': project.id,
                    'Title': project.Title,
                    'Description': project.Description,
                    'Completed': project.Completed,
                    'created_at': project.created_at.isoformat() if project.created_at else None  # Format the datetime as ISO 8601
                }
                for project in projects
            ]

            # Return the list of dictionaries as JSON
            return jsonify(projects_data)
    except Exception as ex:
        return Response(jsonify(ex.args[0]), status=400, content_type='application/json')


#Creating a new project record.
@app.route('/', methods=['POST'])
def SaveProject():
    try:
        request_form = request.form.to_dict()
        completed = True if request_form['completed'].lower() == 'true' else False
        objProject = Projects(
                                Title = request_form['title'],
                                Description = request_form['description'],
                                Completed = completed
                            )
        db.session.add(objProject)
        db.session.commit()

        response = Projects.query.get(objProject.id).toDict()
        return response
    except Exception as ex:
        return Response(jsonify(ex.args[0]), status=400, content_type='application/json')


#Update the existing method by giving the projectId parameter in the URL.
@app.route('/<int:projectId>', methods=['PUT'])
def UpdateProject(projectId):
    try:
        request_form = request.form.to_dict()
        objProject = Projects.query.get(projectId)
        completed = True if request_form['completed'].lower() == 'true' else False

        objProject.Title = request_form['title']
        objProject.Description = request_form['description']
        objProject.Completed = completed
        db.session.commit()

        response = Projects.query.get(projectId).toDict()
        return response
    except Exception as ex:
        return Response(jsonify(ex.args[0]), status=400, content_type='application/json')


#Delete the prject from the db by giving the projectId.
@app.route('/<int:projectId>', methods=['DELETE'])
def DeleteProject(projectId):
    try:
        Projects.query.filter_by(id=projectId).delete()
        db.session.commit()

        return ('Project with Id "{}" deleted successfully!').format(projectId)
    except Exception as ex:
        return Response(jsonify(ex.args[0]), status=400, content_type='application/json')


if __name__ == "__main__":
    # To Run the Server in Terminal => flask run -h localhost -p 5000
    # To Run the Server with Automatic Restart When Changes Occurred => FLASK_DEBUG=1 flask run -h localhost -p 5000

    app.run()