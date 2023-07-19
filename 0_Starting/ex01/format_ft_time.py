import time
from datetime import datetime

# time.time() returns the number of seconds since January 1, 1970
epoch_time = time.time()

# datetime.now() returns the current date and time
date = datetime.now()

# strftime() formats a date according to a format
# %b is the abbreviated month name
# %d is the day of the month
# %Y is the year
formatted_date = date.strftime("%b %d %Y")
# ,.4f formats a float with a comma as a thousands separator and 4 digits after the decimal point
# .2e formats a float in scientific notation with 2 digits after the decimal point
print(f"Seconds since January 1, 1970: {epoch_time:,.4f} or {epoch_time:.2e} in scientific notation")
print(formatted_date)
