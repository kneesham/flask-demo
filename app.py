from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['POST'])
def receive_data():
    if request.method == 'POST':
        # Access the data sent in the POST request
        data = request.get_json()  # For JSON data
        # data = request.form  # For form data

        # Process the data (e.g., save to database, perform calculations)
        print(data)

        # Return a response
        return data
    
if __name__ == '__main__':
    app.run(debug=True)