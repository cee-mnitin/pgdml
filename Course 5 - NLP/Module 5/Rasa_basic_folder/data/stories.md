## interactive_story_1
* greet
    - utter_greet
* goodbye
    - utter_goodbye
    - action_restart

## interactive_story_2
* goodbye
    - action_restart

## interactive_story_3
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_price
* inform_price{"price": "med"}
    - slot{"price": "med"}
    - utter_ask_cuisine
* inform_cuisine{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - action_search_restaurants
    - utter_email_prompt
* affirm
    - utter_ask_email
* inform_email{"email": "mnitin73.upgrad@gmail.com"}
    - slot{"email": "mnitin73.upgrad@gmail.com"}
    - action_send_mail
    - utter_goodbye
    - action_restart

## interactive_story_4
* restaurant_search{"price": "mid"}
    - slot{"price": "med"}
    - utter_ask_location
* inform_location{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* inform_cuisine{"cuisine": "Mexican"}
    - slot{"cuisine": "Mexican"}
    - action_search_restaurants
    - utter_email_prompt
* affirm
    - utter_ask_email
* inform_email{"email": "mnitin73.upgrad@gmail.com"}
    - slot{"email": "mnitin73.upgrad@gmail.com"}
    - action_send_mail
    - utter_goodbye
    - action_restart

## interactive_story_5
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - utter_ask_location
* inform_location{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_price
* inform_price{"price": "med"}
    - slot{"price": "med"}
    - action_search_restaurants
    - utter_email_prompt
* affirm
    - utter_ask_email
* inform_email{"email": "mnitin73.upgrad@gmail.com"}
    - slot{"email": "mnitin73.upgrad@gmail.com"}
    - action_send_mail
    - utter_goodbye
    - action_restart

## interactive_story_6
* restaurant_search{"location": "delhi", "cuisine": "Italian"}
    - slot{"cuisine": "Italian", "location": "delhi"}
    - utter_ask_price
* inform_price{"price": "med"}
    - slot{"price": "med"}
    - action_search_restaurants
    - utter_email_prompt
* affirm
    - utter_ask_email
* inform_email{"email": "mnitin73.upgrad@gmail.com"}
    - slot{"email": "mnitin73.upgrad@gmail.com"}
    - action_send_mail
    - utter_goodbye
    - action_restart

## interactive_story_7
* restaurant_search{"cuisine": "Italian", "price": "med"}
    - slot{"cuisine": "Italian", "price": "med"}
    - utter_ask_location
* inform_location{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_search_restaurants
    - utter_email_prompt
* affirm
    - utter_ask_email
* inform_email{"email": "mnitin73.upgrad@gmail.com"}
    - slot{"email": "mnitin73.upgrad@gmail.com"}
    - action_send_mail
    - utter_goodbye
    - action_restart

## interactive_story_8
* restaurant_search{"price": "mid", "location": "delhi"}
    - slot{"price": "med", "location": "delhi"}
    - utter_ask_cuisine
* inform_cuisine{"cuisine": "Mexican"}
    - slot{"cuisine": "Mexican"}
    - action_search_restaurants
    - utter_email_prompt
* affirm
    - utter_ask_email
* inform_email{"email": "mnitin73.upgrad@gmail.com"}
    - slot{"email": "mnitin73.upgrad@gmail.com"}
    - action_send_mail
    - utter_goodbye
    - action_restart

## interactive_story_9
* greet
    - utter_greet
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_price
* inform_price{"price": "med"}
    - slot{"price": "med"}
    - utter_ask_cuisine
* inform_cuisine{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - action_search_restaurants
    - utter_email_prompt
* affirm
    - utter_ask_email
* inform_email{"email": "mnitin73.upgrad@gmail.com"}
    - slot{"email": "mnitin73.upgrad@gmail.com"}
    - action_send_mail
    - utter_goodbye
    - action_restart

## interactive_story_10
* greet
    - utter_greet
* restaurant_search{"price": "mid"}
    - slot{"price": "med"}
    - utter_ask_location
* inform_location{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* inform_cuisine{"cuisine": "Mexican"}
    - slot{"cuisine": "Mexican"}
    - action_search_restaurants
    - utter_email_prompt
* affirm
    - utter_ask_email
* inform_email{"email": "mnitin73.upgrad@gmail.com"}
    - slot{"email": "mnitin73.upgrad@gmail.com"}
    - action_send_mail
    - utter_goodbye
    - action_restart

## interactive_story_11
* greet
    - utter_greet
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - utter_ask_location
* inform_location{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_price
* inform_price{"price": "med"}
    - slot{"price": "med"}
    - action_search_restaurants
    - utter_email_prompt
* affirm
    - utter_ask_email
* inform_email{"email": "mnitin73.upgrad@gmail.com"}
    - slot{"email": "mnitin73.upgrad@gmail.com"}
    - action_send_mail
    - utter_goodbye
    - action_restart

## interactive_story_12
* greet
    - utter_greet
* restaurant_search{"location": "delhi", "cuisine": "Italian"}
    - slot{"cuisine": "Italian", "location": "delhi"}
    - utter_ask_price
* inform_price{"price": "med"}
    - slot{"price": "med"}
    - action_search_restaurants
    - utter_email_prompt
* affirm
    - utter_ask_email
* inform_email{"email": "mnitin73.upgrad@gmail.com"}
    - slot{"email": "mnitin73.upgrad@gmail.com"}
    - action_send_mail
    - utter_goodbye
    - action_restart

## interactive_story_13
* greet
    - utter_greet
* restaurant_search{"cuisine": "Italian", "price": "med"}
    - slot{"cuisine": "Italian", "price": "med"}
    - utter_ask_location
* inform_location{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_search_restaurants
    - utter_email_prompt
* affirm
    - utter_ask_email
* inform_email{"email": "mnitin73.upgrad@gmail.com"}
    - slot{"email": "mnitin73.upgrad@gmail.com"}
    - action_send_mail
    - utter_goodbye
    - action_restart

## interactive_story_14
* greet
    - utter_greet
* restaurant_search{"price": "mid", "location": "delhi"}
    - slot{"price": "med", "location": "delhi"}
    - utter_ask_cuisine
* inform_cuisine{"cuisine": "Mexican"}
    - slot{"cuisine": "Mexican"}
    - action_search_restaurants
    - utter_email_prompt
* affirm
    - utter_ask_email
* inform_email{"email": "mnitin73.upgrad@gmail.com"}
    - slot{"email": "mnitin73.upgrad@gmail.com"}
    - action_send_mail
    - utter_goodbye
    - action_restart

## interactive_story_15
* greet
  - utter_greet
* restaurant_search
  - utter_ask_location
* restaurant_search{"location": "Bangalore"}
  - action_location_valid
  - slot{"location_validity" : "invalid"}
  - utter_location_invalid
  - utter_ask_location_retry
* affirm
  - utter_ask_location  
  - action_slot_reset
* restaurant_search{"location": "Bangalore"}
  - action_location_valid
  - slot{"location_validity" : "valid"}
  - utter_ask_cuisine  
* restaurant_search{"cuisine": "Chinese"}
  - utter_ask_price
* inform_price{"price": "low"}
  - slot{"price": "low"}
  - action_search_restaurants
  - slot{"search_validity" : "valid", "email_response": ""}
  - utter_email_prompt
* affirm
  - utter_ask_email
* inform_email{"email": "abc@abc.com"}
  - action_send_mail
  - utter_confirm_email
* thank
  - utter_goodbye
  - action_restart

## interactive_story_16
* greet
  - utter_greet
* restaurant_search{"location": "Mumbai", "cuisine": "chinese"}
  - action_location_valid
  - slot{"location_validity" : "valid"}  
  - action_cuisine_valid
  - slot{"cuisine_validity" : "invalid"}
  - utter_cuisine_invalid
  - utter_ask_cuisine_retry
* affirm
  - utter_ask_cuisine
* restaurant_search{"cuisine": "Chinese"}
  - utter_ask_price
* inform_price{"price": "high"}
  - slot{"price": "high"}
  - action_search_restaurants
  - slot{"search_validity" : "valid", "email_response": ""}
  - utter_email_prompt
* affirm
  - utter_ask_email
* inform_email{"email": "abc@abc.com"}
  - action_send_mail
  - utter_confirm_email
* thank
  - utter_goodbye
  - action_restart

## interactive_story_17
* greet
  - utter_greet
* restaurant_search
  - utter_ask_location
* restaurant_search{"location": "Bangalore"}
  - action_location_valid
  - slot{"location_validity" : "valid"}
  - utter_ask_cuisine
* restaurant_search{"cuisine": "Chinese"}
  - utter_ask_price
* inform_price{"price": "low"}
  - slot{"price": "low"}
  - action_search_restaurants
  - slot{"search_validity" : "valid", "email_response": ""}
  - utter_email_prompt
* affirm
  - utter_ask_email
* inform_email{"email": "abc@abc.com"}
  - action_send_mail
  - utter_confirm_email
* thank
  - utter_goodbye
  - action_restart

## interactive_story_18
* greet
  - utter_greet
* restaurant_search
  - utter_ask_location
* restaurant_search{"location": "Bangalore"}
  - action_location_valid
  - slot{"location_validity" : "valid"}  
  - utter_ask_cuisine
* restaurant_search{"cuisine": "Chinese"}
  - utter_ask_price
* inform_price{"price": "low"}
  - slot{"price": "low"}
  - action_search_restaurants
  - slot{"search_validity" : "valid", "email_response": ""}  
  - utter_email_prompt
* deny
  - utter_did_that_help
* affirm
  - utter_happy
  - utter_goodbye
  - action_restart

## interactive_story_19
* greet
  - utter_greet
* restaurant_search{"location": "Mumbai", "cuisine": "chinese"}
  - action_location_valid
  - slot{"location_validity" : "valid"}  
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}
  - utter_ask_price
* inform_price{"price": "high"}
  - slot{"price": "high"}
  - action_search_restaurants
  - slot{"search_validity" : "valid", "email_response": ""}
  - utter_email_prompt
* affirm
  - utter_ask_email
* inform_email{"email": "abc@abc.com"}
  - action_send_mail
  - utter_confirm_email
* thank
  - utter_goodbye
  - action_restart

## interactive_story_20
* greet
  - utter_greet
* restaurant_search{"location": "agra", "cuisine": "italian"}
  - action_location_valid
  - slot{"location_validity" : "valid"}  
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}
  - utter_ask_price
* inform_price{"price": "med"}
  - slot{"price": "med"}
  - action_search_restaurants
  - slot{"search_validity" : "valid", "email_response": ""}  
  - utter_email_prompt
* deny
  - utter_did_that_help
* affirm
  - utter_happy
  - utter_goodbye
  - action_restart

## interactive_story_21
* greet
  - utter_greet
* restaurant_search{"location": "agra", "cuisine": "italian"}
  - action_location_valid
  - slot{"location_validity" : "valid"}  
  - action_cuisine_valid
  - slot{"cuisine_validity" : "invalid"}
  - utter_cuisine_invalid
  - utter_ask_cuisine_retry
* affirm
  - utter_ask_cuisine
* restaurant_search{"cuisine": "Chinese"}
  - utter_ask_price
* inform_price{"price": "med"}
  - slot{"price": "med"}
  - action_search_restaurants
  - slot{"search_validity" : "valid", "email_response": ""}  
  - utter_email_prompt
* deny
  - utter_did_that_help
* affirm
  - utter_happy
  - utter_goodbye
  - action_restart

## interactive_story_22
* greet
  - utter_greet
* restaurant_search{"location": "agra", "cuisine": "italian"}
  - action_location_valid
  - slot{"location_validity" : "valid"}  
  - action_cuisine_valid
  - slot{"cuisine_validity" : "invalid"}
  - utter_cuisine_invalid
  - utter_ask_cuisine_retry
* deny
  - utter_deny
  - utter_goodbye
  - action_restart

## interactive_story_23
* restaurant_search{"cuisine":"indian","location":"Mysore"}
  - action_location_valid
  - slot{"location_validity" : "valid"}  
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}
  - utter_ask_price
* inform_price{"price":"high"}
  - action_search_restaurants
  - slot{"search_validity" : "valid", "email_response": ""}
  - utter_email_prompt
* deny
  - utter_deny
* thank
  - utter_goodbye
  - action_restart

## interactive_story_24
* restaurant_search{"cuisine":"indian","location":"Mysore"}
  - action_location_valid
  - slot{"location_validity" : "valid"}  
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}
  - utter_ask_price
* inform_price{"price":"high"}
  - action_search_restaurants
  - slot{"search_validity" : "valid", "email_response": ""}
  - utter_email_prompt
* affirm
  - utter_ask_email
* inform_email{"email": "abc@abc.com"}
  - action_send_mail
  - utter_confirm_email
* thank
  - utter_goodbye
  - action_restart

## interactive_story_25
* restaurant_search{"cuisine":"indian","location":"Mysore"}
  - action_location_valid
  - slot{"location_validity" : "valid"}  
  - action_cuisine_valid
  - slot{"cuisine_validity" : "invalid"}
  - utter_cuisine_invalid
  - utter_ask_cuisine_retry
* affirm
  - utter_ask_cuisine
* restaurant_search{"cuisine": "Chinese"}
  - utter_ask_price
* inform_price{"price":"high"}
  - action_search_restaurants
  - slot{"search_validity" : "valid", "email_response": ""}
  - utter_email_prompt
* deny
  - utter_deny
  - utter_goodbye
  - action_restart

## interactive_story_26
* restaurant_search{"cuisine":"indian","location":"Mysore"}
  - action_location_valid
  - slot{"location_validity" : "valid"}  
  - action_cuisine_valid
  - slot{"cuisine_validity" : "invalid"}
  - utter_cuisine_invalid
  - utter_ask_cuisine_retry
* affirm
  - utter_ask_cuisine
* restaurant_search{"cuisine": "Chinese"}
  - utter_ask_price
* inform_price{"price":"high"}
  - action_search_restaurants
  - slot{"search_validity" : "valid", "email_response": ""}
  - utter_email_prompt
* affirm
  - utter_ask_email
* inform_email{"email": "abc@abc.com"}
  - action_send_mail
  - utter_confirm_email
  - utter_goodbye
  - action_restart

## interactive_story_27
* greet
  - utter_greet
* restaurant_search{"cuisine": "indian"}
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}
  - utter_ask_location
* restaurant_search{"location": "Patna"}
  - action_location_valid
  - slot{"location_validity" : "valid"}
  - utter_ask_price
* inform_price{"price": "med"}
  - slot{"price": "med"}
  - action_search_restaurants
  - slot{"search_validity" : "valid", "email_response": ""}
  - utter_email_prompt
* affirm
  - utter_ask_email
* inform_email{"email": "abc@abc.com"}
  - action_send_mail
  - utter_confirm_email
* thank
  - utter_goodbye
  - action_restart

## interactive_story_28
* greet
  - utter_greet
* restaurant_search{"cuisine": "indian"}
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}
  - utter_ask_location
* restaurant_search{"location": "Patna"}
  - action_location_valid
  - slot{"location_validity" : "valid"}
  - utter_ask_price
* inform_price{"price": "med"}
  - slot{"price": "med"}
  - action_search_restaurants
  - slot{"search_validity" : "valid", "email_response": ""}
  - utter_email_prompt
* deny
  - utter_did_that_help
* affirm
  - utter_happy
  - utter_goodbye
  - action_restart

## interactive_story_29
* greet
  - utter_greet
* restaurant_search{"cuisine": "indian"}
  - action_cuisine_valid
  - slot{"cuisine_validity" : "invalid"}
  - utter_cuisine_invalid
  - utter_ask_cuisine_retry
* affirm
  - utter_ask_cuisine
* restaurant_search{"cuisine": "Chinese"}
  - utter_ask_location
* restaurant_search{"location": "Patna"}
  - action_location_valid
  - slot{"location_validity" : "valid"}
  - utter_ask_price
* inform_price{"price": "med"}
  - slot{"price": "med"}
  - action_search_restaurants
  - slot{"search_validity" : "valid", "email_response": ""}
  - utter_email_prompt
* deny
  - utter_did_that_help
* affirm
  - utter_happy
  - utter_goodbye
  - action_restart

## interactive_story_30
* greet
  - utter_greet
* restaurant_search{"cuisine": "indian"}
  - action_cuisine_valid
  - slot{"cuisine_validity" : "invalid"}
  - utter_cuisine_invalid
  - utter_ask_cuisine_retry
* affirm
  - utter_ask_cuisine
* restaurant_search{"cuisine": "Chinese"}
  - utter_ask_location
* restaurant_search{"location": "Patna"}
  - action_location_valid
  - slot{"location_validity" : "valid"}
  - utter_ask_price
* inform_price{"price": "med"}
  - slot{"price": "med"}
  - action_search_restaurants
  - slot{"search_validity" : "valid", "email_response": ""}
  - utter_email_prompt
* affirm
  - utter_ask_email
* inform_email{"email": "abc@abc.com"}
  - action_send_mail
  - utter_confirm_email
* thank
  - utter_goodbye
  - action_restart

## interactive_story_31
* greet
  - utter_greet
* restaurant_search{"cuisine": "indian"}
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}
  - utter_ask_location
* restaurant_search{"location": "Patna"}
  - action_location_valid
  - slot{"location_validity" : "invalid"}
  - utter_location_invalid
  - utter_ask_location_retry
* affirm
  - utter_ask_location  
* restaurant_search{"location": "Bangalore"}
  - action_location_valid
  - slot{"location_validity" : "valid"}
  - utter_ask_price
* inform_price{"price": "all"}
  - slot{"price": "all"}
  - action_search_restaurants
  - slot{"search_validity" : "valid", "email_response": ""}
  - utter_email_prompt
* affirm
  - utter_ask_email
* inform_email{"email": "abc@abc.com"}
  - action_send_mail
  - utter_confirm_email
* thank
  - utter_goodbye
  - action_restart

## interactive_story_32
* greet
  - utter_greet
* restaurant_search{"cuisine": "indian"}
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}
  - utter_ask_location
