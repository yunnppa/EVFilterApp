from flask import Blueprint, request, render_template
from app.filters import EVFilter

main = Blueprint('main', __name__)
ev_filter = EVFilter('data/ev_data.csv')

@main.route("/", methods=["GET", "POST"])
def index():
    vehicles = []
    brand = ""
    if request.method == "POST":
        brand = request.form.get("brand")
        vehicles = ev_filter.filter_by_brand(brand)
    return render_template("index.html", vehicles=vehicles, brand=brand)
