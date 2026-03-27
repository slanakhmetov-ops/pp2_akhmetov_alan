#1 Write a Python program to subtract five days from current date.
from datetime import date, timedelta
print (date.today() - timedelta(days = 5))

#2 Write a Python program to print yesterday, today, tomorrow.
from datetime import date, timedelta
print ("Yesterday date was: ", date.today() - timedelta(days=1))
print ("Today's date is: ", date.today())
print ("Tomorrow date will be: ", date.today() + timedelta(days=1))

#3 Write a Python program to drop microseconds from datetime.
from datetime import datetime 
now = datetime.now()
no_microseconds = now.replace(microsecond=0)
print (no_microseconds)

#4 Write a Python program to calculate two date difference in seconds.
from datetime import datetime
from datetime import datetime
date_str1 = input("Enter the first date like 'YYYY-MM-DD HH:MM:SS': ")
date_str2 = input("Enter the second date like 'YYYY-MM-DD HH:MM:SS': ")
date1 = datetime.strptime(date_str1, "%Y-%m-%d %H:%M:%S")
date2 = datetime.strptime(date_str2, "%Y-%m-%d %H:%M:%S")
diff = date1 - date2
seconds = diff.total_seconds()
print("Difference in seconds is: ", seconds)