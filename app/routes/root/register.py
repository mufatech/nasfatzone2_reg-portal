# routes/user.py
from flask import render_template, request, redirect, url_for, flash
from app import app, db, mail
from app.models.user import User
from app.models.pin import Pin
from flask_login import login_user
from flask_mail import Mail, Message
from datetime import datetime

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        number = request.form.get('number')
        email = request.form.get('email')
        zone = request.form.get('zone')
        branch = request.form.get('branch')
        gender = request.form.get('gender')
        category = request.form.get('category')
        age_range = request.form.get('age_range')
        payment_date = request.form.get('payment_date')
        registration_pin = request.form.get('registration_pin')
        expectations = request.form.get('expectations')
        
        # Check if the registration_pin exists and is unused
        pin = Pin.query.filter_by(value=registration_pin, date_used=None, category=category).first()
        
        if not pin:
            flash('Invalid registration PIN or the PIN was not generated for the category you are trying to use it.', 'danger')
        elif pin.date_used:
            flash('Registration PIN already used.', 'danger')
        elif pin.category != category:
            flash('Error, the PIN was not generated for the category you are trying to use it.', 'danger')
        else:
            # Mark the PIN as used
            pin.date_used = datetime.utcnow()
            db.session.add(pin)
            
            # Create a new user
            user = User(first_name=first_name, last_name=last_name, 
                        number=number, email=email, zone=zone, branch=branch, 
                        gender=gender, category=category, age_range=age_range, payment_date=payment_date,
                        registration_pin=registration_pin, 
                        expectations=expectations)
            db.session.add(user)
            
            # Send a welcome email
            send_welcome_email(user)
            
            db.session.commit()
            
            
            return redirect(url_for('success_page'))  # Redirect to your login route

    return render_template("root/register.html")


def send_welcome_email(user):
    try:
        subject = 'Welcome To Nasfat Youth Wing Lagos zone 2 Camp 2024'
        html_template = render_template('user/welcome_email.html', user=user)

        msg = Message(subject, recipients=[user.email])
        msg.html = html_template

        mail.send(msg)
    except Exception as e:
        app.logger.error(str(e))
