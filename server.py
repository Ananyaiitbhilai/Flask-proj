"""Server file for Flightplan Travel app"""

from jinja2 import StrictUndefined
from flask import Flask, render_template, request, flash, redirect, session, jsonify
from flask_debugtoolbar import DebugToolbarExtension
from model import connect_to_db, db, City
import coverage
import doctest


app = Flask(__name__)

app.secret_key = "ABC"

app.jinja_env.undefined = StrictUndefined



@app.route('/')
def index():
    """Homepage."""

    return render_template("homepage.html")




@app.route('/city_page', methods=['GET', 'POST'])
def city():
    
    destination = request.form['destination']
    city = City.query.filter_by(destination=destination).first()
    return render_template("city_page.html", city=city)

@app.route('/city_event_page/<destination>', methods=['GET'])
def city_page(destination):
    """ event page for selected city"""
    destination = City.query.filter_by(destination=destination).first()
    return render_template("city_event_page.html", events=destination.events, city_event_destination=destination)





@app.route('/api', methods=['GET', 'POST'])
def api_page():
    """api page, allows user to make GET request, renders information in JSON format """
    return render_template("api.html")



cities = [
    {
        'id': 1,
        'name': u'New Delhi',
        'recomendation': u'Buy', 
        'estimated fare': 'Rs 7350',
        'lowest fare': 'Rs 4550'
    },
        {
        'id': 2,
        'name': u'Bhopal',
        'recomendation': u'Wait', 
        'estimated fare': 'Rs 5530',
        'lowest fare': 'Rs 3040'
    },
    {
        'id': 3,
        'name': u'Indore',
        'recomendation': u'Buy', 
        'estimated fare': 'Rs 5750',
        'lowest fare': 'Rs 4000'
    },
        {
        'id': 4,
        'name': u'Kolkata',
        'recomendation': u'Buy', 
        'estimated fare': 'Rs 6900',
        'lowest fare': 'Rs 4040'
    },
        {
        'id': 5,
        'name': u'Mumbai',
        'recomendation': u'Buy', 
        'estimated fare': 'Rs 6500',
        'lowest fare': 'Rs 4200'
    },
        {
        'id': 6,
        'name': u'Guwahati',
        'recomendation': u'Wait', 
        'estimated fare': 'Rs 5000',
        'lowest fare': 'Rs 4000'
    },
        {
        'id': 7,
        'name': u'Vishakhapatnam',
        'recomendation': u'Buy', 
        'estimated fare': 'Rs 3000',
        'lowest fare': 'Rs 2000'
    },
        {
        'id': 8,
        'name': u'Pune',
        'recomendation': u'Buy', 
        'estimated fare': 'Rs 6500',
        'lowest fare': 'Rs 4100'
    },
        {
        'id': 9,
        'name': u'Banglore',
        'recomendation': u'Buy', 
        'estimated fare': 'Rs 2000',
        'lowest fare': 'Rs 1500'
    },
        {
        'id': 10,
        'name': u'Ahemdabad',
        'recomendation': u'Wait', 
        'estimated fare': 'Rs 3000',
        'lowest fare': 'Rs 2560'
    },
        {
        'id': 11,
        'name': u'Surat',
        'recomendation': u'Buy', 
        'estimated fare': 'Rs 3000',
        'lowest fare': 'Rs 2540'
    },
        {
        'id': 12,
        'name': u'Lucknow',
        'recomendation': u'Wait', 
        'estimated fare': 'Rs 4060',
        'lowest fare': 'Rs 3000'
    },
        {
        'id': 13,
        'name': u'Bhubaneshwar',
        'recomendation': u'Wait', 
        'estimated fare': 'Rs 3200',
        'lowest fare': 'Rs 1500'
    },
        {
        'id': 14,
        'name': u'Dehradun',
        'recomendation': u'Buy', 
        'estimated fare': 'Rs 5000',
        'lowest fare': 'Rs 4000'
    },
        {
        'id': 15,
        'name': u'Jammu',
        'recomendation': u'Buy', 
        'estimated fare': 'Rs 7500',
        'lowest fare': 'Rs 5000'
    },
        {
        'id': 16,
        'name': u'Shimla',
        'recomendation': u'Buy', 
        'estimated fare': 'Rs 7500',
        'lowest fare': 'Rs 5500'
    },
        {
        'id': 17,
        'name': u'Chandigarh',
        'recomendation': u'Buy', 
        'estimated fare': 'Rs 6000',
        'lowest fare': 'Rs 4200'
    },
        {
        'id': 18,
        'name': u'Raipur',
        'recomendation': u'Buy', 
        'estimated fare': 'Rs 3000',
        'lowest fare': 'Rs 1500'
    },
        {
        'id': 19,
        'name': u'Ranchi',
        'recomendation': u'Wait', 
        'estimated fare': 'Rs 4000',
        'lowest fare': 'Rs 3200'
    },
        {
        'id': 20,
        'name': u'Hyderabad',
        'recomendation': u'Wait', 
        'estimated fare': 'Rs 1000',
        'lowest fare': 'Rs 570'
    },
        {
        'id': 21,
        'name': u'Chennai',
        'recomendation': u'Buy', 
        'estimated fare': 'Rs 800',
        'lowest fare': 'Rs 420'
    },
        {
        'id': 22,
        'name': u'Panaji',
        'recomendation': u'Wait', 
        'estimated fare': 'Rs 3000',
        'lowest fare': 'Rs 1600'
    },
        {
        'id': 23,
        'name': u'Jaipur',
        'recomendation': u'Buy', 
        'estimated fare': 'Rs 4300',
        'lowest fare': 'Rs 3000'
    },
        {
        'id': 24,
        'name': u'Ladhak',
        'recomendation': u'Wait', 
        'estimated fare': 'Rs 7900',
        'lowest fare': 'Rs 6080'
    },
        {
        'id': 25,
        'name': u'Port Blair',
        'recomendation': u'', 
        'estimated fare': 'Rs 4000',
        'lowest fare': 'Rs 3300'
    },
]

@app.route('/api/v1.0/cities', methods=['GET', 'POST'])
def get_tasks():
    """ route for api call to all cities"""
    return jsonify({'cities': cities})


@app.route('/api/v1.0/cities/<int:city_id>', methods=['GET', 'POST'])
def get_task(city_id):
    """ route for api call to selected cities"""
    city = [city for city in cities if city['id'] == city_id]
    return jsonify({'city': city[0]})





if __name__ == "__main__":
   
    app.debug = True

    connect_to_db(app)

   
    DebugToolbarExtension(app)

    app.run(host='0.0.0.0')