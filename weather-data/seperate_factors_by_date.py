import argparse
import csv
import os

def main(file):
	with open(file, 'r+') as raw_file:
		reader = csv.reader(raw_file)
		for row in reader:
			date_time = row[13]
			humidity = row[3]
			visibility = row[5]
			wind_speed = row[7]
			condition = row[11]

			date_time_vs_humidity = [date_time, humidity]
			date_time_vs_visibility = [date_time, visibility]
			date_time_vs_condition = [date_time, wind_speed]
			date_time_vs_condition = [date_time, condition]

			if not os.path.exists('../parsed'):
				os.makedirs('../parsed')
				open('../parsed/date_time_vs_humidity.txt', 'a').close()
				open('../parsed/date_time_vs_visibility.txt', 'a').close()
				open('../parsed/date_time_vs_wind_speed.txt', 'a').close()
				open('../parsed/date_time_vs_condition.txt', 'a').close()

			if row[13] == 'DateUTC':
				continue
			else:
				write_rows('../parsed/date_time_vs_humidity.txt', date_time_vs_humidity)
				write_rows('../parsed/date_time_vs_visibility.txt', date_time_vs_visibility)
				write_rows('../parsed/date_time_vs_wind_speed.txt', date_time_vs_condition)
				write_rows('../parsed/date_time_vs_condition.txt', date_time_vs_condition)

def write_rows(filename, data):
	with open(filename, 'a+') as parsed_file:
		writer = csv.writer(parsed_file, dialect='excel')
		writer.writerow(data)

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='This script is intended to parse a csv file of weather data and extract useful information')
	parser.add_argument('--file', help='Specify the filename that needs to be parsed')
	args = parser.parse_args()
	main(args.file)