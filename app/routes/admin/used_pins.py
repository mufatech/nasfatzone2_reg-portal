# Modify used_pins.py

# Import necessary modules
from flask import render_template, request
from app import app, db
from app.models.pin import Pin
from flask_login import login_required

# Define a route for viewing used pins
@app.route('/used_pins', methods=['GET'])
@login_required
def used_pins():
    # Retrieve the page number from the request, default to 1 if not provided
    page = request.args.get('page', default=1, type=int)
    
    # Set the number of results per page
    per_page = 15
    
    # Query all pins that have been used (date_used is not None) with pagination
    used_pins = (
        Pin.query
        .filter(Pin.date_used.isnot(None))
        .paginate(page=page, per_page=per_page, error_out=False)
    )

    return render_template('admin/used_pins.html', used_pins=used_pins)
