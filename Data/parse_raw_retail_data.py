import argparse
import csv
import os

def main(file):
	with open(file, 'r+') as raw_file:
		reader = csv.reader(raw_file)
		for row in reader:
			description = row[2]
			quantity = row[3]
			invoice_date = row[4]
			unit_price = row[5]
			unique_id = row[8]

			date = invoice_date.split()[0]
			formatted_date = '20%02d-%02d-%02d' % (int(date.split('/')[2]), int(date.split('/')[0]), int(date.split('/')[1]))
			
			time = invoice_date.split()[1]
			formatted_time = '00:00:00'

			parsed_retail_data = [unique_id, invoice_date, description, quantity, unit_price, formatted_date, formatted_time]

			if not os.path.exists('parsed'):
				os.makedirs('parsed')
			open('parsed/parsed_retail_data.txt', 'a').close()

			if row[2] == 'Description':
				continue
			else:
				write_rows('parsed/parsed_retail_data.txt', parsed_retail_data)

def write_rows(filename, data):
	with open(filename, 'a+') as parsed_file:
		writer = csv.writer(parsed_file, dialect='excel')
		writer.writerow(data)

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='This script is intended to parse a csv file of weather data and extract useful information')
	parser.add_argument('--file', help='Specify the filename that needs to be parsed')
	args = parser.parse_args()
	main(args.file)