from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class getProperties(Action):

    def name(self) -> Text:
        return "action_show_properties"

    # Figure out how to extract the property wanted by user
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker):
        # Import data, filter on property type, return X properties then ask
        # user for more info/details/confirmation to narrow down search in next
        # action
        pass

class getPrice(Action):

    def name(self) -> Text:
        return "action_provide_price_info"
    
    # Figure out how to extract the property details
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker):
        # Import data, filter or details given, return price info on available
        # properties then ask user for more info/details/confirmation
        pass

class getLocation(Action):

    def name(self) -> Text:
        return "action_provide_location_info"
    
    # Figure out how to extract detials from user input
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker):
        # Import data, filter or details given, return location info on available
        # properties and ask for confirmation
        # In the story it calls provide_more_details so execute that next
        pass

class getPropertyDetails(Action):

    def name(self) -> Text:
        return "action_provide_property_details"
    
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker):
        pass

class getLocationDetails(Action):

    def name(self) -> Text:
        return "action_provide_more_details"
    
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker):
        pass