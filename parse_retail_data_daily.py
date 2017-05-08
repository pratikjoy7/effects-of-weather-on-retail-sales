import argparse
import csv
import os
import datetime
import re

def main(file, list, product_name):
	products = []

	if product_name is not None:
		generate_regression_data(file, product_name)
	else:
		with open(list, 'r+') as list_file:
			products = list_file.readlines()
	
		for product in products:
			generate_regression_data(file, product)


def generate_regression_data(file, product):
	header_exists = False
	product_quantity = 0
	current_date = None
	product = product.strip()
	file_name = 'regression-dataset/daily/' + product.replace(' ', '-').replace('/', '-').lower() + '.csv'
	with open(file, 'r+') as raw_file:
		reader = csv.reader(raw_file)
		for retail_row in reader:
			if retail_row[2] == 'Description':
				continue
			if product == retail_row[2].strip():
				month,day,year = retail_row[4].split()[0].split('/')
				date = '20%s-%s-%s' % (year,month,day)
				try:
					# Check if directory and file for placing the dataset exists, create if doesn't
					if not os.path.exists('regression-dataset/daily/'):
						os.makedirs('regression-dataset/daily/')
					open(file_name, 'a').close()
					# Check whether header exists in file, create if doesn't
					with open(file_name, 'r') as parsed_file:
						reader = csv.reader(parsed_file)
						for parsed_row in reader:
							if parsed_row[0] == 'date':
								header_exists = True
								break
					if header_exists == False:
						with open(file_name, 'a') as read_file:	
							writer = csv.writer(read_file, dialect='excel')
							writer.writerow(['date', 'quantity', 'temperature', 'humidity', 'visibility', 'wind_speed', 'condition'])

					if current_date == date:
							product_quantity = product_quantity + int(retail_row[3])

					elif current_date != date:
						with open('weather-data-daily-uk.csv', 'r+') as weather_file:
							reader = csv.reader(weather_file)
							for weather_row in reader:
								if weather_row[0] == date:
									write_rows(file_name, [date, product_quantity, weather_row[1], weather_row[2], weather_row[3], weather_row[4], weather_row[5]])
						product_quantity = 0
						current_date = date
				except ValueError:
					continue
		with open('weather-data-daily-uk.csv', 'r+') as weather_file:
			reader = csv.reader(weather_file)
			for row in reader:
				if row[0] == date:
					write_rows(file_name, [date, product_quantity, row[1], row[2], row[3], row[4], row[5]])


def write_rows(file, data):
	with open(file, 'a+') as parsed_file:
		writer = csv.writer(parsed_file, dialect='excel')
		writer.writerow(data)


if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='This script is intended to parse a csv file of weather data and extract useful information')
	parser.add_argument('--product', nargs='?', help='Specify the product for which regression dataset needs to be prepared')
	args = parser.parse_args()
	main('retail-data-uk.csv', 'product-list.txt', args.product)
