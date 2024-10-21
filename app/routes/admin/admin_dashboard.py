from flask import render_template
from app import app, db
from flask_login import login_required
from app.models.pin import Pin
from app.models.user import User
from sqlalchemy import func

@app.route('/admin_dashboard', methods=['GET'])
@login_required
def admin_dashboard():
    # Calculate total pins generated
    total_pins_generated = db.session.query(func.count(Pin.id)).scalar()

    # Calculate total pins unused
    total_pins_unused = db.session.query(func.count(Pin.id)).filter(Pin.date_used.is_(None)).scalar()
    
    # Ensure that total_pins_generated is not zero to avoid division by zero
    if total_pins_generated != 0:

        # Calculate total pins used
        total_pins_used = total_pins_generated - total_pins_unused

        # Calculate percentages
        percentage_unused = round((total_pins_unused / total_pins_generated) * 100, 1)
        percentage_used = round((total_pins_used / total_pins_generated) * 100, 1)
    else:
        # If total_pins_generated is zero, set other values to zero
        total_pins_used = 0
        percentage_unused = 0.0
        percentage_used = 0.0
        
        # Calculate total users registered
    total_users_registered = db.session.query(func.count(User.id)).scalar()

    return render_template('admin/dashboard.html', 
                           total_pins_generated=total_pins_generated,
                           total_pins_unused=total_pins_unused,
                           total_pins_used=total_pins_used,
                           percentage_unused=percentage_unused,
                           percentage_used=percentage_used,
                           total_users_registered=total_users_registered)
