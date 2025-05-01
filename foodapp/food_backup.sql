
CREATE TABLE Texas_Counties (
    County_Name TEXT,
    "2019" REAL,
    "2020" REAL,
    "2021" REAL,
    "2022" REAL
);

CREATE TABLE texas_2019 (
    county_name TEXT PRIMARY KEY,
    food_insecurity REAL
);

CREATE TABLE texas_2020 (
    county_name TEXT PRIMARY KEY,
    food_insecurity REAL
);

CREATE TABLE texas_2021 (
    county_name TEXT PRIMARY KEY,
    food_insecurity REAL
);

CREATE TABLE texas_2022 (
    county_name TEXT PRIMARY KEY,
    food_insecurity REAL
);


INSERT INTO Texas_Counties (County_Name, "2019", "2020", "2021", "2022") VALUES
('Harris', 16.4, 13.8, 14.9, 13.9),
('Dallas', 15.6, 13.1, 14.2, 14.0),
('Tarrant', 14.2, 12.0, 13.1, 13.0),
('Bexar', 17.4, 14.0, 14.6, 13.9),
('Travis', 14.6, 11.9, 12.6, 12.8),
('Collin', 12.1, 10.1, 10.9, 11.1),
('Denton', 12.5, 10.2, 11.2, 11.3),
('Fort Bend', 11.1, 9.1, 10.2, 9.5),
('Hidalgo', 22.9, 19.0, 19.1, 18.0),
('El Paso', 19.4, 15.0, 15.1, 14.6),
('Montgomery', 13.8, 11.7, 12.5, 12.3),
('Williamson', 12.6, 10.1, 10.7, 11.0),
('Cameron', 21.9, 18.0, 17.9, 17.5),
('Brazoria', 12.9, 10.7, 11.6, 11.4),
('Bell', 16.6, 14.1, 15.1, 15.1),
('Galveston', 15.1, 13.1, 14.1, 14.1),
('Nueces', 18.7, 15.4, 15.2, 14.7),
('Lubbock', 17.0, 14.3, 14.9, 15.5),
('Hays', 14.7, 11.8, 12.0, 12.0),
('McLennan', 16.9, 14.4, 15.4, 15.7),
('Webb', 20.0, 16.0, 16.2, 15.8),
('Smith', 14.9, 12.9, 14.3, 14.8),
('Jefferson', 17.8, 16.6, 18.2, 16.6),
('Brazos', 17.1, 14.2, 15.0, 15.5),
('Ellis', 13.1, 10.4, 11.1, 11.5);

INSERT INTO texas_2019 (county_name, food_insecurity) VALUES
('Harris', 16.4),
('Dallas', 15.6),
('Tarrant', 14.2),
('Bexar', 17.4),
('Travis', 14.6),
('Collin', 12.1),
('Denton', 12.5),
('Fort Bend', 11.1),
('Hidalgo', 22.9),
('El Paso', 19.4),
('Montgomery', 13.8),
('Williamson', 12.6),
('Cameron', 21.9),
('Brazoria', 12.9),
('Bell', 16.6),
('Galveston', 15.1),
('Nueces', 18.7),
('Lubbock', 17.0),
('Hays', 14.7),
('McLennan', 16.9),
('Webb', 20.0),
('Smith', 14.9),
('Jefferson', 17.8),
('Brazos', 17.1),
('Ellis', 13.1);

INSERT INTO texas_2020 (county_name, food_insecurity) VALUES
('Harris', 13.8),
('Dallas', 13.1),
('Tarrant', 12.0),
('Bexar', 14.0),
('Travis', 11.9),
('Collin', 10.1),
('Denton', 10.2),
('Fort Bend', 9.1),
('Hidalgo', 19.0),
('El Paso', 15.0),
('Montgomery', 11.7),
('Williamson', 10.1),
('Cameron', 18.0),
('Brazoria', 10.7),
('Bell', 14.1),
('Galveston', 13.1),
('Nueces', 15.4),
('Lubbock', 14.3),
('Hays', 11.8),
('McLennan', 14.4),
('Webb', 16.0),
('Smith', 12.9),
('Jefferson', 16.6),
('Brazos', 14.2),
('Ellis', 10.4);

INSERT INTO texas_2021 (county_name, food_insecurity) VALUES
('Harris', 14.9),
('Dallas', 14.2),
('Tarrant', 13.1),
('Bexar', 14.6),
('Travis', 12.6),
('Collin', 10.9),
('Denton', 11.2),
('Fort Bend', 10.2),
('Hidalgo', 19.1),
('El Paso', 15.1),
('Montgomery', 12.5),
('Williamson', 10.7),
('Cameron', 17.9),
('Brazoria', 11.6),
('Bell', 15.1),
('Galveston', 14.1),
('Nueces', 15.2),
('Lubbock', 14.9),
('Hays', 12.0),
('McLennan', 15.4),
('Webb', 16.2),
('Smith', 14.3),
('Jefferson', 18.2),
('Brazos', 15.0),
('Ellis', 11.1);

INSERT INTO texas_2022 (county_name, food_insecurity) VALUES
('Harris', 13.9),
('Dallas', 14.0),
('Tarrant', 13.0),
('Bexar', 13.9),
('Travis', 12.8),
('Collin', 11.1),
('Denton', 11.3),
('Fort Bend', 9.5),
('Hidalgo', 18.0),
('El Paso', 14.6),
('Montgomery', 12.3),
('Williamson', 11.0),
('Cameron', 17.5),
('Brazoria', 11.4),
('Bell', 15.1),
('Galveston', 14.1),
('Nueces', 14.7),
('Lubbock', 15.5),
('Hays', 12.0),
('McLennan', 15.7),
('Webb', 15.8),
('Smith', 14.8),
('Jefferson', 16.6),
('Brazos', 15.5),
('Ellis', 11.5);

