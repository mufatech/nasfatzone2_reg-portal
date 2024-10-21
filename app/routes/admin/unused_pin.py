from flask import render_template, request
from app import app
from app.models.pin import Pin
from flask_login import login_required

@app.route('/unused_pins', methods=['GET'])
@login_required
def unused_pins():
    # Retrieve the page number from the request, default to 1 if not provided
    page = request.args.get('page', default=1, type=int)
    
    # Set the number of results per page
    per_page = 15
    
    # Query all pins that have not been used (date_used is None) with pagination
    unused_pins = Pin.query.filter_by(date_used=None).paginate(page=page, per_page=per_page, error_out=False)

    
    return render_template('admin/unused_pins.html', unused_pins=unused_pins)
