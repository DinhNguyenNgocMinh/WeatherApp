from transform import get_temperature
import matplotlib.pyplot as plt
from datetime import date

today = date.today()
day = today.day
month = today.month
year = today.year

def choose_day(d,m,y):

    print("<<< SELECT THE DAY IN RANGE OF TODAY AND MAXIMUM 6 DAYS LATER >>>")
    day = str(input(f"Day (Leave BLANK for {d}): "))
    month = str(input(f"Month (Leave BLANK for {m}): "))
    year = str(input(f"Year: (Leave BLANK for {y}): "))

    return f"{year if year != '' else y}-{month if month != '' else m}-{day if day != '' else d}"

selected_day = choose_day(day, month, year)
df = get_temperature(selected_day)

print(df)

x = df['Time']
y = df['Temperature']


print(plt.style.available)
plt.style.use('Solarize_Light2')
plt.title(selected_day)
plt.xlabel('Hour')
plt.ylabel('Temperature')
plt.plot(x, y)
plt.show()


