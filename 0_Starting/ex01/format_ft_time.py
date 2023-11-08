import time
from datetime import datetime

# time.time() returns the number of seconds since January 1, 1970
epoch = time.time()

# datetime.now() returns the current date and time
date = datetime.now()

# strftime() formats a date according to a format
# %b is the abbreviated month name
# %d is the day of the month
# %Y is the year
formatted_date = date.strftime("%b %d %Y")
print(f"Seconds since January 1, 1970: {epoch:,.4f} or "
      f"{epoch:.2e} in scientific notation")
print(formatted_date)
