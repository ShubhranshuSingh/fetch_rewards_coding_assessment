from flask import Flask, request, render_template, jsonify
from pixel_coordinates import make_grid

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def handle_post_req():
    if request.method == 'POST':
        # Get data from POST request
        img_dim = eval(request.form.get('img_dim'))
        corner_points = eval(request.form.get('corner_points'))
        grid = make_grid(img_dim, corner_points)
        return jsonify({"grid":grid}) # Return JSON data
    return render_template('home.html') # Handle GET request
