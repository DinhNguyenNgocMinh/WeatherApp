from extract import get_weather
import pandas as pd
from datetime import date

df = pd.DataFrame(get_weather()['hourly'])

# Split column
df[['Date', 'Time']] = df['time'].str.split('T',n=2,expand=True)

# Clearer time
df['Time'] = df['Time'].apply(lambda x: str(x))
df['Time'] = df['Time'].apply(lambda x: x[0:2])


# Set id
df['time'] = df['time'].apply(lambda x: str(x))
df['time'] = df['time'].apply(lambda x: x[8:10] + x[5:7] + x[2:4] + x[11:13])

# Rename
df.rename(columns={
    'time':'id',
    'temperature_2m':'Temperature'
}, inplace=True)

# Change dtype
df = df.astype({
    'Date': str
})

# Set index
# df.set_index('id', inplace=True)

# Group
df.groupby(['Date', 'Time'])

today=date.today()
def get_temperature(date=today):
    return df[df['Date'].str.contains(str(date))]