
import cohere
from cohere.responses.classify import Example

class CohereClassifier:
    def __init__(self, api_key):
        self.co = cohere.Client(api_key)

    def cohere_classifications(self, text):
        response = self.co.classify(
            model="embed-english-v3.0",  # Replace with the chosen classification model
            inputs=[text],  # User input to be classified
            examples = [
                        Example("Set up a timer for 10 minutes.", "set_timer"),
                        Example("Can you please start a timer for 15 minutes?", "set_timer"),
                        Example("I need to set a timer for 20 minutes.", "set_timer"),
                        Example("Please set a timer for 5 minutes.", "set_timer"),
                        Example("Could you set up a timer for 30 minutes?", "set_timer"),
                        Example("Start a timer for 25 minutes, please.", "set_timer"),
                        Example("I want to set a timer for 12 minutes.", "set_timer"),
                        Example("Let's set a timer for 8 minutes.", "set_timer"),
                        Example("Can you please start a timer for 3 minutes?", "set_timer"),
                        Example("I need to set a timer for 7 minutes.", "set_timer"),
                        Example("Could you set up a timer for 18 minutes?", "set_timer"),
                        Example("Start a timer for 22 minutes, please.", "set_timer"),
                        Example("I want to set a timer for 13 minutes.", "set_timer"),
                        Example("Let's set a timer for 9 minutes.", "set_timer"),
                        Example("Please set a timer for 4 minutes.", "set_timer"),
                        Example("Can you please start a timer for 11 minutes?", "set_timer"),
                        Example("I need to set a timer for 16 minutes.", "set_timer"),
                        Example("Could you set up a timer for 28 minutes?", "set_timer"),
                        Example("Start a timer for 14 minutes, please.", "set_timer"),
                        Example("I want to set a timer for 6 minutes.", "set_timer"),
                        Example("Let's set a timer for 19 minutes.", "set_timer"),
                        Example("Please set a timer for 2 minutes.", "set_timer"),
                        Example("Can you please start a timer for 21 minutes?", "set_timer"),
                        Example("I need to set a timer for 17 minutes.", "set_timer"),
                        Example("Could you set up a timer for 27 minutes?", "set_timer"),
                        Example("Start a timer for 23 minutes, please.", "set_timer"),
                        Example("I want to set a timer for 29 minutes.", "set_timer"),
                        Example("Let's set a timer for 26 minutes.", "set_timer"),
                        Example("Please set a timer for 24 minutes.", "set_timer"),
                        Example("Can you please start a timer for 31 minutes?", "set_timer"),
                        Example("I need to set a timer for 34 minutes.", "set_timer"),
                        Example("Could you set up a timer for 37 minutes?", "set_timer"),
                        Example("Start a timer for 33 minutes, please.", "set_timer"),
                        Example("I want to set a timer for 35 minutes.", "set_timer"),
                        Example("Let's set a timer for 32 minutes.", "set_timer"),
                        Example("Please set a timer for 36 minutes.", "set_timer"),
                        Example("Can you please start a timer for 40 minutes?", "set_timer"),
                        Example("I need to set a timer for 39 minutes.", "set_timer"),
                        Example("Could you set up a timer for 42 minutes?", "set_timer"),
                        Example("Start a timer for 38 minutes, please.", "set_timer"),
                        Example("I want to set a timer for 41 minutes.", "set_timer"),
                        Example("Let's set a timer for 43 minutes.", "set_timer"),
                        Example("Please set a timer for 45 minutes.", "set_timer"),
                        Example("Can you please start a timer for 44 minutes?", "set_timer"),
                        Example("I need to set a timer for 46 minutes.", "set_timer"),
                        Example("Could you set up a timer for 49 minutes?", "set_timer"),
                        Example("Start a timer for 47 minutes, please.", "set_timer"),
                        Example("I want to set a timer for 48 minutes.", "set_timer"),
                        Example("Let's set a timer for 50 minutes.", "set_timer"),
                        Example("Remind me to buy groceries.", "not_timer"),
                        Example("Play my favorite song, please.", "not_timer"),
                        Example("Find the nearest coffee shop.", "not_timer"),
                        Example("Turn off the lights in the living room.", "not_timer"),
                        Example("Set an alarm for 7 AM tomorrow.", "not_timer"),
                        Example("Send a text message to John.", "not_timer"),
                        Example("Add eggs and milk to my shopping list.", "not_timer"),
                        Example("Call Mom.", "not_timer"),
                        Example("Schedule a meeting for 2 PM next Tuesday.", "not_timer"),
                        Example("Open the weather forecast for today.", "not_timer"),
                        Example("Start a workout timer for 30 minutes.", "not_timer"),
                        Example("Translate 'hello' to French.", "not_timer"),
                        Example("Order a pizza for delivery.", "not_timer"),
                        Example("Read me the latest news headlines.", "not_timer"),
                        Example("Book a table for two at 7 PM tonight.", "not_timer"),
                        Example("Search for a recipe for lasagna.", "not_timer"),
                        Example("Calculate the square root of 144.", "not_timer"),
                        Example("Set the thermostat to 72°F.", "not_timer"),
                        Example("Find a tutorial on how to knit a scarf.", "not_timer"),
                        Example("Show me pictures of puppies.", "not_timer"),
                        Example("Create a new playlist named 'Chill Vibes'.", "not_timer"),
                        Example("Play a random episode of 'Friends'.", "not_timer"),
                        Example("Find a good book to read.", "not_timer"),
                        Example("Write an email to Sarah about the project.", "not_timer"),
                        Example("Set up a budget tracker for this month.", "not_timer"),
                        Example("Scan this document and save it as a PDF.", "not_timer"),
                        Example("Check my flight status for tomorrow.", "not_timer"),
                        Example("Teach me a new language phrase.", "not_timer"),
                        Example("Set up a study schedule for finals week.", "not_timer"),
                        Example("Find a yoga class near me.", "not_timer"),
                        Example("Calculate the tip for a $50 bill.", "not_timer"),
                        Example("Order a birthday cake for Sarah's party.", "not_timer"),
                        Example("Plan a weekend getaway trip.", "not_timer"),
                        Example("Review my recent expenses.", "not_timer"),
                        Example("Call a taxi to take me to the airport.", "not_timer"),
                        Example("Research the best smartphone deals.", "not_timer"),
                        Example("Set my phone to 'Do Not Disturb' mode.", "not_timer"),
                        Example("Remind me to water the plants at 6 PM.", "not_timer"),
                        Example("Find a plumber to fix the leaky faucet.", "not_timer"),
                        Example("Calculate my daily calorie intake.", "not_timer"),
                        Example("Schedule a dentist appointment.", "not_timer"),
                        Example("Order flowers for Mom's birthday.", "not_timer"),
                        Example("Learn how to juggle three balls.", "not_timer"),
                        Example("Check if the store is open on Sundays.", "not_timer"),
                        Example("Write a poem about nature.", "not_timer"),
                        Example("Search for hiking trails in the nearby area.", "not_timer"),
                        Example("Check the balance of my bank account.", "not_timer"),
                        Example("Book tickets for the concert next month.", "not_timer")
                    ]
        )
        return response.classifications