* restaurant_search{"location": "Patna"}
  - action_location_valid
  - slot{"location_validity" : "invalid"}
  - utter_location_invalid
  - utter_ask_location_retry
* affirm
  - utter_ask_location  
* restaurant_search{"location": "Bangalore"}
  - action_location_valid
  - slot{"location_validity" : "valid"}
  - utter_ask_price
* inform_price{"price": "all"}
  - slot{"price": "all"}
  - action_search_restaurants
  - slot{"search_validity" : "valid", "email_response": ""}
  - utter_email_prompt
* deny
  - utter_did_that_help
* affirm
  - utter_happy
  - utter_goodbye
  - action_restart

## interactive_story_33
* restaurant_search{"cuisine": "indian"}
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}
  - utter_ask_location
* restaurant_search{"location": "Patna"}
  - action_location_valid
  - slot{"location_validity" : "valid"}
  - utter_ask_price
* inform_price{"price": "med"}
  - slot{"price": "med"}
  - action_search_restaurants
  - slot{"search_validity" : "valid", "email_response": ""}
  - utter_email_prompt
* affirm
  - utter_ask_email
* inform_email{"email": "abc@abc.com"}
  - action_send_mail
  - utter_confirm_email
  - utter_goodbye
  - action_restart

## interactive_story_34
* restaurant_search{"cuisine": "indian"}
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}
  - utter_ask_location
