from flask import Blueprint, render_template, request, flash, session, redirect, url_for
from scripts.calorie_calculator import *
from scripts.meal_planner import *
from scripts.emailer import *

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        age = request.form.get('age')
        sex = request.form.get('sex')
        feet = request.form.get('feet')
        inches = request.form.get('inches')
        weight = request.form.get('weight')
        activity = request.form.get('activity')
        goal = request.form.get('goal')
        
        # verify input
        if int(age) <= 18:
            flash('You must be 18 years old or older to use this website.', 
                  category='error')
        elif int(feet) <= 0 or int(inches) <= 0:
            flash('Please enter a valid height.', category='error')
        elif int(weight) <= 0:
            flash('Please enter a valid weight.', category='error')
        else:
            calorie_calculator = CalorieCalculator(age=int(age), 
                                                   sex=sex, 
                                                   feet=int(feet), 
                                                   inches=int(inches), 
                                                   weight=int(weight), 
                                                   activity_level=activity, 
                                                   goal=goal)
            
            session["calories"] = calorie_calculator.calories
            return redirect("/meal_plan", code=302)

    return render_template("home.html")

@views.route('/meal_plan', methods=['GET', 'POST'])
def meal_plan():
    if request.method == 'GET':
        global meal_planner
        meal_planner = MealPlanner(session["calories"])
    return render_template("meal_plan.html", 
                           meals = meal_planner.get_meal_plan())

@views.route('/contact_me', methods=['GET', 'POST'])
def contact_me():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        number = request.form.get('number')
        subject = request.form.get('subject')
        body = request.form.get('body')
        method = request.form.getlist('method')
        if number:
            if len(number) < 9:
                flash('Please enter a valid phone number.', category='error')
                return render_template("contact_me.html")
        
        if '@' not in email or '.' not in email:
            flash('Please enter a valid email.', category='error')
        else:
            emailer = Emailer(name, email, number, subject, body, method)
            emailer.send_email()
            flash("""Message sent! I will respond via your preferred method as 
                     soon as possible.""", 
                  category='success')
    return render_template("contact_me.html")