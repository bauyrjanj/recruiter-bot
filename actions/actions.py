from rasa_sdk import Action
from rasa_sdk.events import SlotSet
import random


class ActionCheckStatus(Action):

    def name(self):
        return "action_check_status"

    def run(self, dispatcher, tracker, domain):
        # return a random status, just a mockup
        statuses = ["received", "rejected", "interview", "unknown"]
        status = random.choice(statuses)

        # get the name of the user from the slot
        name = tracker.get_slot("name")
        if not name:
            status = "noname"
        return [SlotSet("status", status)]

class ActionCheckPositions(Action):

    def name(self):
        return "action_check_positions"

    def run(self, dispatcher, tracker, domain):
        # return hard-coded open positions, this would normally come from an API
        positions = {
            "technical": [
                "Machine learning engineer",
                "ML product success engineer"
            ],
            "business": []
        }
        position_type = tracker.get_slot("role_type")
        technical_roles = ["tech", "technical", "backend", "engineering"]
        any_roles = ["any", "anything"]

        # Handle the synonymous slot values for position_type
        if position_type in any_roles:
            position_type = "any"
            relevant_positions = positions["technical"] + positions["business"]
        elif position_type in technical_roles:
            position_type = "technical"
            relevant_positions = positions.get(position_type, [])
        else:
            position_type = "business"
            relevant_positions = positions.get(position_type, [])

        # Handle the appropriate listing of the jobs in the response
        if len(relevant_positions)<2:
            relevant_positions = ''.join(relevant_positions)
        elif len(relevant_positions) == 2:
            relevant_positions = ' and '.join(relevant_positions)
        else:
            relevant_positions = ', '.join(relevant_positions[:-1]) + " and " + relevant_positions[-1]
        return [SlotSet("positions", relevant_positions), SlotSet("role_types", position_type)]