* restaurant_search{"location": "Patna"}
  - action_location_valid
  - slot{"location_validity" : "valid"}
  - utter_ask_price
* inform_price{"price": "med"}
  - slot{"price": "med"}
  - action_search_restaurants
  - slot{"search_validity" : "valid", "email_response": ""}
  - utter_email_prompt
* deny
  - utter_did_that_help
* affirm
  - utter_happy
  - utter_goodbye
  - action_restart

## interactive_story_35
* restaurant_search{"cuisine": "indian"}
  - action_cuisine_valid
  - slot{"cuisine_validity" : "invalid"}
  - utter_cuisine_invalid
  - utter_ask_cuisine_retry
* affirm
  - utter_ask_cuisine
* restaurant_search{"cuisine": "Chinese"}
  - utter_ask_location
* restaurant_search{"location": "Patna"}
  - action_location_valid
  - slot{"location_validity" : "valid"}
  - utter_ask_price
* inform_price{"price": "med"}
  - slot{"price": "med"}
  - action_search_restaurants
  - slot{"search_validity" : "valid", "email_response": ""}
  - utter_email_prompt
* deny
  - utter_did_that_help
* affirm
  - utter_happy
  - utter_goodbye
  - action_restart

## interactive_story_36
* restaurant_search{"cuisine": "indian"}
  - action_cuisine_valid
  - slot{"cuisine_validity" : "invalid"}
  - utter_cuisine_invalid
  - utter_ask_cuisine_retry
* affirm
  - utter_ask_cuisine
* restaurant_search{"cuisine": "Chinese"}
  - utter_ask_location
* restaurant_search{"location": "Patna"}
  - action_location_valid
  - slot{"location_validity" : "valid"}
  - utter_ask_price
* inform_price{"price": "med"}
  - slot{"price": "med"}
  - action_search_restaurants
  - slot{"search_validity" : "valid", "email_response": ""}
  - utter_email_prompt
* affirm
  - utter_ask_email
* inform_email{"email": "abc@abc.com"}
  - action_send_mail
  - utter_confirm_email
  - utter_goodbye
  - action_restart

## interactive_story_37
* restaurant_search{"cuisine": "indian"}
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}
  - utter_ask_location
* restaurant_search{"location": "Patna"}
  - action_location_valid
  - slot{"location_validity" : "invalid"}
  - utter_location_invalid
  - utter_ask_location_retry
* affirm
  - utter_ask_location  
* restaurant_search{"location": "Bangalore"}
  - action_location_valid
  - slot{"location_validity" : "valid"}
  - utter_ask_price
* inform_price{"price": "all"}
  - slot{"price": "med"}
  - action_search_restaurants
  - slot{"search_validity" : "valid", "email_response": ""}
  - utter_email_prompt
* affirm
  - utter_ask_email
* inform_email{"email": "abc@abc.com"}
  - action_send_mail
  - utter_confirm_email
  - utter_goodbye
  - action_restart

## interactive_story_38
* restaurant_search{"cuisine": "indian"}
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}
  - utter_ask_location
* restaurant_search{"location": "Patna"}
  - action_location_valid
  - slot{"location_validity" : "invalid"}
  - utter_location_invalid
  - utter_ask_location_retry
* affirm
  - utter_ask_location  
* restaurant_search{"location": "Bangalore"}
  - action_location_valid
  - slot{"location_validity" : "valid"}
  - utter_ask_price
* inform_price{"price": "all"}
  - slot{"price": "all"}
  - action_search_restaurants
  - slot{"search_validity" : "valid", "email_response": ""}
  - utter_email_prompt
* deny
  - utter_did_that_help
* affirm
  - utter_happy
  - utter_goodbye
  - action_restart

## interactive_story_39
* greet
  - utter_greet
* restaurant_search{"location": "Patna"}
  - action_location_valid
  - slot{"location_validity" : "valid"}
  - utter_ask_cuisine
* restaurant_search{"cuisine": "indian"}
  - utter_ask_price
* inform_price{"price": "all"}
  - slot{"price": "all"}
  - action_search_restaurants
  - slot{"search_validity" : "valid", "email_response": ""}
  - utter_email_prompt
* affirm
  - utter_ask_email
* inform_email{"email": "abc@abc.com"}
  - action_send_mail
  - utter_confirm_email
* thank
  - utter_goodbye
  - action_restart

## interactive_story_40
* greet
  - utter_greet
* restaurant_search{"location": "Patna"}
  - action_location_valid
  - slot{"location_validity" : "valid"}
  - utter_ask_cuisine
* restaurant_search{"cuisine": "indian"}
  - utter_ask_price
* inform_price{"price": "all"}
  - slot{"price": "all"}
  - action_search_restaurants
  - slot{"search_validity" : "valid", "email_response": ""}
  - utter_email_prompt
* deny
  - utter_did_that_help
* affirm
  - utter_happy
  - utter_goodbye
  - action_restart

## interactive_story_41
* greet
  - utter_greet
* restaurant_search{"location": "Patna"}
  - action_location_valid
  - slot{"location_validity" : "invalid"}
  - utter_location_invalid
  - utter_ask_location_retry
* affirm
  - utter_ask_location
* restaurant_search{"location": "Patna"}
  - action_location_valid
  - slot{"location_validity" : "valid"}
  - utter_ask_cuisine
* restaurant_search{"cuisine": "Chinese"}
  - utter_ask_price
* inform_price{"price": "all"}
  - slot{"price": "all"}
  - action_search_restaurants
  - slot{"search_validity" : "valid", "email_response": ""}
  - utter_email_prompt
* deny
  - utter_did_that_help
* affirm
  - utter_happy
  - utter_goodbye
  - action_restart

## interactive_story_42
* greet
  - utter_greet
* restaurant_search{"location": "Patna"}
  - action_location_valid
  - slot{"location_validity" : "invalid"}
  - utter_location_invalid
  - utter_ask_location_retry
* affirm
  - utter_ask_location
* restaurant_search{"location": "Patna"}
  - action_location_valid
  - slot{"location_validity" : "valid"}
  - utter_ask_cuisine
* restaurant_search{"cuisine": "Chinese"}
  - utter_ask_price
* inform_price{"price": "all"}
  - slot{"price": "all"}
  - action_search_restaurants
  - slot{"search_validity" : "valid", "email_response": ""}
  - utter_email_prompt
* affirm
  - utter_ask_email
* inform_email{"email": "abc@abc.com"}
  - action_send_mail
  - utter_confirm_email
  - utter_goodbye
  - action_restart

## interactive_story_43
* restaurant_search{"location": "Patna"}
  - action_location_valid
  - slot{"location_validity" : "valid"}
  - utter_ask_cuisine
* restaurant_search{"cuisine": "indian"}
  - utter_ask_price
* inform_price{"price": "all"}
  - slot{"price": "all"}
  - action_search_restaurants
  - slot{"search_validity" : "valid", "email_response": ""}
  - utter_email_prompt
* affirm
  - utter_ask_email
* inform_email{"email": "abc@abc.com"}
  - action_send_mail
  - utter_confirm_email
  - utter_goodbye
  - action_restart

## interactive_story_44
* restaurant_search{"location": "Patna"}
  - action_location_valid
  - slot{"location_validity" : "valid"}
  - utter_ask_cuisine
* restaurant_search{"cuisine": "indian"}
  - utter_ask_price
* inform_price{"price": "all"}
  - slot{"price": "all"}
  - action_search_restaurants
  - slot{"search_validity" : "valid", "email_response": ""}
  - utter_email_prompt
* deny
  - utter_did_that_help
* affirm
  - utter_happy
  - utter_goodbye
  - action_restart

## interactive_story_45
* restaurant_search{"location": "Patna"}
  - action_location_valid
  - slot{"location_validity" : "invalid"}
  - utter_location_invalid
  - utter_ask_location_retry
* affirm
  - utter_ask_location
* restaurant_search{"location": "Patna"}
  - action_location_valid
  - slot{"location_validity" : "valid"}
  - utter_ask_cuisine
* restaurant_search{"cuisine": "Chinese"}
  - utter_ask_price
* inform_price{"price": "all"}
  - slot{"price": "all"}
  - action_search_restaurants
  - slot{"search_validity" : "valid", "email_response": ""}
  - utter_email_prompt
* deny
  - utter_did_that_help
* affirm
  - utter_happy
  - utter_goodbye
  - action_restart

## interactive_story_46
* restaurant_search{"location": "Patna"}
  - action_location_valid
  - slot{"location_validity" : "invalid"}
  - utter_location_invalid
  - utter_ask_location_retry
* affirm
  - utter_ask_location
* restaurant_search{"location": "Patna"}
  - action_location_valid
  - slot{"location_validity" : "valid"}
  - utter_ask_cuisine
* restaurant_search{"cuisine": "Chinese"}
  - utter_ask_price
* inform_price{"price": "all"}
  - slot{"price": "all"}
  - action_search_restaurants
  - slot{"search_validity" : "valid", "email_response": ""}
  - utter_email_prompt
