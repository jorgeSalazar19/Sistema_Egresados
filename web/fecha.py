from datetime import datetime, date, time, timedelta
from dateutil.relativedelta import relativedelta

birthday = (date.today() - relativedelta(years=200))
limit = (date.today() - relativedelta(years=100))

if birthday < limit:
  print ("superaste el limite")
else:
  print("fecha en el limite")