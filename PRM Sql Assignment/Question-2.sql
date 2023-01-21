#Q.2 - Write a SQL statement to create the duplicate of the countries table named country_new with all structure and data.

CREATE TABLE  country_new AS SELECT * FROM  countries;

describe country_new;