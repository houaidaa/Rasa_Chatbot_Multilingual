# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List, Union

from rasa.model import get_latest_model
from rasa.shared.constants import DEFAULT_MODELS_PATH
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

from langdetect import detect

import yaml
from yaml.loader import SafeLoader



class ChoisirLaLangue(Action):

    def name(self) -> Text:
        return "action_choix_de_langue"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        #intentions = tracker.get_intent_of_latest_message()
        msg = tracker.latest_message['text']
        print(msg)
        lang = detect(msg)
        print("langue=", lang)

        if lang == "fr":
            with open('config_fr.yml', 'r') as f:
                data_fr = yaml.load(f, Loader=SafeLoader)
                dispatcher.utter_message(response="utter_greet_bot")
                print(data_fr)
        elif lang == "en":
            with open('config_en.yml', 'r') as f:
                data_ang = yaml.load(f, Loader=SafeLoader)
                model_path = "C:/Users/Karoui Houaida/Desktop/stage/chatbot_telco_fr/models"
                model = get_latest_model(model_path)
                dispatcher.utter_message(response="utter_greet_bot_en")
                print(data_ang)
        return []

class ActionStartConversation(Action):

    def name(self) -> Text:
        return "action_hello_world"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("Bonjour, je suis votre assistant virtuel ! Dit bonjour pour lancer la conversation.Hello, I’m your virtual assistant! says hello to start the conversation.")

        return []


class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_Box_Org"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        return ["OffreBoxOrg"]

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:


        print("slot value :", tracker.get_slot('OffreBoxOrg'))
        if tracker.slots.get("OffreBoxOrg", None) == "Darbox":
            dispatcher.utter_message(response="utter_question_offre_darbox_org")
        elif tracker.slots.get("OffreBoxOrg", None) == "None":
            dispatcher.utter_message(response="utter_orange")

        return []

       # elif tracker.slots.get("testtt", None) == "Flybox postpaye":
           # dispatcher.utter_message(
               #     response="utter_Flybox_info"
              #  )
        #else:
            #dispatcher.utter_message(
            #    response="utter_question_offres_options"
            #)
        #return []
        #print("entité :", tracker.get_slot('OffreBoxOrg'))
        #slot_value = tracker.get_slot('OffreBoxOrg')
        #text_store = tracker.latest_message['text']
        #print(text_store)
        #print(tracker.get_latest_entity_values("OffreBoxOrg"))
        #if text_store == "Darbox":
            #dispatcher.utter_template("utter_Darbox_info", tracker)
        #if text_store == "Flybox postpaye":
        #dispatcher.utter_template("utter_Darbox_info", tracker, link=slot_value)
        #return ["",text_store]
