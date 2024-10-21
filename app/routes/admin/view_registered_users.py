# Import necessary modules
from flask import render_template, request
from app import app
from app.models.user import User
from flask_login import login_required

# Define a route for viewing registered users
@app.route('/view_registered_users', methods=['GET'])
@login_required  # Use login_required to ensure only logged-in admins can access this page
def view_registered_users():
    # Retrieve the page number from the request, default to 1 if not provided
    page = request.args.get('page', default=1, type=int)

    # Set the number of results per page
    per_page = 10  # You can adjust this to your desired number of results per page

    # Query registered users with pagination
    registered_users = User.query.paginate(page=page, per_page=per_page, error_out=False)

    return render_template('admin/view_registered_users.html', registered_users=registered_users)
