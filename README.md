# Effect of weather on retail sales
Thesis project on datamining to determine the effects of weather on retail sales.
This repo is dedicated to hosting the dataset and the scirpts necessary to prepare the dataset for doing the analysis

**Requirements:**
   * python-2.7
   
**Commands:**
  * ***Generate factors by date data:***
    * bash run_script.sh ***weather-data-directory*** *[eg.: bash run_script.sh december-2010]*
  * ***Generate parsed retail data without any weather factors:***
  	* python parse_retail_data.py --file ***retail-data-file*** *[eg.: python parse_retail_data.py --file retail-data-uk.csv]*
  * ***Generate parsed retail data with weather factors:***
    * python prepare_regression_data.py --weather ***parsed-weather-file*** --retail ***parsed-retail-file*** *[eg.: python prepare_regression_data.py --weather parsed/date_time_vs_humidity_january-2011.txt --retail parsed/parsed_retail_data_2011-1.txt]*