* affirm
  - utter_ask_email
* inform_email{"email": "abc@abc.com"}
  - action_send_mail
  - utter_confirm_email
* thank
  - utter_goodbye
  - action_restart

## interactive_story_47
* greet
  - utter_greet
* restaurant_search{"location": "Delhi", "cuisine": "french"}
  - action_location_valid
  - slot{"location_validity": "invalid"}
  - utter_location_invalid
  - utter_ask_location_retry
* affirm
  - action_slot_reset
  - utter_ask_location
* restaurant_search{"location": "Delhi"}
  - action_location_valid
  - slot{"location_validity": "valid"}
  - utter_ask_cuisine
* restaurant_search{"cuisine": "french"}
  - utter_ask_price
* inform_price{"price": "all"}
  - slot{"price": "all"}
  - action_search_restaurants
  - slot{"search_validity": "valid", "email_response": ""}
  - utter_email_prompt
* affirm
  - utter_ask_email
* inform_email{"email": "abc@abc.com"}
  - action_send_mail
  - utter_confirm_email
  - utter_goodbye
  - action_restart

## interactive_story_48
* greet
  - utter_greet
* restaurant_search{"location": "Vizag", "cuisine": "italian"}
  - action_location_valid
  - slot{"location_validity" : "invalid"}
  - utter_location_invalid
  - utter_ask_location_retry
* affirm
  - action_slot_reset
  - utter_ask_location
* restaurant_search{"location": "Vizag"}
  - action_location_valid
  - slot{"location_validity" : "valid"}
  - utter_ask_cuisine
* restaurant_search{"cuisine": "italian"}
  - utter_ask_price
* inform_price{"price": "all"}
  - slot{"price": "all"}
  - action_search_restaurants
  - slot{"search_validity" : "valid", "email_response": ""}
  - utter_email_prompt
* deny
  - utter_did_that_help
* affirm
  - utter_happy
  - utter_goodbye
  - action_restart

## interactive_story_49
* restaurant_search{"location": "Delhi", "cuisine": "french"}
  - action_location_valid
  - slot{"location_validity" : "invalid"}
  - utter_location_invalid
  - utter_ask_location_retry
* affirm
  - action_slot_reset
  - utter_ask_location
* restaurant_search{"location": "Delhi"}
  - action_location_valid
  - slot{"location_validity" : "valid"}
  - utter_ask_cuisine
* restaurant_search{"cuisine": "french"}
  - utter_ask_price
* inform_price{"price": "all"}
  - slot{"price": "all"}
  - action_search_restaurants
  - slot{"search_validity" : "valid", "email_response": ""}
  - utter_email_prompt
* affirm
  - utter_ask_email
* inform_email{"email": "abc@abc.com"}
  - action_send_mail
  - utter_confirm_email
  - utter_goodbye
  - action_restart

## interactive_story_50
* restaurant_search{"location": "Vizag", "cuisine": "italian"}
  - action_location_valid
  - slot{"location_validity" : "invalid"}
  - utter_location_invalid
  - utter_ask_location_retry
* affirm
  - action_slot_reset
  - utter_ask_location
* restaurant_search{"location": "Vizag"}
  - action_location_valid
  - slot{"location_validity" : "valid"}
  - utter_ask_cuisine
* restaurant_search{"cuisine": "italian"}
  - utter_ask_price
* inform_price{"price": "all"}
  - slot{"price": "all"}
  - action_search_restaurants
  - slot{"search_validity" : "valid", "email_response": ""}
  - utter_email_prompt
* deny
  - utter_did_that_help
* affirm
  - utter_happy
  - utter_goodbye
  - action_restart

## interactive_story_51
* greet
  - utter_greet
* restaurant_search
  - utter_ask_location
* restaurant_search{"location": "Bangalore"}
  - action_location_valid
  - slot{"location_validity" : "valid"}
  - utter_ask_cuisine
* restaurant_search{"cuisine": "Chinese"}
  - utter_ask_price
* inform_price{"price": "low"}
  - slot{"price": "low"}
  - action_search_restaurants
  - slot{"search_validity" : "invalid", "email_response": ""}
  - utter_search_invalid
  - utter_goodbye
  - action_restart

## interactive_story_52
* greet
  - utter_greet
* restaurant_search
  - utter_ask_location
* restaurant_search{"location": "Bangalore"}
  - action_location_valid
  - slot{"location_validity" : "invalid"}
  - utter_location_invalid
  - utter_ask_location_retry
* affirm
  - utter_ask_location  
  - action_slot_reset
* restaurant_search{"location": "Bangalore"}
  - action_location_valid
  - slot{"location_validity" : "valid"}
  - utter_ask_cuisine  
* restaurant_search{"cuisine": "Chinese"}
  - utter_ask_price
* inform_price{"price": "low"}
  - slot{"price": "low"}
  - action_search_restaurants
  - slot{"search_validity" : "invalid", "email_response": ""}
  - utter_search_invalid
  - utter_goodbye
  - action_restart

## interactive_story_53
* greet
  - utter_greet
* restaurant_search{"location": "Mumbai", "cuisine": "chinese"}
  - action_location_valid
  - slot{"location_validity" : "valid"}  
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}
  - utter_ask_price
* inform_price{"price": "high"}
  - slot{"price": "high"}
  - action_search_restaurants
  - slot{"search_validity" : "invalid", "email_response": ""}
  - utter_search_invalid
  - utter_goodbye
  - action_restart

## interactive_story_54
* greet
  - utter_greet
* restaurant_search{"location": "Mumbai", "cuisine": "chinese"}
  - action_location_valid
  - slot{"location_validity" : "valid"}  
  - action_cuisine_valid
  - slot{"cuisine_validity" : "invalid"}
  - utter_cuisine_invalid
  - utter_ask_cuisine_retry
* affirm
  - utter_ask_cuisine
* restaurant_search{"cuisine": "Chinese"}
  - utter_ask_price
* inform_price{"price": "high"}
  - slot{"price": "high"}
  - action_search_restaurants
  - slot{"search_validity" : "invalid", "email_response": ""}
  - utter_search_invalid
  - utter_goodbye
  - action_restart

## interactive_story_55
* restaurant_search{"cuisine":"indian","location":"Mysore"}
  - action_location_valid
  - slot{"location_validity" : "valid"}  
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}
  - utter_ask_price
* inform_price{"price":"high"}
  - action_search_restaurants
  - slot{"search_validity" : "valid", "email_response": ""}
  - utter_search_invalid
  - utter_goodbye
  - action_restart

## interactive_story_56
* restaurant_search{"cuisine":"indian","location":"Mysore"}
  - action_location_valid
  - slot{"location_validity" : "valid"}  
  - action_cuisine_valid
  - slot{"cuisine_validity" : "invalid"}
  - utter_cuisine_invalid
  - utter_ask_cuisine_retry
* affirm
  - utter_ask_cuisine
* restaurant_search{"cuisine": "Chinese"}
  - utter_ask_price
* inform_price{"price":"high"}
  - action_search_restaurants
  - slot{"search_validity" : "invalid", "email_response": ""}
  - utter_search_invalid
  - utter_goodbye
  - action_restart

## interactive_story_57
* greet
  - utter_greet
* restaurant_search{"cuisine": "indian"}
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}
  - utter_ask_location
* restaurant_search{"location": "Patna"}
  - action_location_valid
  - slot{"location_validity" : "valid"}
  - utter_ask_price
* inform_price{"price": "all"}
  - slot{"price": "all"}
  - action_search_restaurants
  - slot{"search_validity" : "invalid", "email_response": ""}
  - utter_search_invalid
  - utter_goodbye
  - action_restart

## interactive_story_58
* greet
  - utter_greet
* restaurant_search{"cuisine": "indian"}
  - action_cuisine_valid
  - slot{"cuisine_validity" : "invalid"}
  - utter_cuisine_invalid
  - utter_ask_cuisine_retry
* affirm
  - utter_ask_cuisine
* restaurant_search{"cuisine": "Chinese"}
  - utter_ask_location
* restaurant_search{"location": "Patna"}
  - action_location_valid
  - slot{"location_validity" : "valid"}
  - utter_ask_price
* inform_price{"price": "all"}
  - slot{"price": "all"}
  - action_search_restaurants
  - slot{"search_validity" : "invalid", "email_response": ""}
  - utter_search_invalid
  - utter_goodbye
  - action_restart

## interactive_story_59
* greet
  - utter_greet
* restaurant_search{"cuisine": "indian"}
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}
  - utter_ask_location
* restaurant_search{"location": "Patna"}
  - action_location_valid
  - slot{"location_validity" : "invalid"}
  - utter_location_invalid
  - utter_ask_location_retry
* affirm
  - utter_ask_location  
* restaurant_search{"location": "Bangalore"}
  - action_location_valid
  - slot{"location_validity" : "valid"}
  - utter_ask_price
* inform_price{"price": "all"}
  - slot{"price": "all"}
  - action_search_restaurants
  - slot{"search_validity" : "invalid", "email_response": ""}
  - utter_search_invalid
  - utter_goodbye
  - action_restart

## interactive_story_60
* restaurant_search{"cuisine": "indian"}
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}
  - utter_ask_location
* restaurant_search{"location": "Patna"}
  - action_location_valid
  - slot{"location_validity" : "valid"}
  - utter_ask_price
* inform_price{"price": "all"}
  - slot{"price": "all"}
  - action_search_restaurants
  - slot{"search_validity" : "invalid", "email_response": ""}
  - utter_search_invalid
  - utter_goodbye
  - action_restart

