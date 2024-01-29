# Import the Flask module and make_response function
from flask import Flask, make_response, request

# Create an instance of the Flask class
app = Flask(__name__)

# Define a route for the root URL ("/")
@app.route("/")
def index():
    return "hello world"

# Define a route for the "/no_content" URL
@app.route("/no_content")
def no_content():
    """Return 'no content found' with a status of 204
    
    Returns:
        string: 'no content found' with 204 status code
    """
    return ({"message":"No content found"}, 204)

# Define a route for the "/exp" URL
@app.route("/exp")
def index_explicit():
    """Return 'Hello World' message with a status code of 200
    
    Returns:
        string: 'Hello World'
        status code: 200
    """
    # Create a response object using make_response function
    resp = make_response({"message":"Hello World"})
    resp.status_code = 200
    return resp

# Define a route for the "/name_search" URL
@app.route("/name_search")
def name_search():
    """Find a person in the database
    
    Returns:
        json: person if found, with status of 200
        404: if not found
        422: if argument q is missing
    """
    # Get the value of the "q" query parameter
    data = [
        {"first_name": "John", "last_name": "Doe"},
        {"first_name": "Jane", "last_name": "Smith"},
        {"first_name": "Alice", "last_name": "Johnson"}
    ]

    query = request.args.get("q")

    # Check if the "q" parameter is missing
    if not query:
        return {"message": "Invalid input parameter"}, 422

    # Search for the person in the database
    for person in data:
        if query.lower() in person["first_name"].lower():
            return person

    # Return a 404 status code if the person is not found
    return ({"message": "Person not found"}, 404)

# To run the server, use the following command
# flask --app server --debug run
# curl -X GET -i -w '\n' localhost:5000
