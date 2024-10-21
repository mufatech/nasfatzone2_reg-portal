from flask import render_template
from app import app, db
from flask_login import login_required
from app.models.pin import Pin
from sqlalchemy import func

@app.route('/pin_analytics', methods=['GET'])
@login_required
def pin_analytics():
    # Calculate total pins generated
    total_pins_generated = db.session.query(func.count(Pin.id)).scalar()

    # Calculate total pins unused
    total_pins_unused = db.session.query(func.count(Pin.id)).filter(Pin.date_used.is_(None)).scalar()

    # Calculate total pins used
    total_pins_used = total_pins_generated - total_pins_unused

    # Calculate total pins generated for adults
    total_pins_adults = db.session.query(func.count(Pin.id)).filter(Pin.category == 'adults').scalar()

    # Calculate total pins generated for children
    total_pins_children = db.session.query(func.count(Pin.id)).filter(Pin.category == 'children').scalar()

    # Calculate total pins generated for teens
    total_pins_teens = db.session.query(func.count(Pin.id)).filter(Pin.category == 'teens').scalar()

    # Calculate percentages
    percentage_unused = round((total_pins_unused / total_pins_generated) * 100, 1)
    percentage_used = round((total_pins_used / total_pins_generated) * 100, 1)
    percentage_adults = round((total_pins_adults / total_pins_generated) * 100, 1)
    percentage_children = round((total_pins_children / total_pins_generated) * 100, 1)
    percentage_teens = round((total_pins_teens / total_pins_generated) * 100, 1)


    return render_template('admin/pin_analytics.html', 
                           total_pins_generated=total_pins_generated,
                           total_pins_unused=total_pins_unused,
                           total_pins_used=total_pins_used,
                           total_pins_adults=total_pins_adults,
                           total_pins_children=total_pins_children,
                           total_pins_teens=total_pins_teens,
                           percentage_unused=percentage_unused,
                           percentage_used=percentage_used,
                           percentage_adults=percentage_adults,
                           percentage_children=percentage_children,
                           percentage_teens=percentage_teens)
