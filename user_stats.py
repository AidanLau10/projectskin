from flask import Flask, jsonify
from flask_cors import CORS

# initialize a flask application (app)
app = Flask(__name__)
CORS(app, supports_credentials=True, origins='*')  # Allow all origins (*)

# ... your existing Flask

# add an api endpoint to flask app
@app.route('/api/data')
def get_data():
    # start a list, to be used like a information database
    user_stats = []

    # add a row to list, an Info record
    user_stats.append({
        "ingredient_id": 12345,
        "ingredient_name": "Glycerin",
        "purpose": "Moisturizer",
        "rating": "Goodie",
        "fda_url": "https://incidecoder.com/ingredients/glycerin",
    })

    # add a row to list, an Info record
    user_stats.append({
        "ingredient_id": 12346,
        "ingredient_name": "Hyaluronic Acid",
        "purpose": "Moisturizer",
        "rating": "Goodie",
        "fda_url": "https://incidecoder.com/ingredients/hyaluronic-acid",
    })
    
    return jsonify(user_stats)

# add an HTML endpoint to flask app
@app.route('/')
def say_hello():
    html_content = """
    <html>
    <head>
        <title>User Statistics</title>
    </head>
    <body>
        <h2>User Statistics</h2>
    </body>
    </html>
    """
    return html_content

if __name__ == '__main__':
    # starts flask server on default port, http://127.0.0.1:5001
    app.run(host='0.0.0.0', port=5001)