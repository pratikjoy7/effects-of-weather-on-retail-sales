import argparse
import csv
import os
import glob


def main(dir):
	header_exists = False
	os.chdir(dir)
	for file in glob.glob("*.csv"): 	
		week = file.split('.')[0]
		temperature = 0
		humidity = 0
		visibility = 0
		wind_speed = 0
		condition = 0
		
		# Check whether header exists in file, create if doesn't
		with open('../../weather-data-weekly-uk.csv', 'r') as read_file:
			reader = csv.reader(read_file)
			for row in reader:
				if row[0] == 'date':
					header_exists = True
					break
		if header_exists == False:
			with open('../../weather-data-weekly-uk.csv', 'a') as write_file:	
				writer = csv.writer(write_file, dialect='excel')
				writer.writerow(['week', 'temperature', 'humidity', 'visibility', 'wind_speed', 'condition'])

		with open(file, 'r+') as weather_file:
			reader = csv.reader(weather_file)
			for row in reader:
				if row[0] == 'GMT':
					continue
				try:
					temperature = temperature + int(row[2])
					humidity = humidity + int(row[8])
					visibility = visibility + int(row[14])
					wind_speed = wind_speed + int(row[17])
					event = filter(str.isalpha, row[21]).lower()
					if event in ('lightsnow', 'lowdriftingsnow', 'snow'):
						condition = condition + 0
					elif event in ('lightfreezingfog', 'haze', 'mist', 'fog'):
						condition = condition + 0.2
					elif event in ('mostlycloudy', 'scatteredclouds', 'partlycloudy'):
						condition = condition + 0.4
					elif event in ('lightdrizzle', 'lightrain', 'rain'):
						condition = condition + 0.6
					elif event == 'clear':
						condition = condition + 0.8
					else:
						condition = condition + 1
				except ValueError:
					continue
		write_rows('../../weather-data-weekly-uk.csv', [week, temperature/7, humidity/7, visibility/7, wind_speed/7, round(condition/7, 2)])


def write_rows(file, data):
	with open(file, 'a+') as parsed_file:
		writer = csv.writer(parsed_file, dialect='excel')
		writer.writerow(data)


if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='This script is intended to parse a csv file of weather data and extract useful information')
	parser.add_argument('--dir', help='Specify the directory of the weather files that are needed to be parsed')
	args = parser.parse_args()
	main(args.dir)
