import pandas as pd
import csv
import requests
from io import StringIO
response = requests.get("https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/02_Filtering_%26_Sorting/Euro12/Euro_2012_stats_TEAM.csv")

csv_data = StringIO(response.text)
# reader = csv.reader(csv_data)
# print(reader)
df = pd.read_csv(csv_data)

my_columns = ["Team", "Yellow Cards", "Red Cards"]
df[my_columns]
df["Team"].count()
#print(df[my_columns])
#print(df["Team"].count())
print(df["Team"][df["Goals"] >= 6])