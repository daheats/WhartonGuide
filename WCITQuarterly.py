from __future__ import print_function
import requests
import random 

names = [

    "Dan Alig",
    "Geoffrey Garret",
    "Peggy Bishop Lane",
    "Americus Reed"

    ]

location_names = [
    
    "The Wharton Store",
    "Wharton Operations",
    "Student Support",
    "Wharton Human Resources"
    "McNulty Leadership Program"

    ]

locations = [

    "Suite 400...Steinberg-Dietrich Hall...by Joe's Cafe`",
    "F30...Jon M. Huntsman Hall...F30",
    "114 Steinberg-Deitrich Hall",
    "450 Steinberg-Deitrich Hall",
    "G47...Jon M. Huntsman Hall",
    ]

biographies = [     

    "Dan Alig, Chief Information Officer at The Wharton School, leads Wharton\
    Computing in delivering IT resources to faculty,students, staff and alumni and\
    developing strategies to enhance the School’s mission with technology.",

    "Geoffrey Garrett is Dean, Reliance Professor of Management and Private Enterprise, and Professor of Management at the Wharton School\
    of the University of Pennsylvania. He became Dean of the Wharton School in 2014, having been a member of the Wharton faculty in the\
    Management Department from 1995 to 1997. Prior to his return to Penn, he was dean of the business schools at both the University of Sydney and UNSW in his native Australia.",

    "Peggy Bishop Lane is Vice Dean of the Wharton MBA Program for Executives and Adjunct Professor of Accounting. Based in Philadelphia, Professor Lane oversees both the Philadelphia\
    and San Francisco programs. Before joining the MBA Program for Executives, she directed the academic experience for the full-time MBA Program as Deputy Vice Dean of Academic Affairs\
    for 11 years",

    "Professor Americus Reed is the Marketing Department's only "identity theorist" focusing his research on the role consumers' self concepts play in guiding buying decisions.\
    He examines how social identity, social influence, values, attitudes and judgments interact in shaping purchase decisions and consumer behavior,\
    but from a social psychology point of view.",

    ]

def lambda_handler(event, context):
    print("event.session.application.applicationId=" +
          event['session']['application']['applicationId'])

    if event['session']['new']:
        on_session_started({'requestId': event['request']['requestId']},
                           event['session'])

    if event['request']['type'] == "LaunchRequest":
        return on_launch(event['request'], event['session'])
    elif event['request']['type'] == "IntentRequest":
        return on_intent(event['request'], event['session'])
    elif event['request']['type'] == "SessionEndedRequest":
        return on_session_ended(event['request'], event['session'])

def on_session_started(session_started_request, session):
    print("on_session_started requestId=" +
          session_started_request['requestId'] + ", sessionId=" +
          session['sessionId'])

def on_launch(launch_request, session):
    print("on_launch requestId=" + launch_request['requestId'] +
          ", sessionId=" + session['sessionId'])
    return get_welcome_response()

def on_intent(intent_request, session):
    print("on_intent requestId=" + intent_request['requestId'] +
          ", sessionId=" + session['sessionId'])

    intent = intent_request['intent']
    intent_name = intent_request['intent']['name']
    if intent_name == "WhartonGuideIntent":
        return get_welcome_response()
    elif intent_name == "AMAZON.NoIntent":
        return handle_finish_session_request(intent, session)
    elif intent_name == "AMAZON.YesIntent":
        return handle_anotherq_request(intent, session)
    elif intent_name == "AMAZON.HelpIntent":
        return handle_help_request(intent, session)
    elif intent_name == "AdditionalGuidanceIntent":
        return handle_anotherq_request(intent, session)
    elif intent_name == "AMAZON.CancelIntent":
        return handle_finish_session_request(intent, session)
    elif intent_name == "AMAZON.StopIntent":
        return handle_finish_session_request(intent, session)
    else:
        return handle_finish_session_request(intent, session)
        
def get_welcome_response():
    session_attributes = {}
    speech_output = "Welcome to the Wharton Guide!"
    reprompt_text = "If you'd like to hear about staff and faculty you can say biographies...if you'd like\
    to hear about places on campus you can say places...you can also ask me about Wharton's or Penn's mission statement\
    by saying Penn's Mission or Wharton's mission"
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response_without_card(speech_output, reprompt_text, should_end_session))

def dan_alig_response():
    session_attributes = {}
    speech output = "names[0], biographies[0]"
    reprompt_text = "Is there anything else I can help you with?"
    should should_end_session = False
    return build_response(attributes, build_speechlet_response_without_card(speech_output, reprompt_text, should_end_session))

def geoff_garrett_response():
    session_attributes  = {}
    speech_output = "names[1], biographies[1]"
    reprompt_text = "Is there anything else I can help you with?"
    should_end_session = False
    return build_response(attributes, build_speechlet_response_without_card(speech_output, reprompt_text, should_end_session))