## interactive_story_61
* restaurant_search{"cuisine": "indian"}
  - action_cuisine_valid
  - slot{"cuisine_validity" : "invalid"}
  - utter_cuisine_invalid
  - utter_ask_cuisine_retry
* affirm
  - utter_ask_cuisine
* restaurant_search{"cuisine": "Chinese"}
  - utter_ask_location
* restaurant_search{"location": "Patna"}
  - action_location_valid
  - slot{"location_validity" : "valid"}
  - utter_ask_price
* inform_price{"price": "all"}
  - slot{"price": "all"}
  - action_search_restaurants
  - slot{"search_validity" : "invalid", "email_response": ""}
  - utter_search_invalid
  - utter_goodbye
  - action_restart

## interactive_story_62
* restaurant_search{"cuisine": "indian"}
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}
  - utter_ask_location
* restaurant_search{"location": "Patna"}
  - action_location_valid
  - slot{"location_validity" : "invalid"}
  - utter_location_invalid
  - utter_ask_location_retry
* affirm
  - utter_ask_location  
* restaurant_search{"location": "Bangalore"}
  - action_location_valid
  - slot{"location_validity" : "valid"}
  - utter_ask_price
* inform_price{"price": "all"}
  - slot{"price": "all"}
  - action_search_restaurants
  - slot{"search_validity" : "invalid", "email_response": ""}
  - utter_search_invalid
  - utter_goodbye
  - action_restart

## interactive_story_63
* greet
  - utter_greet
* restaurant_search{"location": "Patna"}
  - action_location_valid
  - slot{"location_validity" : "valid"}
  - utter_ask_cuisine
* restaurant_search{"cuisine": "indian"}
  - utter_ask_price
* inform_price{"price": "all"}
  - slot{"price": "all"}
  - action_search_restaurants
  - slot{"search_validity" : "invalid", "email_response": ""}
  - utter_search_invalid
  - utter_goodbye
  - action_restart

## interactive_story_64
* greet
  - utter_greet
* restaurant_search{"location": "Patna"}
  - action_location_valid
  - slot{"location_validity" : "invalid"}
  - utter_location_invalid
  - utter_ask_location_retry
* affirm
  - utter_ask_location
* restaurant_search{"location": "Patna"}
  - action_location_valid
  - slot{"location_validity" : "valid"}
  - utter_ask_cuisine
* restaurant_search{"cuisine": "Chinese"}
  - utter_ask_price
* inform_price{"price": "all"}
  - slot{"price": "all"}
  - action_search_restaurants
  - slot{"search_validity" : "invalid", "email_response": ""}
  - utter_search_invalid
  - utter_goodbye
  - action_restart

## interactive_story_65
* restaurant_search{"location": "Patna"}
  - action_location_valid
  - slot{"location_validity" : "valid"}
  - utter_ask_cuisine
* restaurant_search{"cuisine": "indian"}
  - utter_ask_price
* inform_price{"price": "all"}
  - slot{"price": "all"}
  - action_search_restaurants
  - slot{"search_validity" : "invalid", "email_response": ""}
  - utter_search_invalid
  - utter_goodbye
  - action_restart

## interactive_story_66
* restaurant_search{"location": "Patna"}
  - action_location_valid
  - slot{"location_validity" : "invalid"}
  - utter_location_invalid
  - utter_ask_location_retry
* affirm
  - utter_ask_location
* restaurant_search{"location": "Patna"}
  - action_location_valid
  - slot{"location_validity" : "valid"}
  - utter_ask_cuisine
* restaurant_search{"cuisine": "Chinese"}
  - utter_ask_price
* inform_price{"price": "all"}
  - slot{"price": "all"}
  - action_search_restaurants
  - slot{"search_validity" : "invalid", "email_response": ""}
  - utter_search_invalid
  - utter_goodbye
  - action_restart

## interactive_story_67
* greet
  - utter_greet
* restaurant_search{"location": "Delhi", "cuisine": "french"}
  - action_location_valid
  - slot{"location_validity": "invalid"}
  - utter_location_invalid
  - utter_ask_location_retry
* affirm
  - action_slot_reset
  - utter_ask_location
* restaurant_search{"location": "Delhi"}
  - action_location_valid
  - slot{"location_validity": "valid"}
  - utter_ask_cuisine
* restaurant_search{"cuisine": "french"}
  - utter_ask_price
* inform_price{"price": "all"}
  - slot{"price": "all"}
  - action_search_restaurants
  - slot{"search_validity" : "invalid", "email_response": ""}
  - utter_search_invalid
  - utter_goodbye
  - action_restart

## interactive_story_68
* restaurant_search{"location": "Delhi", "cuisine": "french"}
  - action_location_valid
  - slot{"location_validity" : "invalid"}
  - utter_location_invalid
  - utter_ask_location_retry
* affirm
  - action_slot_reset
  - utter_ask_location
* restaurant_search{"location": "Delhi"}
  - action_location_valid
  - slot{"location_validity" : "valid"}
  - utter_ask_cuisine
* restaurant_search{"cuisine": "french"}
  - utter_ask_price
* inform_price{"price": "all"}
  - slot{"price": "all"}
  - action_search_restaurants
  - slot{"search_validity" : "invalid", "email_response": ""}
  - utter_search_invalid
  - utter_goodbye
  - action_restart


## interactive_story_69
* greet
  - utter_greet
* restaurant_search
  - utter_ask_location
* restaurant_search{"location": "Bangalore"}
  - action_location_valid
  - slot{"location_validity" : "valid"}  
  - utter_ask_cuisine
* restaurant_search{"cuisine": "Chinese"}
  - utter_ask_price
* inform_price{"price": "low"}
  - slot{"price": "low"}
  - action_search_restaurants
  - slot{"search_validity" : "valid", "email_response": ""}  
  - utter_email_prompt
* deny
  - utter_did_that_help
* deny
  - utter_deny
  - utter_goodbye
  - action_restart

## interactive_story_70
* greet
  - utter_greet
* restaurant_search{"location": "agra", "cuisine": "italian"}
  - action_location_valid
  - slot{"location_validity" : "valid"}  
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}
  - utter_ask_price
* inform_price{"price": "all"}
  - slot{"price": "all"}
  - action_search_restaurants
  - slot{"search_validity" : "valid", "email_response": ""}  
  - utter_email_prompt
* deny
  - utter_did_that_help
* deny
  - utter_deny
  - utter_goodbye
  - action_restart

## interactive_story_71
* greet
  - utter_greet
* restaurant_search{"location": "agra", "cuisine": "italian"}
  - action_location_valid
  - slot{"location_validity" : "valid"}  
  - action_cuisine_valid
  - slot{"cuisine_validity" : "invalid"}
  - utter_cuisine_invalid
  - utter_ask_cuisine_retry
* affirm
  - utter_ask_cuisine
* restaurant_search{"cuisine": "Chinese"}
  - utter_ask_price
* inform_price{"price": "all"}
  - slot{"price": "all"}
  - action_search_restaurants
  - slot{"search_validity" : "valid", "email_response": ""}  
  - utter_email_prompt
* deny
  - utter_did_that_help
* deny
  - utter_deny
  - utter_goodbye
  - action_restart

## interactive_story_72
* greet
  - utter_greet
* restaurant_search{"cuisine": "indian"}
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}
  - utter_ask_location
* restaurant_search{"location": "Patna"}
  - action_location_valid
  - slot{"location_validity" : "valid"}
  - utter_ask_price
* inform_price{"price": "all"}
  - slot{"price": "all"}
  - action_search_restaurants
  - slot{"search_validity" : "valid", "email_response": ""}
  - utter_email_prompt
* deny
  - utter_did_that_help
* deny
  - utter_deny
  - utter_goodbye
  - action_restart

## interactive_story_73
* greet
  - utter_greet
* restaurant_search{"cuisine": "indian"}
  - action_cuisine_valid
  - slot{"cuisine_validity" : "invalid"}
  - utter_cuisine_invalid
  - utter_ask_cuisine_retry
* affirm
  - utter_ask_cuisine
* restaurant_search{"cuisine": "Chinese"}
  - utter_ask_location
* restaurant_search{"location": "Patna"}
  - action_location_valid
  - slot{"location_validity" : "valid"}
  - utter_ask_price
* inform_price{"price": "all"}
  - slot{"price": "all"}
  - action_search_restaurants
  - slot{"search_validity" : "valid", "email_response": ""}
  - utter_email_prompt
* deny
  - utter_did_that_help
* deny
  - utter_deny
  - utter_goodbye
  - action_restart

## interactive_story_74
* greet
  - utter_greet
* restaurant_search{"cuisine": "indian"}
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}
  - utter_ask_location
* restaurant_search{"location": "Patna"}
  - action_location_valid
  - slot{"location_validity" : "invalid"}
  - utter_location_invalid
  - utter_ask_location_retry
* affirm
  - utter_ask_location  
* restaurant_search{"location": "Bangalore"}
  - action_location_valid
  - slot{"location_validity" : "valid"}
  - utter_ask_price
* inform_price{"price": "all"}
  - slot{"price": "all"}
  - action_search_restaurants
  - slot{"search_validity" : "valid", "email_response": ""}
  - utter_email_prompt
* deny
  - utter_did_that_help
* deny
  - utter_deny
  - utter_goodbye
  - action_restart

## interactive_story_75
* restaurant_search{"cuisine": "indian"}
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}
  - utter_ask_location
* restaurant_search{"location": "Patna"}
  - action_location_valid
  - slot{"location_validity" : "valid"}
  - utter_ask_price
