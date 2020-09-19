------------------------------------------------------------------------------------------
FILES
------------------------------------------------------------------------------------------

readme.txt
	this file, which describes its neighbors


Project 4 v01.html
	HTML version of main project document; file describing the documentation of my data wrangling process in order to answer the rubric requirements
	
Project 4 v01.pdf
	PDF version of main project document; file describing the documentation of my data wrangling process in order to answer the rubric requirements
		
austin.osm
	original data from from openstreetmap.org

example.osm
	sample of austin.osm data

map_position_link.txt
	link to the map position I chose, and the reason why

resources.txt
	list of sites, forums, posts, repos, etc used when researching for this project
	
make_example.py
	python script for creating a file with a sample of the complete openstreetmap data (edit of original script provided by Udacity)

audit.py
	script used for ad hoc review prior to actual analysis

schema.py
	Udacity file containing data schema. super helpful

streetnames.py
	used to assess and clean street types/names
	
zipcodes.py
	used to trim suffix from long zip codes
	
heights.py
	used to clean string values from height-key value tags

data.py
	primary program reading source data, cleaning it via streetnames.py, and writing cleaned results to csv

db.py
	program to create sqlite database schema and populate from csv