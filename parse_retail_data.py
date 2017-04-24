import argparse
import csv
import os
from datetime import datetime
import re

def main(file):
	with open(file, 'r+') as raw_file:
		reader = csv.reader(raw_file)
		for row in reader:
			description = re.sub(' +',' ', re.sub(r"[^\w\s]", '', row[2]))
			quantity = row[3]
			invoice_date = row[4]
			unit_price = row[5]
			unique_id = row[8]

			if row[2] == 'Description':
				continue
			try:
				date,time = invoice_date.split()
				month = '20%s-%s' % (date.split('/')[2], date.split('/')[0])
				date = '20%02d-%02d-%02d' % (int(date.split('/')[2]), int(date.split('/')[0]), int(date.split('/')[1]))
				time = '%02d:%02d:00' % (int(time.split(':')[0]), int(time.split(':')[1]))
				invoice_date = '%s %s' % (date, time)

				parsed_retail_data = [unique_id, invoice_date, description, quantity, unit_price, date, time]

				if not os.path.exists('parsed'):
					os.makedirs('parsed')
				open('parsed/parsed_retail_data_' + month + '.txt', 'a').close()

				write_rows('parsed/parsed_retail_data_' + month + '.txt', parsed_retail_data)
			except ValueError:
				continue

def write_rows(filename, data):
	with open(filename, 'a+') as parsed_file:
		writer = csv.writer(parsed_file, dialect='excel')
		writer.writerow(data)

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='This script is intended to parse a csv file of weather data and extract useful information')
	parser.add_argument('--file', help='Specify the filename that needs to be parsed')
	args = parser.parse_args()
	main(args.file)