* inform_price{"price": "all"}
  - slot{"price": "all"}
  - action_search_restaurants
  - slot{"search_validity" : "valid", "email_response": ""}
  - utter_email_prompt
* deny
  - utter_did_that_help
* deny
  - utter_deny
  - utter_goodbye
  - action_restart

## interactive_story_76
* restaurant_search{"cuisine": "indian"}
  - action_cuisine_valid
  - slot{"cuisine_validity" : "invalid"}
  - utter_cuisine_invalid
  - utter_ask_cuisine_retry
* affirm
  - utter_ask_cuisine
* restaurant_search{"cuisine": "Chinese"}
  - utter_ask_location
* restaurant_search{"location": "Patna"}
  - action_location_valid
  - slot{"location_validity" : "valid"}
  - utter_ask_price
* inform_price{"price": "all"}
  - slot{"price": "all"}
  - action_search_restaurants
  - slot{"search_validity" : "valid", "email_response": ""}
  - utter_email_prompt
* deny
  - utter_did_that_help
* deny
  - utter_deny
  - utter_goodbye
  - action_restart

## interactive_story_77
* restaurant_search{"cuisine": "indian"}
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}
  - utter_ask_location
* restaurant_search{"location": "Patna"}
  - action_location_valid
  - slot{"location_validity" : "invalid"}
  - utter_location_invalid
  - utter_ask_location_retry
* affirm
  - utter_ask_location  
* restaurant_search{"location": "Bangalore"}
  - action_location_valid
  - slot{"location_validity" : "valid"}
  - utter_ask_price
* inform_price{"price": "all"}
  - slot{"price": "all"}
  - action_search_restaurants
  - slot{"search_validity" : "valid", "email_response": ""}
  - utter_email_prompt
* deny
  - utter_did_that_help
* deny
  - utter_deny
  - utter_goodbye
  - action_restart

## interactive_story_78
* greet
  - utter_greet
* restaurant_search{"location": "Vizag", "cuisine": "italian"}
  - action_location_valid
  - slot{"location_validity" : "invalid"}
  - utter_location_invalid
  - utter_ask_location_retry
* affirm
  - action_slot_reset
  - utter_ask_location
* restaurant_search{"location": "Vizag"}
  - action_location_valid
  - slot{"location_validity" : "valid"}
  - utter_ask_cuisine
* restaurant_search{"cuisine": "italian"}
  - utter_ask_price
* inform_price{"price": "all"}
  - slot{"price": "all"}
  - action_search_restaurants
  - slot{"search_validity" : "valid", "email_response": ""}
  - utter_email_prompt
* deny
  - utter_did_that_help
* deny
  - utter_deny
  - utter_goodbye
  - action_restart

## interactive_story_79
* greet
  - utter_greet
* restaurant_search{"location": "Patna"}
  - action_location_valid
  - slot{"location_validity" : "valid"}
  - utter_ask_cuisine
* restaurant_search{"cuisine": "indian"}
  - utter_ask_price
* inform_price{"price": "all"}
  - slot{"price": "all"}
  - action_search_restaurants
  - slot{"search_validity" : "valid", "email_response": ""}
  - utter_email_prompt
* deny
  - utter_did_that_help
* deny
  - utter_deny
  - utter_goodbye
  - action_restart

## interactive_story_80
* greet
  - utter_greet
* restaurant_search{"location": "Patna"}
  - action_location_valid
  - slot{"location_validity" : "invalid"}
  - utter_location_invalid
  - utter_ask_location_retry
* affirm
  - utter_ask_location
* restaurant_search{"location": "Patna"}
  - action_location_valid
  - slot{"location_validity" : "valid"}
  - utter_ask_cuisine
* restaurant_search{"cuisine": "Chinese"}
  - utter_ask_price
* inform_price{"price": "all"}
  - slot{"price": "all"}
  - action_search_restaurants
  - slot{"search_validity" : "valid", "email_response": ""}
  - utter_email_prompt
* deny
  - utter_did_that_help
* deny
  - utter_deny
  - utter_goodbye
  - action_restart

## interactive_story_81
* restaurant_search{"location": "Patna"}
  - action_location_valid
  - slot{"location_validity" : "valid"}
  - utter_ask_cuisine
* restaurant_search{"cuisine": "indian"}
  - utter_ask_price
* inform_price{"price": "all"}
  - slot{"price": "all"}
  - action_search_restaurants
  - slot{"search_validity" : "valid", "email_response": ""}
  - utter_email_prompt
* deny
  - utter_did_that_help
* deny
  - utter_deny
  - utter_goodbye
  - action_restart

## interactive_story_82
* restaurant_search{"location": "Patna"}
  - action_location_valid
  - slot{"location_validity" : "invalid"}
  - utter_location_invalid
  - utter_ask_location_retry
* affirm
  - utter_ask_location
* restaurant_search{"location": "Patna"}
  - action_location_valid
  - slot{"location_validity" : "valid"}
  - utter_ask_cuisine
* restaurant_search{"cuisine": "Chinese"}
  - utter_ask_price
* inform_price{"price": "all"}
  - slot{"price": "all"}
  - action_search_restaurants
  - slot{"search_validity" : "valid", "email_response": ""}
  - utter_email_prompt
* deny
  - utter_did_that_help
* deny
  - utter_deny
  - utter_goodbye
  - action_restart

## interactive_story_83
* greet
  - utter_greet
* goodbye
  - utter_goodbye
  - action_restart

## interactive_story_84
* restaurant_search
  - utter_ask_location
* goodbye
  - utter_goodbye
  - action_restart

## interactive_story_85
* restaurant_search{"location": "delhi"}
  - action_location_valid
  - slot{"location_validity" : "invalid"}
  - utter_location_invalid
  - utter_ask_location_retry
* goodbye
  - utter_goodbye
  - action_restart

## interactive_story_86
* restaurant_search
  - utter_ask_location
* restaurant_search{"location": "delhi"}
  - action_location_valid
  - slot{"location_validity" : "invalid"}
  - utter_location_invalid
  - utter_ask_location_retry
* affirm
  - action_slot_reset
  - utter_ask_location  
* restaurant_search{"location": "Bangalore"}
  - action_location_valid
  - slot{"location_validity" : "valid"}
  - utter_ask_cuisine
* restaurant_search{"cuisine": "Chinese"}
  - utter_ask_price
* inform_price{"price": "all"}
  - slot{"price": "all"}
  - action_search_restaurants
  - slot{"search_validity" : "valid", "email_response": ""}
  - utter_email_prompt
* goodbye
  - utter_goodbye
  - action_restart

## interactive_story_87
* restaurant_search{"location": "delhi"}
  - action_location_valid
  - slot{"location_validity" : "invalid"}
  - utter_location_invalid
  - utter_ask_location_retry
* affirm
  - action_slot_reset
  - utter_ask_location  
* restaurant_search{"location": "Bangalore"}
  - action_location_valid
  - slot{"location_validity" : "valid"}
  - utter_ask_cuisine
* goodbye
  - utter_goodbye
  - action_restart

## interactive_story_88
* greet
  - utter_greet
* restaurant_search
  - utter_ask_location
* goodbye
  - utter_goodbye
  - action_restart

## interactive_story_89
* restaurant_search
  - utter_ask_location
* restaurant_search{"location": "delhi"}
  - action_location_valid
  - slot{"location_validity" : "invalid"}
  - utter_location_invalid
  - utter_ask_location_retry
* affirm
  - action_slot_reset
  - utter_ask_location  
* restaurant_search{"location": "Bangalore"}
  - action_location_valid
  - slot{"location_validity" : "valid"}
  - utter_ask_cuisine
* restaurant_search{"cuisine": "Chinese"}
  - utter_ask_price
* inform_price{"price": "all"}
  - slot{"price": "all"}
  - action_search_restaurants
  - slot{"search_validity" : "valid", "email_response": ""}
  - utter_email_prompt
* goodbye
  - utter_goodbye
  - action_restart



## interactive_story_90
* restaurant_search
  - utter_ask_location
* restaurant_search{"location": "delhi"}
  - action_location_valid
  - slot{"location_validity" : "invalid"}
  - utter_location_invalid
  - utter_ask_location_retry
* affirm
  - action_slot_reset
  - utter_ask_location  
* restaurant_search{"location": "Bangalore"}
  - action_location_valid
  - slot{"location_validity" : "valid"}
  - utter_ask_cuisine
* restaurant_search{"cuisine": "Chinese"}
  - utter_ask_price
* inform_price{"price": "all"}
  - slot{"price": "all"}
  - action_search_restaurants
  - slot{"search_validity" : "valid", "email_response": ""}
  - utter_email_prompt
* deny
  - utter_goodbye
  - action_restart

## interactive_story_91
* restaurant_search
  - utter_ask_location
* restaurant_search{"location": "delhi"}
  - action_location_valid
  - slot{"location_validity" : "invalid"}
  - utter_location_invalid
  - utter_ask_location_retry
* affirm
  - action_slot_reset
  - utter_ask_location  
* restaurant_search{"location": "Bangalore"}
  - action_location_valid
  - slot{"location_validity" : "valid"}
  - utter_ask_cuisine
* restaurant_search{"cuisine": "Chinese"}
  - utter_ask_price
* inform_price{"price": "all"}
  - slot{"price": "all"}
  - action_search_restaurants
  - slot{"search_validity" : "valid", "email_response": ""}
  - utter_email_prompt
* affirm
  - utter_ask_email
