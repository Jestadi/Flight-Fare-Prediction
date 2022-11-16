from flask import Flask, request, render_template
from flask_cors import cross_origin
import sklearn
import pickle
import pandas as pd

app = Flask(__name__)
model = pickle.load(open("flight_pred.pkl", "rb"))

@app.route("/")
@cross_origin()
def home():
    return render_template("home.html")


@app.route("/predict", methods = ["GET", "POST"])
@cross_origin()
def predict():
    if request.method == "POST":

        # Date_of_Journey
        date_dep_day = request.form["journey_day"]
        date_dep_month = request.form["journey_month"]
        date_dep_year = request.form["journey_year"]
        Journey_day = int(pd.to_datetime(date_dep_day, format="%Y-%m-%dT%H:%M"))
        Journey_month = int(pd.to_datetime(date_dep_month, format ="%Y-%m-%dT%H:%M"))
        Journey_year = int(pd.to_datetime(date_dep_year, format ="%Y-%m-%dT%H:%M"))
        # print("Journey Date : ",Journey_day, Journey_month)

        # Departure
        dep_hour = request.form["Dep_Time_hour"]
        dep_minute = request.form["Dep_Time_minute"]
        Dep_hour = int(pd.to_datetime(dep_hour, format ="%Y-%m-%dT%H:%M"))
        Dep_min = int(pd.to_datetime(dep_minute, format ="%Y-%m-%dT%H:%M"))
        # print("Departure : ",Dep_hour, Dep_min)

        # Arrival
        arr_hour = request.form["Arrival_Time_hour"]
        arr_minute = request.form["Arrival_Time_minute"]

        Arrival_hour = int(pd.to_datetime(arr_hour, format ="%Y-%m-%dT%H:%M"))
        Arrival_min = int(pd.to_datetime(arr_minute, format ="%Y-%m-%dT%H:%M"))
        # print("Arrival : ", Arrival_hour, Arrival_min)

        # Duration
        dur_hour = request.form["Duration_hours"]
        dur_min = abs("Duration_minutes")
        # print("Duration : ", dur_hour, dur_min)

        # Total Stops
        Total_stops = int(request.form["Total_Stops"])
        # print(Total_stops)

        # Airline
        # AIR ASIA = 0 (not in column)
        airline=request.form['Airline']
        if(airline=='Jet Airways'):
            Airline = 10

        elif (airline=='IndiGo'):
            Airline = 3

        elif (airline=='Air India'):
            Airline = 7
            
        elif (airline=='Multiple carriers'):
            Airline = 8

        elif (airline=='SpiceJet'):
            Airline = 1
            
        elif (airline=='Vistara'):
            Airline = 5

        elif (airline=='GoAir'):
            Airline = 4

        elif (airline=='Multiple carriers Premium economy'):
            Airline = 9

        elif (airline=='Jet Airways Business'):
            Airline = 11

        elif (airline=='Vistara Premium economy'):
            Airline = 6
            
        elif (airline=='Trujet'):
           Airline = 0
        
        elif (airline=='Air Asia'):
            Airline = 2


        else:
            Airline = ValueError

        # print(Jet_Airways,
        #     IndiGo,
        #     Air_India,
        #     Multiple_carriers,
        #     SpiceJet,
        #     Vistara,
        #     GoAir,
        #     Multiple_carriers_Premium_economy,
        #     Jet_Airways_Business,
        #     Vistara_Premium_economy,
        #     Trujet)

        # Source
        # Banglore = 0 (not in column)
        Source_Delhi = request.form["Source"]
        if (Source == 'Delhi'):
            Source_Delhi = 1
            Source_Kolkata = 0
            Source_Mumbai = 0
            Source_Chennai = 0
            Source_Bangalore = 0
        
        elif (Source == 'Bangalore'):
            Source_Delhi = 0
            Source_Kolkata = 0
            Source_Mumbai = 0
            Source_Chennai = 0
            Source_Bangalore = 1

        elif (Source == 'Kolkata'):
            Source_Delhi = 0
            Source_Kolkata = 1
            Source_Mumbai = 0
            Source_Chennai = 0
            Source_Bangalore = 0

        elif (Source == 'Mumbai'):
            Source_Delhi = 0
            Source_Kolkata = 0
            Source_Mumbai = 1
            Source_Chennai = 0
            Source_Bangalore = 0

        elif (Source == 'Chennai'):
            Source_Delhi = 0
            Source_Kolkata = 0
            Source_Mumbai = 0
            Source_Chennai = 1
            Source_Bangalore = 0

        else:
            Source_Delhi = 0
            Source_Kolkata = 0
            Source_Mumbai = 0
            Source_Chennai = 0
            Source_Bangalore = 0

        # print(Source_Delhi,
        #     Source_Kolkata,
        #     Source_Mumbai,
        #     Source_Chennai)

        # Destination
        # Banglore = 0 (not in column)
        Source = request.form["Destination"]
        if (Source == 'Cochin'):
            d_Cochin = 1
            d_Delhi = 0
            d_Bangalore = 0
            d_Hyderabad = 0
            d_Kolkata = 0
        
        elif (Source == 'Delhi'):
            d_Cochin = 0
            d_Delhi = 1
            d_Bangalore = 0
            d_Hyderabad = 0
            d_Kolkata = 0
        
        elif (Source == 'Bangalore'):
            d_Cochin = 0
            d_Delhi = 0
            d_Bangalore = 1
            d_Hyderabad = 0
            d_Kolkata = 0

        elif (Source == 'Hyderabad'):
            d_Cochin = 0
            d_Delhi = 0
            d_Bangalore = 0
            d_Hyderabad = 1
            d_Kolkata = 0

        elif (Source == 'Kolkata'):
            d_Cochin = 0
            d_Delhi = 0
            d_Bangalore = 0
            d_Hyderabad = 0
            d_Kolkata = 1

        else:
            d_Cochin = 0
            d_Delhi = 0
            d_Bangalore = 0
            d_Hyderabad = 0
            d_Kolkata = 0

        # print(
        #     d_Cochin,
        #     d_Delhi,
        #     d_Bangalore,
        #     d_Hyderabad,
        #     d_Kolkata
        # )
        

    #     ['Total_Stops', 'Journey_day', 'Journey_month', 'Dep_hour',
    #    'Dep_min', 'Arrival_hour', 'Arrival_min', 'Duration_hours',
    #    'Duration_mins', 'Airline_Air India', 'Airline_GoAir', 'Airline_IndiGo',
    #    'Airline_Jet Airways', 'Airline_Jet Airways Business',
    #    'Airline_Multiple carriers',
    #    'Airline_Multiple carriers Premium economy', 'Airline_SpiceJet',
    #    'Airline_Trujet', 'Airline_Vistara', 'Airline_Vistara Premium economy',
    #    'Source_Chennai', 'Source_Delhi', 'Source_Kolkata', 'Source_Mumbai',
    #    'Destination_Cochin', 'Destination_Delhi', 'Destination_Hyderabad',
    #    'Destination_Kolkata', 'Destination_New Delhi']
        
        prediction=model.predict([[
            Total_stops,
            Journey_day,
            Journey_month,
            Journey_year,
            Dep_hour,
            Dep_min,
            Arrival_hour,
            Arrival_min,
            dur_hour,
            dur_min,
            Airline,
            Source_Chennai,
            Source_Delhi,
            Source_Kolkata,
            Source_Mumbai,
            Source_Bangalore,
            d_Cochin,
            d_Delhi,
            d_Hyderabad,
            d_Kolkata,
            d_Bangalore
        ]])

        output=round(prediction[0],2)

        return render_template('home.html',prediction_text="Your Predicted flight price is Rs. {}".format(output))


    return render_template("home.html")




if __name__ == "__main__":
    app.run(debug=True)
