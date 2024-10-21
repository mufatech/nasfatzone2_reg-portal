from flask import render_template
from app import app, db
from flask_login import login_required
from app.models.user import User
from sqlalchemy import func

@app.route('/user_analytics', methods=['GET'])
@login_required  # Use login_required to ensure only logged-in admins can access this page
def user_analytics():
    # Calculate total users registered
    total_users_registered = db.session.query(func.count(User.id)).scalar()

    # Calculate percentages
    total_female_users = db.session.query(func.count(User.id)).filter(User.gender == 'Female').scalar()
    total_male_users = db.session.query(func.count(User.id)).filter(User.gender == 'Male').scalar()
    total_zone_2_users = db.session.query(func.count(User.id)).filter(User.zone == 'Zone 2').scalar()
    total_zone_3_users = db.session.query(func.count(User.id)).filter(User.zone == 'Zone 3').scalar()
    total_teens_users = db.session.query(func.count(User.id)).filter(User.category == 'teens').scalar()
    total_children_users = db.session.query(func.count(User.id)).filter(User.category == 'children').scalar()
    total_adults_users = db.session.query(func.count(User.id)).filter(User.category == 'adults').scalar()

    percentage_total_users = 100  # Calculate the total percentage

    percentage_female_users = round((total_female_users / total_users_registered) * 100, 1)
    percentage_male_users = round((total_male_users / total_users_registered) * 100, 1)
    percentage_zone_2_users = round((total_zone_2_users / total_users_registered) * 100, 1)
    percentage_zone_3_users = round((total_zone_3_users / total_users_registered) * 100, 1)
    percentage_teens_users = round((total_teens_users / total_users_registered) * 100, 1)
    percentage_children_users = round((total_children_users / total_users_registered) * 100, 1)
    percentage_adults_users = round((total_adults_users / total_users_registered) * 100, 1)


    return render_template('admin/user_analytics.html', 
                           total_users_registered=total_users_registered,
                           percentage_total_users=percentage_total_users,
                           total_female_users=total_female_users,
                           total_male_users=total_male_users,
                           total_zone_2_users=total_zone_2_users,
                           total_zone_3_users=total_zone_3_users,
                           total_teens_users=total_teens_users,
                           total_children_users=total_children_users,
                           total_adults_users=total_adults_users,
                           percentage_female_users=percentage_female_users,
                           percentage_male_users=percentage_male_users,
                           percentage_zone_2_users=percentage_zone_2_users,
                           percentage_zone_3_users=percentage_zone_3_users,
                           percentage_teens_users=percentage_teens_users,
                           percentage_children_users=percentage_children_users,
                           percentage_adults_users=percentage_adults_users)