* inform_email{"email": "abc@abc.com"}
  - action_send_mail
  - utter_confirm_email
  - utter_goodbye
  - action_restart

## interactive_story_92
* restaurant_search{"location":"Kolkata", "cuisine":"mexican"}
  - action_location_valid
  - slot{"location_validity" : "invalid"}
  - utter_location_invalid
  - utter_ask_location_retry
* affirm
  - utter_ask_location  
* restaurant_search{"location": "Bangalore"}
  - action_location_valid
  - slot{"location_validity" : "valid"}
  - utter_ask_cuisine
* restaurant_search{"cuisine":"mexican"}
  - utter_ask_price
* inform_price{"price": "all"}
  - slot{"price": "all"}
  - action_search_restaurants
  - slot{"search_validity" : "valid", "email_response": ""}
  - utter_email_prompt
* affirm
  - utter_ask_email
* inform_email{"email": "abc@abc.com"}
  - action_send_mail
  - utter_confirm_email
  - utter_goodbye
  - action_restart

## interactive_story_93
* greet
  - utter_greet
* restaurant_search{"location": "Mumbai", "cuisine": "chinese"}
  - action_location_valid
  - slot{"location_validity" : "valid"}  
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}
  - utter_ask_price
* inform_price{"price": "high"}
  - slot{"price": "high"}
  - action_search_restaurants
  - slot{"search_validity" : "valid", "email_response": ""}
  - utter_email_prompt
* inform_email{"email": "abc@abc.com"}
  - action_send_mail
  - utter_confirm_email
* thank
  - utter_goodbye
  - action_restart

## interactive_story_94
* restaurant_search{"cuisine":"indian","location":"Mysore"}
  - action_location_valid
  - slot{"location_validity" : "valid"}  
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}
  - utter_ask_price
* inform_price{"price":"high"}
  - action_search_restaurants
  - slot{"search_validity" : "valid", "email_response": ""}
  - utter_email_prompt
* inform_email{"email": "abc@abc.com"}
  - action_send_mail
  - utter_confirm_email
* thank
  - utter_goodbye
  - action_restart

## interactive_story_95
* greet
  - utter_greet
* restaurant_search
  - utter_ask_location
* restaurant_search{"location": "Bangalore"}
  - action_location_valid
  - slot{"location_validity" : "valid"}
  - utter_ask_cuisine
* restaurant_search{"cuisine": "Chinese"}
  - utter_ask_price
* inform_price{"price": "low"}
  - slot{"price": "low"}
  - action_search_restaurants
  - slot{"search_validity" : "valid", "email_response": ""}
  - utter_email_prompt
* inform_email{"email": "abc@abc.com"}
  - action_send_mail
  - utter_confirm_email
* thank
  - utter_goodbye
  - action_restart


## interactive_story_96
* greet
  - utter_greet
* restaurant_search{"location": "Delhi", "cuisine": "french"}
  - action_location_valid
  - slot{"location_validity": "invalid"}
  - utter_location_invalid
  - utter_ask_location_retry
* affirm
  - action_slot_reset
  - utter_ask_location
* restaurant_search{"location": "Delhi"}
  - action_location_valid
  - slot{"location_validity": "valid"}
  - utter_ask_cuisine
* restaurant_search{"cuisine": "french"}
  - utter_ask_price
* inform_price{"price": "med"}
  - slot{"price": "med"}
  - action_search_restaurants
  - slot{"search_validity": "valid", "email_response": ""}
  - utter_email_prompt
* inform_email{"email": "abc@abc.com"}
  - action_send_mail
  - utter_confirm_email
  - utter_goodbye
  - action_restart

## interactive_story_97
* greet
  - utter_greet
* restaurant_search
  - utter_ask_location
* restaurant_search{"location": "Bangalore"}
  - action_location_valid
  - slot{"location_validity" : "invalid"}
  - utter_location_invalid
  - utter_ask_location_retry
  - action_slot_reset
* restaurant_search{"location": "Bangalore"}
  - action_location_valid
  - slot{"location_validity" : "valid"}
  - utter_ask_cuisine  
* restaurant_search{"cuisine": "Chinese"}
  - utter_ask_price
* inform_price{"price": "low"}
  - slot{"price": "low"}
  - action_search_restaurants
  - slot{"search_validity" : "valid", "email_response": ""}
  - utter_email_prompt
* affirm
  - utter_ask_email
* inform_email{"email": "abc@abc.com"}
  - action_send_mail
  - utter_confirm_email
* thank
  - utter_goodbye
  - action_restart

## interactive_story_98
* greet
  - utter_greet
* restaurant_search{"cuisine": "indian"}
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}
  - utter_ask_location
* restaurant_search{"location": "Patna"}
  - action_location_valid
  - slot{"location_validity" : "invalid"}
  - utter_location_invalid
  - utter_ask_location_retry
* restaurant_search{"location": "Bangalore"}
  - action_location_valid
  - slot{"location_validity" : "valid"}
*   - utter_ask_price
inform_price{"price": "all"}
  - slot{"price": "all"}
  - action_search_restaurants
  - slot{"search_validity" : "valid", "email_response": ""}
  - utter_email_prompt
* affirm
  - utter_ask_email
* inform_email{"email": "abc@abc.com"}
  - action_send_mail
  - utter_confirm_email
* thank
  - utter_goodbye
  - action_restart

## interactive_story_99
* greet
  - utter_greet
* restaurant_search{"cuisine": "indian"}
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}
  - utter_ask_location
* restaurant_search{"location": "Patna"}
  - action_location_valid
  - slot{"location_validity" : "invalid"}
  - utter_location_invalid
  - utter_ask_location_retry
* restaurant_search{"location": "Bangalore"}
  - action_location_valid
  - slot{"location_validity" : "valid"}
  - utter_ask_price
* inform_price{"price": "all"}
  - slot{"price": "all"}
  - action_search_restaurants
  - slot{"search_validity" : "valid", "email_response": ""}
  - utter_email_prompt
* deny
  - utter_happy
  - utter_goodbye
  - action_restart

## interactive_story_100
* restaurant_search{"cuisine": "indian"}
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}
  - utter_ask_location
* restaurant_search{"location": "Patna"}
  - action_location_valid
  - slot{"location_validity" : "invalid"}
  - utter_location_invalid
  - utter_ask_location_retry
* restaurant_search{"location": "Bangalore"}
  - action_location_valid
  - slot{"location_validity" : "valid"}
  - utter_ask_price
* inform_price{"price": "all"}
  - slot{"price": "all"}
  - action_search_restaurants
  - slot{"search_validity" : "valid", "email_response": ""}
  - utter_email_prompt
* inform_email{"email": "abc@abc.com"}
  - action_send_mail
  - utter_confirm_email
  - utter_goodbye
  - action_restart

## interactive_story_101
* greet
  - utter_greet
* restaurant_search{"location": "Patna"}
  - action_location_valid
  - slot{"location_validity" : "invalid"}
  - utter_location_invalid
  - utter_ask_location_retry
* restaurant_search{"location": "Patna"}
  - action_location_valid
  - slot{"location_validity" : "valid"}
  - utter_ask_cuisine
* restaurant_search{"cuisine": "Chinese"}
  - utter_ask_price
* inform_price{"price": "med"}
  - slot{"price": "med"}
  - action_search_restaurants
  - slot{"search_validity" : "valid", "email_response": ""}
  - utter_email_prompt
* deny
  - utter_goodbye
  - action_restart

## interactive_story_102
* greet
  - utter_greet
* restaurant_search{"location": "Patna"}
  - action_location_valid
  - slot{"location_validity" : "invalid"}
  - utter_location_invalid
  - utter_ask_location_retry
* restaurant_search{"location": "Patna"}
  - action_location_valid
  - slot{"location_validity" : "valid"}
  - utter_ask_cuisine
* restaurant_search{"cuisine": "Chinese"}
  - utter_ask_price
* inform_price{"price": "med"}
  - slot{"price": "med"}
  - action_search_restaurants
  - slot{"search_validity" : "valid", "email_response": ""}
  - utter_email_prompt
* inform_email{"email": "abc@abc.com"}
  - action_send_mail
  - utter_confirm_email
  - utter_goodbye
  - action_restart

## interactive_story_103
* restaurant_search{"location": "Patna"}
  - action_location_valid
  - slot{"location_validity" : "invalid"}
  - utter_location_invalid
  - utter_ask_location_retry
* restaurant_search{"location": "Patna"}
  - action_location_valid
  - slot{"location_validity" : "valid"}
  - utter_ask_cuisine
* restaurant_search{"cuisine": "Chinese"}
  - utter_ask_price
* inform_price{"price": "med"}
  - slot{"price": "med"}
  - action_search_restaurants
  - slot{"search_validity" : "valid", "email_response": ""}
  - utter_email_prompt
* deny
  - utter_happy
  - utter_goodbye
  - action_restart

## interactive_story_104
* restaurant_search{"location": "Patna"}
  - action_location_valid
  - slot{"location_validity" : "invalid"}
  - utter_location_invalid
  - utter_ask_location_retry
* restaurant_search{"location": "Patna"}
  - action_location_valid
  - slot{"location_validity" : "valid"}
  - utter_ask_cuisine
* restaurant_search{"cuisine": "Chinese"}
  - utter_ask_price
* inform_price{"price": "med"}
  - slot{"price": "med"}
  - action_search_restaurants
  - slot{"search_validity" : "valid", "email_response": ""}
  - utter_email_prompt
* inform_email{"email": "abc@abc.com"}
  - action_send_mail
  - utter_confirm_email
