import bs4
import requests
data_url = "https://www.tdcj.state.tx.us/death_row/dr_scheduled_executions.html"
response = requests.get(data_url)
soup = bs4.BeautifulSoup(response.text)
link = soup.select("td")[0]
print(link.text)
06/18/2015
import time
from datetime import date
today = date.today()
print today
2015-06-08
execution = date(today.year, 6, 18)
time_to_execution = abs(execution - today)
time_to_execution
Out[123]: datetime.timedelta(10)