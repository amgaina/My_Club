from django.shortcuts import render
import calendar
from calendar import HTMLCalendar
from datetime import datetime

# Create your views here.
def home(request, month, year):
    name = "Abhishek"
    month = month.capitalize()
    month_number = list(calendar.month_name).index(month)
    month_number = int(month_number)
    now = datetime.now()
    current_year = now.year
    time = now.strftime("%I:%M %p")
    # create a calendar
    cal = HTMLCalendar().formatmonth(year, month_number)

    return render(request, "home.html", {
        "name": name,
        "month": month,
        "year": year,
        "cal": cal,
        "current_year": current_year,
        "current_time":time
    })