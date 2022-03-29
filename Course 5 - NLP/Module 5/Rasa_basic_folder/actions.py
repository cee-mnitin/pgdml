from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

import logging
import json
import smtplib
import pandas as pd

from email.message import EmailMessage
#from rasa.constants import DEFAULT_DATA_PATH
from rasa_sdk import Action, Tracker
from rasa_sdk.events import AllSlotsReset, SlotSet, Restarted

import warnings
warnings.filterwarnings("ignore")

DEFAULT_DATA_PATH = '.'

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("__name__")


WeOperate = ['New Delhi', 'Gurgaon', 'Noida', 'Faridabad', 'Allahabad', 'Bhubaneshwar', 'Mangalore', 'Mumbai', 'Ranchi', 'Patna', 'Mysore', 'Aurangabad', 'Amritsar', 'Puducherry', 'Varanasi', 'Nagpur', 'Vadodara', 'Dehradun', 'Vizag', 'Agra', 'Ludhiana', 'Kanpur', 'Lucknow', 'Surat', 'Kochi', 'Indore', 'Ahmedabad', 'Coimbatore', 'Chennai', 'Guwahati', 'Jaipur', 'Hyderabad', 'Bangalore', 'Nashik', 'Pune', 'Kolkata', 'Bhopal', 'Goa', 'Chandigarh', 'Ghaziabad', 'Ooty', 'Gangtok', 'Shimla']

def RestaurantSearch(City, Cuisine, price):
	ZomatoData = pd.read_csv('zomato.csv')
	ZomatoData = ZomatoData.drop_duplicates().reset_index(drop=True)
	
	logger.info("RestaurantSearch " + str(City) + str(Cuisine) + str(price))
	# Filter by City
	if City.lower() in [x.lower() for x in WeOperate]:
		ZomatoData = ZomatoData[(ZomatoData['City'].apply(lambda x: City.lower() in x.lower()))]
	
	if Cuisine.lower() in ["chinese", "mexican", "italian", "american", "south indian", "north indian"]:
		ZomatoData = ZomatoData[(ZomatoData['Cuisines'].apply(lambda x: Cuisine.lower() in x.lower()))]

	if price in ["low", "mid", "high", "all"]:
		rangeMin = 0
		rangeMax = 999999
		
		if price == "low":
			rangeMax = 299
		elif price == "mid":
			rangeMin = 300
			rangeMax = 700
		elif price == "high":
			rangeMin = 701
		else:
			#Default budget
			rangeMin = 0
			rangeMax = 9999
		
		ZomatoData = ZomatoData[(ZomatoData['Average Cost for two'].apply(lambda x: (x >= rangeMin and x <= rangeMax)))]
    
	ZomatoData = ZomatoData[['Restaurant Name','Address','Average Cost for two','Aggregate rating']]

	return ZomatoData

         
""" Custom action to fetch list of restaurants
"""
class ActionSearchRestaurants(Action):
	def name(self):
		return 'action_search_restaurants'

	def run(self, dispatcher, tracker, domain):
		#config={ "user_key":"f4924dc9ad672ee8c4f8c84743301af5"}
		loc = tracker.get_slot('location')
		cuisine = tracker.get_slot('cuisine')
		price = tracker.get_slot("price")
		results = RestaurantSearch(City=loc, Cuisine=cuisine, price=price)
		response=""
		email_response = ""
		if results.shape[0] == 0:
			response= "Sorry, no restaurants found."
			email_response = "Sorry, no restaurants found."
			search_validity = "invalid"
		else:
			search_validity = "valid"
			results = results.sort_values(by='Aggregate rating', ascending=False)
			
			for restaurant in results.iloc[:5].iterrows():
				restaurant = restaurant[1]
				new_restaurant = f"{restaurant['Restaurant Name']} in {restaurant['Address']} has been rated {restaurant['Aggregate rating']}"
				new_restaurant = new_restaurant + '\n' + '-' * len(new_restaurant)
				response = response + "\n" + new_restaurant
			response = f"Showing you the Top Rated restaurants matching your search :- \n\n {response}"
			response = response + "\n\n" + "=" * max(len(x) for x in response.split("\n")) + "\n\n"

			for restaurant in results.iloc[:10].iterrows():
				restaurant = restaurant[1]
				new_restaurant = f"Restaurant Name: {restaurant['Restaurant Name']}\nRestaurant locality address: {restaurant['Address']}\n"
				new_restaurant =  new_restaurant + f"The average budget for two people: {restaurant['Average Cost for two']}\nZomato user rating: {restaurant['Aggregate rating']}\n"
				new_restaurant = new_restaurant + '\n' + '-' * len(new_restaurant)
				email_response = email_response + "\n" + new_restaurant + "\n"
			
		dispatcher.utter_message(response)
		return [SlotSet("search_validity", search_validity), SlotSet('email_response',email_response)]

