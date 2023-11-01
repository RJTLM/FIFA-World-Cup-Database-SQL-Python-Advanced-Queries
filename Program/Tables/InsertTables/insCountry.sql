/* insCountry.sql: MySQL file for inserting data into the Country table */

-- Load data from CSV file into Country table
LOAD DATA INFILE ./Program/bigDataCleaned.csv
INTO TABLE Country
FIELDS TERMINATED BY ',' -- or whatever your delimiter is
ENCLOSED BY '"' -- or whatever your text qualifier is
LINES TERMINATED BY '\n'
IGNORE 1 LINES -- if your CSV file has a header row
(EventHost)
SET CountryName = EventHost;
