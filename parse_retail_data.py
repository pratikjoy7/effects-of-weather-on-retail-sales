import argparse
import csv
import os
import datetime
import re

def main(file, list):
	first_week = None
	second_week = None
	third_week = None
	fourth_week = None
	products = []
	header_exists = False
	product_quantity = [0, 0, 0, 0]
	current_month = 'december'
	week_count = 1
	with open(list, 'r+') as list_file:
		products = list_file.readlines()
	for product in products:
		product = product.strip()
		file_name = 'regression-dataset/' + product.replace(' ', '-').replace('/', '-').lower() + '.csv'
		with open(file, 'r+') as raw_file:
			reader = csv.reader(raw_file)
			for row in reader:
				if row[2] == 'Description':
					continue
				if product == row[2].strip():
					month,day,year = row[4].split()[0].split('/')

					try:
						month = datetime.date(int('20' + year), int(month), int(day)).strftime('%B').lower()
						# Check if directory and file for placing the dataset exists, create if doesn't
						if not os.path.exists('regression-dataset'):
							os.makedirs('regression-dataset')
						open(file_name, 'a').close()
						# Check whether header exists in file, create if doesn't
						with open(file_name, 'r') as retail_file:
							reader = csv.reader(retail_file)
							for row in reader:
								if row[0] == 'week':
									header_exists = True
									break
						if header_exists == False:
							with open(file_name, 'a') as read_file:	
								writer = csv.writer(read_file, dialect='excel')
								writer.writerow(['week', 'quantity', 'temperature', 'humidity', 'visibility', 'wind_speed', 'condition'])

						if current_month == month:
							first_week = '%s-20%s_1-7' % (month, year)
							second_week = '%s-20%s_8-14' % (month, year)
							third_week = '%s-20%s_15-21' % (month, year)
							fourth_week = '%s-20%s_22-28' % (month, year)
							if 1 <= int(day) <= 7:
								product_quantity[0] = product_quantity[0] + int(row[3])
							elif 8 <= int(day) <= 14:
								product_quantity[1] = product_quantity[1] + int(row[3])
							elif 15 <= int(day) <= 21:
								product_quantity[2] = product_quantity[2] + int(row[3])
							elif 22 <= int(day) <= 28:
								product_quantity[3] = product_quantity[3] + int(row[3])
							else:
								pass

						elif current_month != month:
							with open('weather-data-uk.csv', 'r+') as weather_file:
								reader = csv.reader(weather_file)
								for row in reader:
									if row[0] == first_week:
										write_rows(file_name, [week_count, product_quantity[0], row[1], row[2], row[3], row[4], row[5]])
										week_count = increase_week_count(week_count, file_name, current_file_name)
									elif row[0] == second_week:
										write_rows(file_name, [week_count, product_quantity[1], row[1], row[2], row[3], row[4], row[5]])
										week_count += 1
									elif row[0] == third_week:
										write_rows(file_name, [week_count, product_quantity[2], row[1], row[2], row[3], row[4], row[5]])
										week_count += 1
									elif row[0] == fourth_week:
										write_rows(file_name, [week_count, product_quantity[3], row[1], row[2], row[3], row[4], row[5]])
										week_count += 1
									else:
										pass
							product_quantity = [0, 0, 0, 0]
							current_month = month
							current_file_name = file_name
					except ValueError:
						continue
			with open('weather-data-uk.csv', 'r+') as weather_file:
				reader = csv.reader(weather_file)
				for row in reader:
					if row[0] == first_week:
						write_rows(file_name, [week_count, product_quantity[0], row[1], row[2], row[3], row[4], row[5]])
						week_count += 1
					elif row[0] == second_week:
						write_rows(file_name, [week_count, product_quantity[1], row[1], row[2], row[3], row[4], row[5]])
						week_count += 1
					elif row[0] == third_week:
						write_rows(file_name, [week_count, product_quantity[2], row[1], row[2], row[3], row[4], row[5]])
						week_count += 1
					elif row[0] == fourth_week:
						write_rows(file_name, [week_count, product_quantity[3], row[1], row[2], row[3], row[4], row[5]])
						week_count += 1
					else:
						pass


def increase_week_count(week_count, file_name, current_file_name):
	if current_file_name == file_name:
		week_count += 1
		return week_count
	else:
		week_count = 0
		return week_count

def write_rows(file, data):
	with open(file, 'a+') as parsed_file:
		writer = csv.writer(parsed_file, dialect='excel')
		writer.writerow(data)


if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='This script is intended to parse a csv file of weather data and extract useful information')
	main('retail-data-uk.csv', 'product-list.txt')
