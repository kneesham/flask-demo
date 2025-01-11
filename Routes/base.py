from flask import Blueprint

auth_blueprint = Blueprint('base', __name__)

@auth_blueprint.route('/', methods=['POST'])
def receive_data():
    if request.method == 'POST':
        # Access the data sent in the POST request
        data = request.get_json()  # For JSON data
        # data = request.form  # For form data

        # Process the data (e.g., save to database, perform calculations)
        print(data)

        # Return a response
        return data