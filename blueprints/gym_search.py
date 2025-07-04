from flask import Blueprint, render_template, request, current_app
from models.gym import GymModel
from extension import db
from forms.gym_search_form import GymSearchForm
from dotenv import load_dotenv
import googlemaps
import os
import requests

load_dotenv()
# Get the Google Maps API Key from the environment variable
api_key = os.getenv("GOOGLE_MAPS_API_KEY")

GOOGLE_PLACES_URL = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json'

gym_search = Blueprint("gym_search", __name__, url_prefix="/gym_search")

# Initialize Google Maps client
gmaps = googlemaps.Client(key=api_key)
def get_lat_lng_from_location(location):
    geocode_result = gmaps.geocode(location)
    if geocode_result:
        lat = geocode_result[0] ['geometry']['location']['lat']
        lng = geocode_result[0] ['geometry']['location']['lng']
        return lat,lng
    return None, None #Return None if the location couldn't be geocoded

@gym_search.route('/search_gyms', methods=['GET', 'POST'])
def search_gyms():
    form = GymSearchForm()
    query = GymModel.query
    if request.method == 'GET':
        location = request.args.get('location') or form.location.data 
        gyms = []
        for gym in query:
            gyms.append({"latitude": gym.lat, "longitude":gym.lng})
        if location:
            filtered_query = query.filter(GymModel.location.ilike(f"%{location.strip()}%"))
        # Perform the search for gyms based on the location
        # Call Google Maps API to get the gyms
        # Store gyms in the database
        # Return a result template
            lat, lng = get_lat_lng_from_location(location)
            if filtered_query.count() != 0:
                return render_template('search.html', api_key=api_key, form=form, location=location, gyms=filtered_query, lat=lat, lng=lng, formatted_gyms=gyms)
            else:
                return render_template('search.html', api_key=api_key, form=form, location=location, lat=lat, lng=lng, formatted_gyms=gyms, error="No gyms found or invalid location")
    return render_template('search.html', api_key=api_key, form=form, lat= 51.509865, lng= -0.118092, formatted_gyms=gyms)
