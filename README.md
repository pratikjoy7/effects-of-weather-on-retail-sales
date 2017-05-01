# Effects of weather on retail sales
Thesis project on datamining to determine the effects of weather on retail sales.
This repo is dedicated to hosting the dataset and the scirpts necessary to prepare the dataset for doing the analysis

**Requirements:**
   * python-2.7
   * Git

**Getting Started:**
  * ***Install Git:***
    * Follow instructions: https://www.atlassian.com/git/tutorials/install-git
  * ***Install Python2.7:***
    * Follow instructions: https://www.python.org/downloads/windows/
  * ***Setting up the project:***
	* Launch **cmd** on windows or **terminal** of unix machinces
	* Change directory to wherever you want to keep the project
	* ***git clone git@github.com:pratikjoy7/effects-of-weather-on-retail-sales.git***
	* ***cd effects-of-weather-on-retail-sales/***
  * ***Rename and store raw weather data:***
    * Put the dataset inside "**weather-dataset**" directory
    * Rename the dataset like the following format:
      * **december-2010_1-7.csv** [*For first week's data*]
      * **december-2010_8-14.csv** [*For second week's data*]
      * **december-2010_15-21.csv** [*For third week's data*]
      * **december-2010_22-28.csv** [*For fourth week's data*]
      * ***Note: This example is for 4 weeks of december,2010. Rename for the month you want to parse accordingly***
    
**Commands:**
  * ***Parse weather data for generating regression analysis dataset:***
    * python parse_weather_data.py --file <***full-path-of-weather-data***>
      * **Example:** ***python parse_weather_data.py --file weather-dataset/december-2010/december-2010_1-7.csv***
  * ***Generate regression dataset from the weather data and the retail data:***
    * python parse_retail_data.py --product <***name-of-the-product-to-generate-regression-data***>
      * **Example:** ***python parse_retail_data.py --product "SET 2 TEA TOWELS I LOVE LONDON"*** 
      * *[In this example production name is "SET 2 TEA TOWELS I LOVE LONDON"]*