class ActionSendMail(Action):
	def name(self):
		return 'action_send_mail'

	def run(self, dispatcher, tracker, domain):
		email = tracker.get_slot('email')
		restaurants = tracker.get_slot('email_response')
		if email == None:
			email = 'mnitin73.upgrad@gmail.com'
		s = smtplib.SMTP('smtp.gmail.com', 587) 
		s.starttls() 
		try:
			s.login('mnitin73.upgrad@gmail.com', "5R3FT9XFXK")
		except:
			dispatcher.utter_message(f'bad credentials, your preferences deleted. {email}')
			return [AllSlotsReset()]
		message = "The details of all the restaurants you inquried \n \n"
		message = message + restaurants
		try:
			s.sendmail("mnitin73.upgrad@gmail.com", str(email), message)
			s.quit()
			dispatcher.utter_message("Email sent please check your inbox. your preferances will be deleted ")
			return [AllSlotsReset()]
		except:
			dispatcher.utter_message("Can't send the email. deleted your preferances")
			return [AllSlotsReset()]

class ActionValidateLocation(Action):
    def name(self):
        return "action_location_valid"

    def run(self, dispatcher, tracker, domain):

        location = tracker.get_slot("location")
        location_validity = "valid"

        if not location:
            location_validity = "invalid"
        else:
            WeOperate = ['New Delhi', 'Gurgaon', 'Noida', 'Faridabad', 'Allahabad', 'Bhubaneshwar', 'Mangalore', 'Mumbai', 'Ranchi', 'Patna', 'Mysore', 'Aurangabad', 'Amritsar', 'Puducherry', 'Varanasi', 'Nagpur', 'Vadodara', 'Dehradun', 'Vizag', 'Agra', 'Ludhiana', 'Kanpur', 'Lucknow', 'Surat', 'Kochi', 'Indore', 'Ahmedabad', 'Coimbatore', 'Chennai', 'Guwahati', 'Jaipur', 'Hyderabad', 'Bangalore', 'Nashik', 'Pune', 'Kolkata', 'Bhopal', 'Goa', 'Chandigarh', 'Ghaziabad', 'Ooty', 'Gangtok', 'Shimla']
            WeOperate = [x.lower() for x in WeOperate]
            location_validity = (
                        "invalid"
                        if location.lower() not in WeOperate
                        else "valid"
                    )
                
        return [SlotSet("location_validity", location_validity)]

class ActionValidateCuisine(Action):
    def name(self):
        return "action_cuisine_valid"

    def run(self, dispatcher, tracker, domain):

        cuisine = tracker.get_slot("cuisine")
        cuisine_check = "valid"

        if not cuisine:
            cuisine_check = "invalid"
        else:
            supported_cuisines = ["american","chinese","italian","mexican","north indian","south indian"]

            cuisine_check = (
                "invalid" if cuisine.lower() not in supported_cuisines else "valid")

        return [SlotSet("cuisine_validity", cuisine_check)]

class ActionRestarted(Action): 	
	def name(self):
		return 'action_restart'

	def run(self, dispatcher, tracker, domain):
		return[Restarted()] 


class ActionSlotReset(Action): 
	def name(self): 
		return 'action_slot_reset' 

	def run(self, dispatcher, tracker, domain): 
		return[AllSlotsReset()]