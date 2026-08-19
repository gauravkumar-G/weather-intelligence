from pathlib import Path

from datetime import date
import meteostat as ms

station = ms.Station(id='42105')
start = date(2020 , 1 , 1)
end = date(2025 , 8 , 22)

data = ms.daily(station , start , end)
data = data.fetch()

raw_dir = Path('data/raw')
raw_dir.mkdir(parents = True , exist_ok = True)

output_path = raw_dir / 'chd_weather_2020_2025.csv'
data.to_csv(output_path)
print(f"\nSaved raw data to : {output_path}")

if data is not None :
    print(data.head())
else :
    print('no data found for this date range')


print('\nShape : ')
print(data.shape)

print('\nColumns')
print(data.columns.tolist())

print('\nMissing Values :')
print(data.isna().sum())

print('\nDate Range :')
print(data.index.min() , '->' , data.index.max())

print('\nMissing percentages :')
print((data.isna().mean() * 100).round(2))

