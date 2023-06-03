import numpy as np
import pandas as pd
import mysql.connector as c
from flask import Flask, request,render_template,redirect

class Drone:
    drone_name='Not Selected'
    transmission_range='Not Selected'
    flight_altitude='Not Selected'
    flight_speed='Not Selected'
    camera_quality='Not Selected'
    payload_capacity='Not Selected'
    cost='Not Selected'
    flight_time='Not Selected'
    video_resolution='Not Selected'
    thermal_camera='Not Selected'
    

app=Flask(__name__)
@app.route("/", methods=['GET','POST'])
def get_requirements():
    # connecting the database and fetching the data:
    con=c.connect(host='localhost',user='root',password='Akash_2312',database='drones') #check the user and it's correspoinding password
    cur=con.cursor()
    query=f"SELECT * FROM drone_data"
    cur.execute(query)
    column_names= [column[0] for column in cur.description]
    rows=cur.fetchall()
    df=pd.DataFrame(rows,columns=column_names)
    cur.close()
    con.close()
    a1=Drone()
    a2=Drone()
    a3=Drone()
    a4=Drone()
    a5=Drone()
    print(df)
    print('the database has been connected')
    # taking input data from webpage
    if request.method=="POST":
        print('post request strted')
        transmission_range=int(request.form["transmissionRange"])
        print('transmission range has been taken')
        transmission_range_preference=int(request.form["transmissionRangePreference"])
        print('transmission range preference has been taken')
        flight_altitude=int(request.form["flightAltitude"])
        print('flight altitude has been taken')
        flight_altitude_preference=int(request.form["flightAltitudePreference"])
        print('flight altitude preference has been taken')
        flight_speed=int(request.form["flightSpeed"])
        print('flight speed has been taken')
        flight_speed_preference=int(request.form["flightSpeedPreference"])
        print('flight speed preference has been taken')
        camera_quality=int(request.form["cameraQuality"])
        print('camera quality has been taken')
        camera_quality_preference=int(request.form["cameraQualityPreference"])
        print('camera quality preference has been taken')
        payload_capacity=round(float(request.form["payloadCapacity"]))
        print('payload capacity has been taken')
        payload_capacity_preference=int(request.form["payloadCapacityPreference"])
        print('payload capacity preference has been taken')
        cost=int(request.form["cost"])
        print('cost has been taken')
        cost_preference=int(request.form["costPreference"])
        print('cost preference has been taken')
        flight_time=int(request.form["flightTime"])
        print('flight time has been taken')
        flight_time_preference=int(request.form["flightTimePreference"])
        print('flight time preference has been taken')
        video_resolution=int(request.form["videoResolution"])
        print('video resolution has been taken')
        video_resolution_preference=int(request.form["videoResolutionPreference"])
        print('video resolution has been taken')
        thermal_camera=int(request.form["thermalCamera"])
        print('thermal camera has been taken')
        inputs=[transmission_range,flight_altitude,flight_speed,camera_quality,payload_capacity,cost,flight_time,video_resolution,thermal_camera]
        inputs_preference=[transmission_range_preference,flight_altitude_preference,flight_speed_preference,camera_quality_preference,payload_capacity_preference,cost_preference,flight_time_preference,video_resolution_preference]
        print('the input has been taken from the page')
        print(inputs)
        print(inputs_preference)
        total_count=len(df)
        df['Score']=0
        for x in range(0,total_count):
            #calculating score for transmission range:
            y=df.iloc[x]['Transmission_Range']
            score_of_transmission_range=(y/inputs[0])*100
            score_of_transmission_range=100-score_of_transmission_range
            if score_of_transmission_range<0:
                score_of_transmission_range*=(-1)
            score_of_transmission_range=100-score_of_transmission_range
            score_of_transmission_range*=inputs_preference[0]
            df.at[x,'Score']+=score_of_transmission_range
            #calculating score for flight altitude:
            y=df.iloc[x]['Flight_Altitude']
            score_of_flight_altitude=(y/inputs[1])*100
            score_of_flight_altitude=100-score_of_flight_altitude
            if score_of_flight_altitude<0:
                score_of_flight_altitude*=(-1)
            score_of_flight_altitude=100-score_of_flight_altitude
            score_of_flight_altitude*=inputs_preference[1]
            df.at[x,'Score']+=score_of_flight_altitude

            #calculating score for flight speed:
            y=df.iloc[x]['Flight_Speed']
            score_of_flight_speed=(y/inputs[2])*100
            score_of_flight_speed=100-score_of_flight_speed
            if score_of_flight_speed:
                score_of_flight_speed*=(-1)
            score_of_flight_speed=100-score_of_flight_speed
            score_of_flight_speed*=inputs_preference[2]
            df.at[x,'Score']+=score_of_flight_speed
            #calculating score for camera quality:
            y=df.iloc[x]['Camera_Quality']
            score_of_camera_quality=(y/inputs[3])*100
            score_of_camera_quality=100-score_of_camera_quality
            if score_of_camera_quality<0:
                score_of_camera_quality*=(-1)
            score_of_camera_quality=100-score_of_camera_quality
            score_of_camera_quality*=inputs_preference[3]
            df.at[x,'Score']+=score_of_camera_quality
            #calculating score for payload capacity:
            y=df.iloc[x]['Payload_Capacity']
            score_of_payload_capacity=(y/inputs[4])*100
            score_of_payload_capacity=100-score_of_payload_capacity
            if score_of_payload_capacity<0:
                score_of_payload_capacity*=(-1)
            score_of_payload_capacity=100-score_of_payload_capacity
            score_of_payload_capacity*=inputs_preference[4]
            df.at[x,'Score']+=score_of_payload_capacity
            #calculating score for cost:
            y=df.iloc[x]['Cost']
            score_of_cost=(y/inputs[5])*100
            score_of_cost=100-score_of_cost
            if score_of_cost<0:
                score_of_cost*=(-1)
            score_of_cost=100-score_of_cost
            score_of_cost*=inputs_preference[5]
            df.at[x,'Score']+=score_of_cost
            #calculating score for flight time:
            y=df.iloc[x]['Flight_Time']
            score_of_flight_time=(y/inputs[6])*100
            score_of_flight_time=100-score_of_flight_time
            if score_of_flight_time<0:
                score_of_flight_time*=(-1)
            score_of_flight_time=100-score_of_flight_time
            score_of_flight_time*=inputs_preference[6]
            df.at[x,'Score']+=score_of_flight_time
            #calculating score for Video Resolution:
            y=df.iloc[x]['Video_Resolution']
            score_of_video_resolution=(y/inputs[7])*100
            score_of_video_resolution=100-score_of_video_resolution
            if score_of_video_resolution<0:
                score_of_video_resolution*=(-1)
            score_of_video_resolution=100-score_of_video_resolution
            score_of_video_resolution*=inputs_preference[7]
            df.at[x,'Score']+=score_of_video_resolution
            #calculating score for thermal camera:
            y=df.iloc[x]['Thermal_Camera']
            if (inputs[8]==y):
                score_of_thermal_camera=400
            else:
                score_of_thermal_camera=0
            df.at[x,'Score']+=score_of_thermal_camera
        print(df)
        max_score=df['Score'].max()
        x=(df.sort_values('Score',ascending=False))
        x=(x.head())
        print(x)
        a1.drone_name=x['Drone_Name'].iloc[0]
        a1.transmission_range=x['Transmission_Range'].iloc[0]
        a1.flight_altitude=x['Flight_Altitude'].iloc[0]
        a1.flight_speed=x['Flight_Speed'].iloc[0]
        a1.camera_quality=x['Camera_Quality'].iloc[0]
        a1.payload_capacity=x['Payload_Capacity'].iloc[0]
        a1.cost=x['Cost'].iloc[0]
        a1.flight_time=x['Flight_Time'].iloc[0]
        a1.video_resolution=x['Video_Resolution'].iloc[0]
        a1.thermal_camera=x['Thermal_Camera'].iloc[0]
        if a1.thermal_camera>=1:
            a1.thermal_camera='Available'
        else:
            a1.thermal_camera='Not Available'
        
        a2.drone_name=x['Drone_Name'].iloc[1]
        a2.transmission_range=x['Transmission_Range'].iloc[1]
        a2.flight_altitude=x['Flight_Altitude'].iloc[1]
        a2.flight_speed=x['Flight_Speed'].iloc[1]
        a2.camera_quality=x['Camera_Quality'].iloc[1]
        a2.payload_capacity=x['Payload_Capacity'].iloc[1]
        a2.cost=x['Cost'].iloc[1]
        a2.flight_time=x['Flight_Time'].iloc[1]
        a2.video_resolution=x['Video_Resolution'].iloc[1]
        a2.thermal_camera=x['Thermal_Camera'].iloc[1]
        if a2.thermal_camera>=1:
            a2.thermal_camera='Available'
        else:
            a2.thermal_camera='Not Available'
        
        a3.drone_name=x['Drone_Name'].iloc[2]
        a3.transmission_range=x['Transmission_Range'].iloc[2]
        a3.flight_altitude=x['Flight_Altitude'].iloc[2]
        a3.flight_speed=x['Flight_Speed'].iloc[2]
        a3.camera_quality=x['Camera_Quality'].iloc[2]
        a3.payload_capacity=x['Payload_Capacity'].iloc[2]
        a3.cost=x['Cost'].iloc[2]
        a3.flight_time=x['Flight_Time'].iloc[2]
        a3.video_resolution=x['Video_Resolution'].iloc[2]
        a3.thermal_camera=x['Thermal_Camera'].iloc[2]
        if a3.thermal_camera>=1:
            a3.thermal_camera='Available'
        else:
            a3.thermal_camera='Not Available'

        a4.drone_name=x['Drone_Name'].iloc[4]
        a4.transmission_range=x['Transmission_Range'].iloc[4]
        a4.flight_altitude=x['Flight_Altitude'].iloc[4]
        a4.flight_speed=x['Flight_Speed'].iloc[4]
        a4.camera_quality=x['Camera_Quality'].iloc[4]
        a4.payload_capacity=x['Payload_Capacity'].iloc[4]
        a4.cost=x['Cost'].iloc[4]
        a4.flight_time=x['Flight_Time'].iloc[4]
        a4.video_resolution=x['Video_Resolution'].iloc[4]
        a4.thermal_camera=x['Thermal_Camera'].iloc[4]
        if a4.thermal_camera>=1:
            a4.thermal_camera='Available'
        else:
            a4.thermal_camera='Not Available'

        a5.drone_name=x['Drone_Name'].iloc[3]
        a5.transmission_range=x['Transmission_Range'].iloc[3]
        a5.flight_altitude=x['Flight_Altitude'].iloc[3]
        a5.flight_speed=x['Flight_Speed'].iloc[3]
        a5.camera_quality=x['Camera_Quality'].iloc[3]
        a5.payload_capacity=x['Payload_Capacity'].iloc[3]
        a5.cost=x['Cost'].iloc[3]
        a5.flight_time=x['Flight_Time'].iloc[3]
        a5.video_resolution=x['Video_Resolution'].iloc[3]
        a5.thermal_camera=x['Thermal_Camera'].iloc[3]
        if a5.thermal_camera>=1:
            a5.thermal_camera='Available'
        else:
            a5.thermal_camera='Not Available'

    return render_template('demo.html',a1=a1,a2=a2,a3=a3,a4=a4,a5=a5)

if __name__ == '__main__':
    app.run()