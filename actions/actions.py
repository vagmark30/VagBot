from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet

class ResolveIssue(Action):
    def name(self) -> Text:
        return "action_resolve_issue"

    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        contact_type = next(tracker.get_latest_entity_values('yphresia'), None)


        if str(contact_type) == 'apps':
            strg = 'Για προβλήματα σχετικά με το Apps επικοινωνήστε με το noc@it.teithe.gr'
        elif str(contact_type) == 'webmail':
            strg = 'Για προβλήματα σχετικά με το Webmail επικοινωνήστε με το noc@it.teithe.gr ή στο https://helpdesk.the.ihu.gr'
        elif str(contact_type) == 'thesis':
            strg = 'Για προβλήματα σχετικά με το Thesis επικοινωνήστε με τον Κυριάκο Τσιακμάκη στο ktsiak@physics.auth.gr'
        else:
            strg = 'Συγγνώμη δεν κατάλαβα το πρόβλημα. Επικοινωνήστε με την γραμματεία'
        dispatcher.utter_message(strg)     
        return []