import argparse
import csv
import os
import glob


def main(dir):
	header_exists = False
	daily_weather_file = '../../weather-data-daily-uk.csv'
	os.chdir(dir)
	for file in glob.glob("*.csv"):
		print 'Reading: ' + file
		# Check whether header exists in file, create if doesn't
		if not os.path.exists(daily_weather_file):
			open(daily_weather_file, 'a').close()
		with open(daily_weather_file, 'r') as read_file:
			reader = csv.reader(read_file)
			for row in reader:
				if row[0] == 'date':
					header_exists = True
					break
		if header_exists == False:
			with open(daily_weather_file, 'a') as write_file:	
				writer = csv.writer(write_file, dialect='excel')
				writer.writerow(['date', 'temperature', 'humidity', 'visibility', 'wind_speed', 'condition'])

		with open(file, 'r+') as weather_file:
			reader = csv.reader(weather_file)
			print 'Writing in progress...\n'
			for row in reader:
				if row[0] in ('GMT', 'BST'):
					continue
				try:
					date = row[0]
					temperature = row[2]
					humidity = row[8]
					visibility = row[14]
					wind_speed = row[17]
					event = filter(str.isalpha, row[21]).lower()
					if event in ('lightsnow', 'lowdriftingsnow', 'snow'):
						condition = 0
					elif event in ('lightfreezingfog', 'haze', 'mist', 'fog'):
						condition = 0.2
					elif event in ('mostlycloudy', 'scatteredclouds', 'partlycloudy'):
						condition = 0.4
					elif event in ('lightdrizzle', 'lightrain', 'rain'):
						condition = 0.6
					elif event == 'clear':
						condition = 0.8
					else:
						condition = 1
				except ValueError:
					print 'ValueError occurred! Skipping row...'
					continue
				write_rows(daily_weather_file, [date, temperature, humidity, visibility, wind_speed, condition])
	print 'Done!\n'


def write_rows(file, data):
	with open(file, 'a+') as parsed_file:
		writer = csv.writer(parsed_file, dialect='excel')
		writer.writerow(data)


if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='This script is intended to parse a csv file of weather data and extract useful information')
	parser.add_argument('--dir', help='Specify the directory of the weather files that are needed to be parsed')
	args = parser.parse_args()
	main(args.dir)
