import time
import datetime

today_is = datetime.datetime.now()
formatted_date = today_is.strftime("%b %d %Y")
epoch = time.time()

print(f"Seconds since January 1, 1970: {epoch:,.4f} or "
      f"{epoch:.2e} in scientific notation")
print(f"{formatted_date}")
