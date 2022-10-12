# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionAccount(Action):

    def name(self) -> Text:
        return "action_account"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        for blob in tracker.latest_message['entities']:
            if blob['entity'] == 'cuenta':
                cuenta = blob['value'].lower()
                if cuenta == 'credito':
                    dispatcher.utter_message(response="utter_ask_monto")
                else:
                    dispatcher.utter_message(response="utter_debito")
        return []

class ActionMonto(Action):

    def name(self) -> Text:
        return "action_monto"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        for blob in tracker.latest_message['entities']:
            if blob['entity'] == 'monto':
                monto = int(blob['value'])
                if monto>=1000:
                    dispatcher.utter_message(response="utter_ask_sucursal")
                else:
                    dispatcher.utter_message(response="utter_confirmation", monto=f"{monto}")

        return []

class ActionSucursal(Action):

    def name(self) -> Text:
        return "action_sucursal"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        for blob in tracker.latest_message['entities']:
            if blob['entity'] == 'sucursal':
                sucursal = blob['value'].lower()
                if sucursal=="principal":
                    dispatcher.utter_message(text="Calle A 316 Surco. Atención de 9am a 5pm")
                else:
                    dispatcher.utter_message(text="Calle B 315 La Molina. Atención de 9am a 5pm")

        return []