* thank
  - utter_happy
  - utter_goodbye
  - action_restart

## interactive_story_105
* greet
  - utter_greet
* restaurant_search{"location": "Vizag", "cuisine": "italian"}
  - action_location_valid
  - slot{"location_validity" : "invalid"}
  - utter_location_invalid
  - utter_ask_location_retry
  - action_slot_reset
* restaurant_search{"location": "Vizag"}
  - action_location_valid
  - slot{"location_validity" : "valid"}
  - utter_ask_cuisine
* restaurant_search{"cuisine": "italian"}
  - utter_ask_price
* inform_price{"price": "med"}
  - slot{"price": "med"}
  - action_search_restaurants
  - slot{"search_validity" : "valid", "email_response": ""}
  - utter_email_prompt
* deny
  - utter_did_that_help
* affirm
  - utter_happy
  - utter_goodbye
  - action_restart

## interactive_story_106
* restaurant_search{"location": "Delhi", "cuisine": "french"}
  - action_location_valid
  - slot{"location_validity" : "invalid"}
  - utter_location_invalid
  - utter_ask_location_retry
  - action_slot_reset
* restaurant_search{"location": "Delhi"}
  - action_location_valid
  - slot{"location_validity" : "valid"}
  - utter_ask_cuisine
* restaurant_search{"cuisine": "french"}
  - utter_ask_price
* inform_price{"price": "med"}
  - slot{"price": "med"}
  - action_search_restaurants
  - slot{"search_validity" : "valid", "email_response": ""}
  - utter_email_prompt
* inform_email{"email": "abc@abc.com"}
  - action_send_mail
  - utter_confirm_email
  - utter_goodbye
  - action_restart

## interactive_story_107
* greet
  - utter_greet
* restaurant_search{"location": "agra", "cuisine": "italian"}
  - action_location_valid
  - slot{"location_validity" : "valid"}  
  - action_cuisine_valid
  - slot{"cuisine_validity" : "invalid"}
  - utter_cuisine_invalid
  - utter_ask_cuisine_retry
* restaurant_search{"cuisine": "Chinese"}
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}
  - utter_ask_price
* inform_price{"price": "med"}
  - slot{"price": "med"}
  - action_search_restaurants
  - slot{"search_validity" : "valid", "email_response": ""}  
  - utter_email_prompt
* deny
  - utter_did_that_help
* deny
  - utter_deny
  - utter_goodbye
  - action_restart

## interactive_story_108
* restaurant_search{"location": "agra", "cuisine": "italian"}
  - action_location_valid
  - slot{"location_validity" : "valid"}  
  - action_cuisine_valid
  - slot{"cuisine_validity" : "invalid"}
  - utter_cuisine_invalid
  - utter_ask_cuisine_retry
* restaurant_search{"cuisine": "Chinese"}
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}
  - utter_ask_price
* inform_price{"price": "med"}
  - slot{"price": "med"}
  - action_search_restaurants
  - slot{"search_validity" : "valid", "email_response": ""}  
  - utter_email_prompt
* deny
  - utter_did_that_help
* deny
  - utter_deny
  - utter_goodbye
  - action_restart

## interactive_story_109
* greet
  - utter_greet
* restaurant_search{"location": "agra", "cuisine": "italian"} 
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}
  - action_location_valid
  - slot{"location_validity" : "invalid"}
  - utter_location_invalid
  - utter_ask_location_retry
* restaurant_search{"location": "agra"}
  - action_location_valid
  - slot{"location_validity" : "valid"}
  - utter_ask_price
* inform_price{"price": "med"}
  - slot{"price": "med"}
  - action_search_restaurants
  - slot{"search_validity" : "valid", "email_response": ""}  
  - utter_email_prompt
* deny
  - utter_did_that_help
* deny
  - utter_deny
  - utter_goodbye
  - action_restart

## interactive_story_110
* restaurant_search{"location": "agra", "cuisine": "italian"} 
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}
  - action_location_valid
  - slot{"location_validity" : "invalid"}
  - utter_location_invalid
  - utter_ask_location_retry
* restaurant_search{"location": "agra"}
  - action_location_valid
  - slot{"location_validity" : "valid"}
  - utter_ask_price
* inform_price{"price": "med"}
  - slot{"price": "med"}
  - action_search_restaurants
  - slot{"search_validity" : "valid", "email_response": ""}  
  - utter_email_prompt
* deny
  - utter_did_that_help
* deny
  - utter_deny
  - utter_goodbye
  - action_restart

## interactive_story_111
* greet
  - utter_greet
* restaurant_search{"location": "agra", "cuisine": "italian"}
  - action_location_valid
  - slot{"location_validity" : "valid"}  
  - action_cuisine_valid
  - slot{"cuisine_validity" : "invalid"}
  - utter_cuisine_invalid
  - utter_ask_cuisine_retry
* restaurant_search{"cuisine": "Chinese"}
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}
  - utter_ask_price
* inform_price{"price": "med"}
  - slot{"price": "med"}
  - action_search_restaurants
  - slot{"search_validity" : "valid", "email_response": ""}  
  - utter_email_prompt
* affirm
  - utter_ask_email
* inform_email{"email": "abc@abc.com"}
  - action_send_mail
  - utter_confirm_email
  - utter_goodbye
  - action_restart

## interactive_story_112
* restaurant_search{"location": "agra", "cuisine": "italian"}
  - action_location_valid
  - slot{"location_validity" : "valid"}  
  - action_cuisine_valid
  - slot{"cuisine_validity" : "invalid"}
  - utter_cuisine_invalid
  - utter_ask_cuisine_retry
* restaurant_search{"cuisine": "Chinese"}
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}
  - utter_ask_price
* inform_price{"price": "med"}
  - slot{"price": "med"}
  - action_search_restaurants
  - slot{"search_validity" : "valid", "email_response": ""}  
  - utter_email_prompt
* affirm
  - utter_ask_email
* inform_email{"email": "abc@abc.com"}
  - action_send_mail
  - utter_confirm_email
  - utter_goodbye
  - action_restart

## interactive_story_113
* greet
  - utter_greet
* restaurant_search{"location": "agra", "cuisine": "italian"} 
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}
  - action_location_valid
  - slot{"location_validity" : "invalid"}
  - utter_location_invalid
  - utter_ask_location_retry
* restaurant_search{"location": "agra"}
  - action_location_valid
  - slot{"location_validity" : "valid"}
  - utter_ask_price
* inform_price{"price": "med"}
  - slot{"price": "med"}
  - action_search_restaurants
  - slot{"search_validity" : "valid", "email_response": ""}  
  - utter_email_prompt
* affirm
  - utter_ask_email
* inform_email{"email": "abc@abc.com"}
  - action_send_mail
  - utter_confirm_email
  - utter_goodbye
  - action_restart

## interactive_story_114
* restaurant_search{"location": "agra", "cuisine": "italian"} 
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}
  - action_location_valid
  - slot{"location_validity" : "invalid"}
  - utter_location_invalid
  - utter_ask_location_retry
* restaurant_search{"location": "agra"}
  - action_location_valid
  - slot{"location_validity" : "valid"}
  - utter_ask_price
* inform_price{"price": "med"}
  - slot{"price": "med"}
  - action_search_restaurants
  - slot{"search_validity" : "valid", "email_response": ""}  
  - utter_email_prompt
* affirm
  - utter_ask_email
* inform_email{"email": "abc@abc.com"}
  - action_send_mail
  - utter_confirm_email
  - utter_goodbye
  - action_restart

## interactive_story_115

* greet
    - utter_greet
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location":"Delhi NCR"}
    - slot{"location":"Delhi NCR"}
    - action_location_valid
    - slot{"location_validity":"valid"}
    - utter_ask_cuisine
    - slot{"location":"Delhi NCR"}
    - slot{"cuisine":"italian"}
    - slot{"price":"high"}
* deny
    - utter_did_that_help
* affirm
    - utter_happy
    - utter_goodbye
    - action_restart

## interactive_story_116

* restaurant_search{"location":"Delhi NCR"}
    - slot{"location":"Delhi NCR"}
    - action_location_valid
    - slot{"location_validity":"valid"}
    - utter_ask_cuisine
    - slot{"location":"Delhi NCR"}
    - slot{"location":"Delhi NCR"}
    - slot{"cuisine":"chinese"}
    - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}
  - utter_ask_price
* inform_price{"price": "med"}
  - slot{"price": "med"}
  - action_search_restaurants
  - slot{"search_validity" : "valid", "email_response": ""}  
  - utter_email_prompt
* affirm
  - utter_ask_email
* inform_email{"email": "abc@abc.com"}
  - action_send_mail
  - utter_confirm_email
  - utter_goodbye
  - action_restart

## interactive_story_117

* greet
    - utter_greet
* restaurant_search{"location":"Delhi NCR","cuisine":"chinese"}
    - slot{"cuisine":"chinese"}
    - slot{"location":"Delhi NCR"}
    - action_location_valid
    - slot{"location_validity":"valid"}
    - action_cuisine_valid
    - slot{"cuisine_validity":"valid"}
    - utter_ask_price
    - slot{"cuisine":"chinese"}
    - slot{"location":"Delhi NCR"}
    - slot{"price":"high"}
    - slot{"email":"blah@blah.in"}
    - slot{"cuisine":"chinese"}
    - slot{"location":"Delhi NCR"}
    - slot{"price":"high"}
    - slot{"email":"blah@blah.in"}
    - utter_confirm_email
* affirm
    - utter_happy
    - utter_goodbye
    - action_restart
