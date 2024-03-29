# Description: This file contains the code for the NLP tagging of the text input.
'''
The extract_duration function is designed to extract the duration in hours and minutes from a given text. 
This function is particularly useful in natural language processing tasks where you need to extract specific information from a user's input.

The function starts by defining a regular expression pattern to match durations in the text. 
The pattern is designed to match both hours and minutes, and it uses named groups (hours and minutes) to make it easier to extract these values later. 
After defining the pattern, the function uses the search method to search the text for a match to the pattern. 
If a match is found, the function extracts the hours and minutes from the match object using the group method and the names of the groups. 
If the group method returns None (which means the group wasn't found in the match), the function uses a default value of 0.

Finally, the function calculates the total duration in minutes by converting the hours to minutes and adding the minutes. 
If no match is found, the function returns None.

'''
from numpy import extract
import speech_recognition as sr
import nltk
import speakEngine
import re
import nltk
import re
speakEngine = speakEngine.SpeakEngine()

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

def extract_duration(text):
    duration_regex = re.compile(r"""
    (?:(?P<hours>\d+)\s?(?:hours|hour|h))?  # Match optional hours 
    \s+                                     # Require whitespace between hours and minute sections
    ((?P<minutes>\d+)\s?(?:minutes|min|m)) # Match minutes 
""", re.IGNORECASE | re.VERBOSE) 


    match = duration_regex.search(text)

    if match:
        hours = int(match.group('hours')) if match.group('hours') else 0
        minutes = int(match.group('minutes')) if match.group('minutes') else 0
        total_minutes = (hours * 60) + minutes
        return total_minutes
    else:
        return None



def set_timer(text):
    text = text.lower()
    tokens = nltk.word_tokenize(text)
    tagged = nltk.pos_tag(tokens)
    
    if "set" in tokens and "timer" in tokens:
        duration = extract_duration(text)
        speakEngine.speak("Timer set for " + str(duration) + " minutes")
        print("Timer set for " + str(duration) + " minutes")
    else:
        speakEngine.speak("I'm sorry, I didn't understand that")
        print("I'm sorry, I didn't understand that")

# The output of this code is:
# Timer set for 10 minutes
