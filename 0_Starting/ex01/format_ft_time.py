import time
from datetime import datetime

epoch_time = time.time()
date = datetime.now()

formatted_date = date.strftime("%b %d %Y")
print(f"Seconds since January 1, 1970: {epoch_time:,.4f} or {epoch_time:.2e} in scientific notation")
print(formatted_date)
