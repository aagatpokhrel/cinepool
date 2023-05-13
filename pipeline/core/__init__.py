import datetime

p_date = datetime.datetime.now()
date = p_date.strftime("%B %d, %Y")

b_date = p_date - datetime.timedelta(days=7)
b_date = b_date.strftime("%B %d, %Y")