def peggy_bishop_lane_response():
    session_attributes = {}
    speech_output = "names[2], biographies[2]"
    reprompt_text = "Is there anything else I can help you with?"
    should_end_session = False
    return build_response(attributes, build_speechlet_response_without_card(speech_output, reprompt_text, should_end_session))

def amercius_reed_response():
    session_attributes = {}
    speech_output = "names[3], biographies[3]"
    reprompt_text = "Is there anything else I can help you with?"
    should_end_session = False
    return build_response (attributes, build_speechlet_response_without_card(speech_output, reprompt_text, should_end_session))

def wharton_store_response():
    session_attributes = {}
    speech_output = "location_names[0], locations[0]"
    reprompt_text = "Is there anything else I can help you with?"
    should_end_session = False
    return build_response (attributes, build_speechlet_response_without_card(speech_output, reprompt_text, should_end_session))

def mcnulty_leadership_response():
    session_attributes = {}
    speech_output = "location_names[1], locations[1]"
    reprompt_text = "Is there anything else I can help you with?"
    should_end_session = False
    return build_response (attributes, build_speechlet_response_without_card(speech_output, reprompt_text, should_end_session))

def wharton_operations_response():
    session_attributes = {}
    speech_output = "location_names[2], locations[2]"
    reprompt_text = "Is there anything else I can help you with?"
    should_end_session = False
    return build_response (attributes, build_speechlet_response_without_card(speech_output, reprompt_text, should_end_session))

def human_resources_response
    session_attributes = {}
    speech_output = "location_names[3], locations[3]"
    reprompt_text = "Is there anything else I can help you with?"
    should_end_session = False
    return build_response (attributes, build_speechlet_response_without_card(speech_output, reprompt_text, should_end_session))

def student_support_response
    session_attributes = {}
    speech_output = "location_names[4], locations[4]"
    reprompt_text = "Is there anything else I can help you with?"
    should_end_session = False
    return build_response (attributes, build_speechlet_response_without_card(speech_output, reprompt_text, should_end_session))

def penn_mission_statement
    session_attributes = {}
    speech_output = ""
    reprompt_text = ""
    should_end_session = False
    return build_response (attributes, build_speechlet_response_without_card(speech_output, reprompt_text, should_end_session))

def wharton_mission_statement
    session_attributes = {}
    speech_output = ""
    reprompt_text = ""
    should_end_session = False
    return build_response (attributes, build_speechlet_response_without_card(speech_output, reprompt_text, should_end_session))


def on_session_ended(session_ended_request, session):
    print("on_session_ended requestId=" + session_ended_request['requestId'] +
          ", sessionId=" + session['sessionId'])


def AdditionalGuidanceIntent(intent, session):
    attributes = {}
    speech_output = "Here's another quote!" + quotes[random_number] + "... Would you like to hear another quote?"
    reprompt_text = "Would you like to hear another quote?"
    should_end_session = False
    return build_response(attributes, build_speechlet_response_without_card(speech_output, reprompt_text, should_end_session))

def handle_help_request(intent, session):
    attributes = {}
    speech_output = "You can ask me about staff and faculty members by saying biographies, to hear about places on campus say places, to hear\
    about Penn or Wharton's mission statement say Penn's Mission or Wharton's Mission."
    reprompt_text = "So, how can I help you?"
    should_end_session = False
    return build_response(attributes, build_speechlet_response_without_card(speech_output, reprompt_text, should_end_session))

def handle_finish_session_request(intent, session):
    attributes = {}
    reprompt_text = None
    speech_output = "Thank you for using the Wharton Guide!"
    should_end_session = True
    return build_response(attributes, build_speechlet_response_without_card(speech_output, reprompt_text, should_end_session))


def build_speechlet_response(title, output, reprompt_text, should_end_session):
    return {
        'outputSpeech': {
            'type': 'PlainText',
            'text': output
        },
        'card': {
            'type': 'Simple',
            'title': title,
            'content': output
        },
        'reprompt': {
            'outputSpeech': {
                'type': 'PlainText',
                'text': reprompt_text
            }
        },
        'shouldEndSession': should_end_session
    }


def build_speechlet_response_without_card(output, reprompt_text, should_end_session):
    return {
        'outputSpeech': {
            'type': 'PlainText',
            'text': output
        },
        'reprompt': {
            'outputSpeech': {
                'type': 'PlainText',
                'text': reprompt_text
            }
        },
        'shouldEndSession': should_end_session
    }


def build_response(attributes, speechlet_response):
    return {
        'version': '1.0',
        'sessionAttributes': attributes,
        'response': speechlet_response
    }