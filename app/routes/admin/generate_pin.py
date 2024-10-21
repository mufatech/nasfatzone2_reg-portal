from random import randint
from flask import render_template, request, redirect, flash, url_for
from app import app, db
from app.models.pin import Pin
from flask_login import login_required

# ...

@app.route('/generate_pin', methods=['GET', 'POST'])
@login_required
def generate_pin():
    if request.method == 'POST':
        pin_category = request.form.get('pin_category')
        pin_count = int(request.form.get('pin_count'))
        
        # Determine the pin length based on the category
        if pin_category == 'children':
            pin_length = 6
        elif pin_category == 'teens':
            pin_length = 8
        elif pin_category == 'adults':
            pin_length = 10
        else:
            flash('Invalid pin category', 'danger')
            return redirect(url_for('generate_pin'))

        # Generate the pins
        generated_pins = []
        for _ in range(pin_count):
            generated_pin = ''.join(str(randint(0, 9)) for _ in range(pin_length))
            generated_pins.append(generated_pin)

            # Store each generated pin in the database (create a Pin model for this)
            pin = Pin(category=pin_category, value=generated_pin)
            db.session.add(pin)

        db.session.commit()

        return render_template('admin/generate_pin.html', generated_pins=generated_pins, pin_category=pin_category)

    return render_template('admin/generate_pin.html')