import streamlit as st
import sklearn
import numpy as np
import pandas as pd
import pickle
from PIL import Image

loaded_model = pickle.load(open('/Users/rahuljestadi/Desktop/FLIGHT/flight_flight.pkl','rb'))


def flight_predict(input_data):
    input_data_as_numpy_array = np.asarray(input_data)
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)
    prediction = loaded_model.predict(input_data_reshaped)
    return prediction

def main():

    st.set_page_config(page_title='Flight Fare Predictor', layout='wide')

#----Header----

    st.text("Predictive Analytics")
    image=Image.open('/Users/rahuljestadi/Desktop/FLIGHT/img/wallpapersden.com_airport-night-illustration_6800x2500.jpg')
    st.image(image, use_column_width=True)

    st.header("Predict flight fare")
    st.write("Select the values below to get prediction")
 
# first argument takes the titleof the selectionbox
# second argument takes options
    Airline = st.selectbox("Airline: ",
                     ['Trujet', 'SpiceJet', 'Air Asia','IndiGo','GoAir','Vistara',
                     'Vistara Premium Economy','Air India','Multiple Carriers',
                     'Multiple carriers Premium Economy','Jet Airways','Jet Airways Business'])
 
# print the selected hobby
    st.write("Your chosen airline is: ", Airline)

    departure = st.date_input("Enter your date of departure")
    st.write("Date chosen is : ",departure)

    #t = st.time_input('Desired departure time')
    #st.write("Chosen departure time is : ",t)

    t = st.text_input('Desired departure time')
    st.write("Chosen departure time is : ",t)

    Stops = st.selectbox("Stops: ",
                     [0,1,2,3,4,5])
 
# print the selected hobby
    st.write("Number of stops is: ", Stops)

    arrival = st.date_input("Enter your date of Arrival")
    st.write("Date chosen is : ",arrival)

    #t = st.time_input('Desired arrival time')
    #st.write("Chosen arrival time is : ",arrival)

    t = st.text_input('Desired arrival time')
    st.write("Chosen arrival time is : ",arrival)

    Source = st.selectbox("Your Source: ",
                     ['Delhi', 'Banglore', 'Chennai','Kolkata','Mumbai'])

    st.write("Your chosen destination is: ", Source)


    Destination = st.selectbox("Your Destination: ",
                     ['Delhi', 'Banglore', 'Cochin','Kolkata','Hyderabad'])

    st.write("Your chosen destination is: ", Destination)

     # Date_of_Journey
    date_dep = departure
    journey_day = int(pd.to_datetime(date_dep, format="%Y-%m-%dT%H:%M").day)
    journey_month = int(pd.to_datetime(date_dep, format ="%Y-%m-%dT%H:%M").month)
    journey_year = int(pd.to_datetime(date_dep, format="%Y-%m-%dT%H:%M").year)

    Dep_Time_hour = int(pd.to_datetime(date_dep, format ="%Y-%m-%dT%H:%M").hour)
    Dep_Time_minute = int(pd.to_datetime(date_dep, format ="%Y-%m-%dT%H:%M").minute)

    date_arr = arrival
    Arrival_Time_hour = int(pd.to_datetime(date_arr, format ="%Y-%m-%dT%H:%M").hour)
    Arrival_Time_minute = int(pd.to_datetime(date_arr, format ="%Y-%m-%dT%H:%M").minute)

    Duration_hours = abs(Arrival_Time_hour - Dep_Time_hour)
    Duration_minutes = abs(Arrival_Time_minute - Dep_Time_minute)
 
    Total_Stops = Stops
  
    airline=Airline
    if(airline=='Jet Airways'):
        Airline= 10
    elif(airline=='IndiGo'):
        Airline = 3
    elif(airline=='Air India'):
        Airline = 7
    elif(airline=='Multiple_carriers'):
        Airline = 8 
    elif(airline=='SpiceJet'):
        Airline = 1
    elif(airline=='Vistara'):
        Airline = 5          
    elif(airline=='GoAir'):
        Airline = 4
    elif(airline=='Multiple carriers Premium Economy'):
        Airline = 9
    elif(airline=='Jet Airways Business'):
        Airline = 11
    elif(airline=='Vistara Premium Economy'):
        Airline = 6
    elif(airline=='Trujet'):
        Airline = 0
    elif(airline=='Air Asia'):
        Airline = 2
 
    Source = Source
    if (Source == 'Delhi'):
        Source_Delhi = 1
        Source_Kolkata = 0
        Source_Mumbai = 0
        Source_Chennai = 0
        Source_Banglore = 0

    elif (Source == 'Kolkata'):
        Source_Delhi = 0
        Source_Kolkata = 1
        Source_Mumbai = 0
        Source_Chennai = 0
        Source_Banglore = 0

    elif (Source == 'Mumbai'):
        Source_Delhi = 0
        Source_Kolkata = 0
        Source_Mumbai = 1
        Source_Chennai = 0
        Source_Banglore = 0

    elif (Source == 'Chennai'):
        Source_Delhi = 0
        Source_Kolkata = 0
        Source_Mumbai = 0
        Source_Chennai = 1
        Source_Banglore = 0

    elif (Source == 'Banglore'):
        Source_Delhi = 0
        Source_Kolkata = 0
        Source_Mumbai = 0
        Source_Chennai = 0
        Source_Banglore = 1

    else:
        Source_Delhi = 0
        Source_Kolkata = 0
        Source_Mumbai = 0
        Source_Chennai = 0
        Source_Banglore = 0

    dest = Destination
    if (dest == 'Cochin'):
        Destination = 4
        
    elif (dest == 'Delhi'):
        Destination = 2

    elif (dest == 'Banglore'):
        Destination = 3

    elif (dest == 'Hyderabad'):
        Destination = 1

    elif (dest == 'Kolkata'):
        Destination = 0

    price_pred = ''
    if st.button('Predict Price'):
        price_pred = flight_predict([Airline, Destination, Total_Stops, journey_day, journey_month,
        journey_year, Dep_Time_hour, Dep_Time_minute, Arrival_Time_hour, Arrival_Time_minute, 
        Duration_hours, Duration_minutes, Source_Banglore, Source_Kolkata,Source_Delhi, Source_Chennai,
        Source_Mumbai])

    st.success(price_pred)

if __name__ == '__main__':
    main()


  