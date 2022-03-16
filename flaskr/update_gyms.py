from bs4 import BeautifulSoup
import requests
from .models import Gym, db
from flask import render_template
from geopy.geocoders import Nominatim

from flask import Blueprint

bp = Blueprint("gyms", __name__)


def get_states():
    html_request = requests.get("https://www.indoorclimbing.com/worldgyms.html")
    html_doc = html_request.text
    soup = BeautifulSoup(html_doc, "html.parser")
    divs = soup.find_all("div", "i")
    states = divs[1]("a")
    state_list = []
    for state in states[:50]:
        state_list.append(state.get("href"))
    return state_list


def get_zip(string):
    geolocator = Nominatim(user_agent="climbr")
    location = geolocator.geocode(string)
    location_data = location.address.split()
    zipcode = location_data[-3]
    return zipcode


def separate_address(string):
    address_list = string.split(", ")
    if len(address_list) != 3:
        return 0, 0, 0, 0
    street = address_list[0]
    city = address_list[1]
    state_zip = address_list[2].split()
    if len(state_zip) == 3:
        state = state_zip[0] + " " + state_zip[1]
        zipcode = state_zip[-1]
    else:
        state = state_zip[0]
        if len(state_zip) == 1:
            zipcode = 0
        else:
            zipcode = state_zip[1]
    return street, city, state, zipcode


def states_gyms(state_html):
    base_url = "https://www.indoorclimbing.com/"
    html_request = requests.get(base_url + state_html)
    soup = BeautifulSoup(html_request.text, "html.parser")
    gyms_html = soup("p")
    gym_list = []
    for gym in gyms_html:
        gym_text = gym.get_text(strip=True, separator="\n").splitlines()
        print(gym_text)
        if len(gym_text) < 3 or len(gym_text[2]) > 14:
            continue
        name = gym_text[0]
        address = gym_text[1]
        phone = gym_text[2]
        street, city, state, zipcode = separate_address(address)
        if zipcode == 0:
            continue
        gym_list.append(Gym(name, street, city, state, zipcode, phone))
    return gym_list


@bp.route("/update")
def update_gyms():
    states = get_states()
    for state in states:
        gym_list = states_gyms(state)
        for gym in gym_list:
            db.session.add(gym)
    db.session.commit()
    return render_template("update_gyms.html")
