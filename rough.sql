-- Run the following commands in the MySQL CLI to create the database, update the username and password in app.py

--creating a database
CREATE DATABASE drones;

--creating a table
CREATE TABLE drone_data
(
    Drone_Name VARCHAR(30),
    Transmission_Range INT,
    Flight_Altitude INT,
    Flight_Speed INT,
    Camera_Quality INT,
    Payload_Capacity INT,
    Cost INT,
    Flight_Time INT,
    Video_Resolution INT,
    Thermal_Camera INT
);

--inserting the data into the table
INSERT INTO drone_data(Drone_Name,Transmission_Range,Flight_Altitude,Flight_Speed,Camera_Quality,Payload_Capacity,Cost,Flight_Time,Video_Resolution,Thermal_Camera)
VALUES('DJI Mavic 3',15000,6000,42,20,0.8,8200,46,30,1),('Sony Airpeak s1',2500,1900,60,24,2.5,9000,22,45,1),('Freefly Alta X ',8000,2100,60,30,16,16000,50,60,1),('Flyabilty Elios 3',2400,1500,15,12,0.5,2000,15,25,0),('DJI Agras T10',7500,1000,20,30,2,12000,120,60,1),('senseFly eBeeX',5000,1200,68,24,1.5,6000,90,30,1);

INSERT INTO drone_data(Drone_Name,Transmission_Range,Flight_Altitude,Flight_Speed,Camera_Quality,Payload_Capacity,Cost,Flight_Time,Video_Resolution,Thermal_Camera)
VALUES('DJI Matrice 300 RTK',4000,500,51,36,2,4500,55,30,0),('AirShark Zeus',8000,3000,60,20,5000,5,60,30,0),('FlyLeaf 3',1200,600,40,20,10,4500,30,30,0),('DJI Inspire 2',4000,1800,45,60,0.5,10000,60,60,1),('AVT Spark',5500,2200,30,36,7,5600,45,30,0),('DJI Inspire 2',2500,1000,30,40,0.5,9000,35,60,1),('Holmes 2E',1200,800,30,20,4.5,3000,25,30,0),('DJI Air 2S',4000,1000,50,48,2.5,7500,25,60,1),('FlyLeaf 4',2400,800,30,20,12.5,5500,30,30,0),('DJI Mavic Mini',4000,1200,45,25,1.5,6000,30,60,1);