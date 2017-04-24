import argparse
import csv
import os

def main(file):
	file_ext = file.split('/')[0]
	with open(file, 'r+') as raw_file:
		reader = csv.reader(raw_file)
		for row in reader:
			if row[13] == 'DateUTC':
				continue
			else:
				date_time = row[13]
				date,time = date_time.split()
				humidity = row[3]
				visibility = row[5]
				wind_speed = row[7]
				condition = row[11]

				date_time_vs_humidity = [date, time, humidity]
				date_time_vs_visibility = [date, time, visibility]
				date_time_vs_condition = [date, time, wind_speed]
				date_time_vs_condition = [date, time, condition]

				if not os.path.exists('parsed'):
					os.makedirs('parsed')
				open('parsed/date_time_vs_humidity_' + file_ext + '.txt', 'a').close()
				open('parsed/date_time_vs_visibility_' + file_ext + '.txt', 'a').close()
				open('parsed/date_time_vs_wind_speed_' + file_ext + '.txt', 'a').close()
				open('parsed/date_time_vs_condition_' + file_ext + '.txt', 'a').close()

				write_rows('parsed/date_time_vs_humidity_' + file_ext + '.txt', date_time_vs_humidity)
				write_rows('parsed/date_time_vs_visibility_' + file_ext + '.txt', date_time_vs_visibility)
				write_rows('parsed/date_time_vs_wind_speed_' + file_ext + '.txt', date_time_vs_condition)
				write_rows('parsed/date_time_vs_condition_' + file_ext + '.txt', date_time_vs_condition)

def write_rows(filename, data):
	with open(filename, 'a+') as parsed_file:
		writer = csv.writer(parsed_file, dialect='excel')
		writer.writerow(data)

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='This script is intended to parse a csv file of weather data and extract useful information')
	parser.add_argument('--file', help='Specify the filename that needs to be parsed')
	args = parser.parse_args()
	main(args.file)