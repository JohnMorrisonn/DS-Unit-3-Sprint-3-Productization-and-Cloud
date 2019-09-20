"""OpenAQ Air Quality Dashboard with Flask."""
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from aq_app import openaq
from aq_app import APP, DB

# Set the api
api = openaq.OpenAQ()

# function to pull pm25 air values with utc date per city
def get_pm25(api, city):
    measurements = api.measurements(city=city, parameter='pm25')
    results = measurements[1]['results']
    values = []
    for i in range(len(results)):
        utc = results[i]['date']['utc']
        value = results[i]['value']
        values.append((utc, value))
    return values


# function to add new records to DB
def add_current_record(api, city):
    measurements = api.measurements(city=city, parameter='pm25')
    results = measurements[1]['results']
    for i in range(len(results)):
        utc = results[i]['date']['utc']
        value = results[i]['value']
        new_record = Record(datetime=str(utc), value=str(value))
        DB.session.add(new_record)



# root currently displays filtered value lists
@APP.route('/')
def root():
    print('Something here')
    filter_1 = Record.query.filter(Record.value > 10).all()
    filter_2 = Record.query.filter(Record.value < 2.5).all()
    return render_template('record.html', filter_1=filter_1, filter_2=filter_2)

# raw file from Part 2
@APP.route('/raw')
def raw():
    return str(get_pm25(api, 'Los Angeles'))

# refresh data
@APP.route('/refresh')
def refresh():
    DB.drop_all()
    DB.create_all()
    add_current_record(api, 'Los Angeles')
    DB.session.commit()
    return ('Data Refreshed!')


class Record(DB.Model):
    id = DB.Column(DB.Integer, primary_key=True)
    datetime = DB.Column(DB.String(25))
    value = DB.Column(DB.Float, nullable=False)

    def __repr__(self):
        return '<Time {}, Value {}'.format(self.datetime, self.value)



