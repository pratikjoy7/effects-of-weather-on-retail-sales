import argparse
import csv
import os
import datetime
import re
import sys

def main(weather_file, retail_file):
	file_ext = weather_file.split('_vs_')[1]
	with open(weather_file, 'r+') as file:
		weather_file_reader = csv.reader(file)
		for weather_row in weather_file_reader:
			weather_date = weather_row[0]
			try:
				time_range_start = datetime.datetime.strptime(weather_row[1], '%H:%M:%S')
				factor = weather_row[2]
				time_range_end = time_range_start + datetime.timedelta(minutes = 30)
			except ValueError:
				continue
			with open(retail_file, 'r+') as raw_file:
				retail_file_reader = csv.reader(raw_file)
				for retail_row in retail_file_reader:
					unique_id = retail_row[0]
					invoice_date = retail_row[1]
					product = retail_row[2]
					quantity = int(retail_row[3])
					unit_price = retail_row[4]
					date = retail_row[5]
					time = retail_row[6]
					
					if product not in (None, ''):
						if quantity > 0:
							if retail_row[2] == 'Description':
								continue
							try:
								time_obj = datetime.datetime.strptime(time, '%H:%M:%S')

								if date == weather_date:
									if time_range_start <= time_obj < time_range_end:
										regression_retail_data = [unique_id, invoice_date, product, quantity, unit_price, factor]

										if not os.path.exists('regression_dataset'):
											os.makedirs('regression_dataset')
										open('regression_dataset/regression_retail_data_vs_' + file_ext, 'a').close()

										write_rows('regression_dataset/regression_retail_data_vs_' + file_ext, regression_retail_data)
									else:
										continue
								else:
									continue
							except ValueError:
								continue

def write_rows(filename, data):
	with open(filename, 'a+') as regression_file:
		writer = csv.writer(regression_file, dialect='excel')
		writer.writerow(data)

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='This script is intended to parse a csv file of weather data and extract useful information')
	parser.add_argument('--weather', help='Specify the weather filename that needs to be parsed')
	parser.add_argument('--retail', help='Specify the retail data filename that needs to be parsed')
	args = parser.parse_args()
	main(args.weather, args.retail)
