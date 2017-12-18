#Django-FullCalendar Integration
####Requirements: Django>=2.0
###USAGE::
>Go to path/calendar/ to add a schedule.
>Go to path/calendar/view/ to view the calendar.

>1. To integrate the calendar in your project, add the almanac_calendar directory in your app,
include it in your **INSTALLED_APPS**
>2. run **python manage.py makemigrations almanac_calendar and python manage.py migrate**
>3. Edit calendar.html which is for adding events and add CSS as per requirements.
>4. Edit index.html to modify it to a block so that you can include in other templates. 
