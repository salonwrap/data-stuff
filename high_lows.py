import csv
from datetime import datetime as d 
from matplotlib import pyplot as plt 

#Get dates, high and low temperatures from file

filename = 'death_valley_2014.csv'

with open(filename) as f:
	reader = csv.reader(f)
	header_row = next(reader)
#	print(header_row)


#for index, column_header in enumerate(header_row):
#	print(index, column_header)

#	highs = []
#	dates = []
#	lows  = []

	dates, highs, lows = [], [], []
	for row in reader:
		try:
			current_date = d.strptime(row[0], '%Y-%m-%d')
			high = int(row[1])
			low = int(row[3])
		except ValueError:
			print(current_date, 'missing data')
		else:
			dates.append(current_date)
			highs.append(high)
			lows.append(low)
#			print(dates)


# Plot data

fig = plt.figure(dpi= 80, figsize=(10,6))
plt.plot(dates, highs, c = 'red', alpha=0.5)
plt.plot(dates, lows, c = 'blue', alpha=0.5)
plt.fill_between(dates,highs,lows, facecolor = 'blue', alpha =0.1)


#Format plot
plt.title('Daily high and low temperature, 2014\nDeath Valley, CA', 
	fontsize= 18)
plt.xlabel('', fontsize=10)
fig.autofmt_xdate()
plt.ylabel('Temperature (F)', fontsize=10)
plt.tick_params(axis='both',which='major',labelsize=10)

plt.savefig('death_valley.png')






