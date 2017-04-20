# coding: utf-8
from __future__ import print_function
import random



names = [

    "Dan Aylig",
    "Peggy Bishop Lane",
    "Docotor Americus Reed",
    "Geoffrey Garrett."

]



biographies = [
    
    "Dan Aylig...Chief Information Officer at The Wharton School...leads\
    Wharton Computing in delivering IT resources to faculty...students...\
    staff and alumni...and developing strategies to enhance the School's\
    mission with technology.",

    "Peggy Bishop Lane is Vice Dean of the Wharton MBA Program for Executives\
    and Adjunct Professor of Accounting. Based in Philadelphia, Professor Lane\
    oversees both the Philadelphia and San Francisco programs. Before joining\
    the MBA Program for Executives, she directed the academic experience for\
    the full-time MBA Program as Deputy Vice Dean of Academic Affairs for\
    eleven years. Professor Lane teaches Financial Accounting to first year\
    MBA and Executive MBA students.",

    "Doctor Americus Reed is the Marketing Department's only identity\
    theorist, focusing his research on the role consumers' self concepts play\
    in guiding buying decisions. He examines how social identity,\
    social influence, values, attitudes and judgments interact in\
    shaping purchasing decisions and consumer behavior, but, from a social\
    psychology point of view.",


    "Geoffrey Garrett is the Dean, he is the Reliance Professor of Management\
    and Private Enterprise and a Professor of Management at the Wharton School,\
    also a Professor of Political Science at the University of Pennsylvania.\
    He became Dean of the Wharton School in 2014, having been a member of\
    the Wharton faculty in the Management Department from 1995 to 1997."
    
    ]


locations = [

    "Suite 450 in Steinberg Dietrich Hall, by Joe's cafe",
    "Suite 400 in Steinberg Dietrich Hall, by Joe's cafe",
    "G47 in Jon M. Huntsman Hall",
    "Suite 114 in Steinberg Dietrich Hall",
    "36 0 1 Walnut Street, a few strides away from the Inn at Penn"

]

facts = [

    "1881, Wharton is the first business school at a University.",
    "From 1881 to 1901, the school's name is the Wharton School of Finance\
    and Economy.",
    "From 1902 to 1971, the school's name is the Wharton School of Finance\
    and Commerce.",
    "From 1881 to 1910, Wharton creates the first business textbooks.",
    "1921, the Industrial Research Unit, is the first research center\
    at a business school.",
    "1953 to now, Securities Industries Institute, is the first and\
    longest running custom executive education program.",
    "1970, Wharton has the first M.B.A program in healthcare management.",
    "From 1972 to now, the school's name is the Wharton School.",
    "1973, Wharton has the first center for entrepreneurship.",
    "1978, Wharton has the first joint-degree program in management\
    and technology.",
    "1983, Wharton has the first joint-degree MBA MA program in\
    international management, Joseph H. Lauder institute.",
    "1994, Wharton has the first joint-degree undergraduate program in\
    international studies at a business school, Huntsman Program in\
    International Studies.",
    "From 1988 to 1994, Wharton has the first executive advisory boards\
    in Europe, Asia, and Latin America.",
    "1999, Knowledge at Wharton, the School's bi-weekly online business journal\
    is launched.",
    "2001, Wharton establishes the West Coast MBA program for executives,\
    Wharton San Francisco.",
    "2001, Wharton establishes an alliance with INSEAD in the global\
    development and delivery of management education.",
    "2003, Wharton has the first doctoral program in ethics and legal studies.",
    "2005, Wharton created a new undergraduate joint-degree program, the Roy\
    and Diana Vagelos Program in Life Sciences and Management.",
    "2010, Wharton introduced Global Modular Courses, intensive for-credit\
    workshops delivered in 13 countries around the world.",
    "2011, Wharton launchds Wharton Digital Press, offering business\
    intelligence on digital publishing platforms.",
    "2012, Wharton rolled out MOOCs, with Wharton Online becoming the top\
    business school on Coursera with 2.7 million students in 18 courses.",
    "2013, Wharton opened Penn Wharton Public Policy Center in Philadelphia\
    and Washington, DC.",
    "2014, Wharton launched Business Radio Powered by the Wharton School, \
    presenting 40 hours of unique real-time programming on Sirius XM.",
    "2015, Wharton opened Penn Wharton China Center in Beijing, \
    the university’s only center outside the United States"

]

aboutwharton = [

    "The Wharton School of the University of Pennsylvania... (also known\
    as the Wharton School or simply Wharton)...is the business school of the\
    University of Pennsylvania, a private Ivy League university, located\
    in Philadelphia, Pennsylvania. Wharton was established in 1881 through\
    a donation from Joseph Wharton and is the world’s first collegiate school\
    of business. Wharton's MBA program is ranked number one in the world\
    according to Business Insider, and is tied with Harvard Business School\
    for the number one rank in the United States, according to\
    U.S. News & World Report."

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
    elif intent_name == "WhartonGenIntent":
        return generic_wharton_response(intent, session)
    elif intent_name == "WhartonFactIntent":
        return wharton_fact_response(intent, session)
    elif intent_name == "AnotherFactIntent":
        return wharton_fact_response(intent, session)
    elif intent_name == "DanAligIntent":
        return dan_alig_response(intent, session)
    elif intent_name == "DanAligEasterEggIntent":
        return dan_alig_egg_response(intent, session)
    elif intent_name == "DanNameIntent":
        return dan_name_response(intent, session)
    elif intent_name == "PBLIntent":
        return peggy_bishop_response(intent, session)
    elif intent_name == "PBLNameIntent":
        return peggy_name_response(intent, session)
    elif intent_name == "GGIntent":
        return gg_response(intent, session)
    elif intent_name == "GGNameIntent":
        return gg_name_repsonse(intent, session)
    elif intent_name == "AmericusIntent":
        return americus_response(intent, session)
    elif intent_name == "AmericusNameIntent":
        return americus_name_response(intent, session)
    elif intent_name == "BioIntent":
        return wharton_bio_response(intent, session)
    elif intent_name == "PlacesIntent":
        return wharton_places_response(intent, session)
    elif intent_name == "WhartonHRIntent":
        return wharton_hrlocation_response(intent, session)
    elif intent_name == "StudentSupportIntent":
        return student_support_response(intent, session)
    elif intent_name == "WhartonComputingIntent":
        return wharton_computing_response(intent, session)
    elif intent_name == "WhartonComputingSupportIntent":
        return wharton_computingsupport_response(intenet, session)
    elif intent_name == "WCFacultySupportIntent":
        return wharton_computingfacsupport_response(intent, session)
    elif intent_name == "WCStaffSupportIntent":
        return wharton_computingstaffsupport_response(intent, session)
    elif intent_name == "StudentHelpIntent":
        return wharton_computingstudent_response(intent, session)
    elif intent_name == "StaffFacHelpIntent":
        return wharton_computingstafffac_response(intent,session)
    elif intent_name == "WhartonStoreIntent":
        return wharton_store_response(intent, session)
    elif intent_name == "CoffeeIntent":
        return yum_coffee_response(intent, session)
    elif intent_name == "WhartonStoreIntent":
        return wharton_store_response(intent, session)
    elif intent_name == "PennBookStoreIntent":
        return penn_bookstore_response(intent, session)
    elif intent_name == "PennBookStoreAddlIntent":
        return penn_bookstoreaddl_response(intent, session)
    elif intent_name == "ComputerConnIntent":
        return computer_conn_response(intent, session)
    elif intent_name == "PennCardIntent":
        return penn_card_response(intent, session)
    elif intent_name == "AMAZON.NoIntent":
        return handle_finish_session_request(intent, session)
    elif intent_name == "AMAZON.YesIntent":
        return handle_anotherq_request(intent, session)
    elif intent_name == "AMAZON.HelpIntent":
        return handle_help_request(intent, session)
    elif intent_name == "AnotherQuoteIntent":
        return handle_anotherq_request(intent, session)
    elif intent_name == "AMAZON.CancelIntent":
        return handle_finish_session_request(intent, session)
    elif intent_name == "AMAZON.StopIntent":
        return (intent, session)
    else:
        return handle_finish_session_request(intent, session)
        
def get_welcome_response():
    session_attributes = {}
    speech_output = "Welcome to the Wharton Guide! To hear biographies on staff and faculty say biographies, to hear about places on campus say places, for technology related issues say Wharton Computing, to hear Wharton facts say facts, to hear about Wharton simply say Wharton!"
    reprompt_text = "Is there anything I can help you with?"
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response_without_card(speech_output, reprompt_text, should_end_session))

def generic_wharton_response(intent, session):
    session_attributes = {}
    speech_output = aboutwharton[0]
    reprompt_text = ""
    should_end_session = True
    return build_response(session_attributes, build_speechlet_response_without_card(speech_output, reprompt_text, should_end_session))

def wharton_fact_response(intent, session):
    session_attributes = {}
    random_number = random.randint(0, len(facts))
    speech_output = "Here is your Wharton fact..." + facts[random_number] + "...If you would like to hear another fact simply say another fact!"
    reprompt_text = ""
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response_without_card(speech_output, reprompt_text, should_end_session))

def dan_alig_response(intent, session):
    session_attributes = {}
    speech_output = biographies[0]
    reprompt_text = "Did you want to hear about any other staff or faculty at the Wharton School?"
    should_end_session = False 
    return build_response(session_attributes, build_speechlet_response_without_card(speech_output, reprompt_text, should_end_session))

def dan_name_response(intent, session):
    session_attributes = {}
    speech_output = names[0]
    reprompt_text = ""
    should_end_session = True
    return build_response(session_attributes, build_speechlet_response_without_card(speech_output, reprompt_text, should_end_session))

def dan_alig_egg_response(intent, session):
    session_attributes = {}
    speech_output = "Wouldn't you like to know?... Too bad...Nope, Nope, I'm not saying a word!"
    should_end_session = False
    reprompt_text = "Do you have any other nosey questions you'd like to ask me?"
    return build_response(session_attributes, build_speechlet_response_without_card(speech_output, reprompt_text, should_end_session))

def peggy_bishop_response(intent, session):
    session_attributes = {}
    speech_output = biographies[1]
    reprompt_text = "Did you want to hear about any other staff or faculty at the Wharton School?"
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response_without_card(speech_output, reprompt_text, should_end_session))

def peggy_name_response(intent, session):
    session_attributes = {}
    speech_output = names[1]
    reprompt_text = ""
    should_end_session = True
    return build_response(session_attributes, build_speechlet_response_without_card(speech_output, reprompt_text, should_end_session))

def gg_response(intent, session):
    session_attributes = {}
    speech_output = biographies[3]
    reprompt_text = "Did you want to hear about any other staff or faculty at the Wharton School?"
    should_end_session = False 
    return build_response(session_attributes, build_speechlet_response_without_card(speech_output, reprompt_text, should_end_session))

def gg_name_repsonse(intent,session):
    session_attributes = {}
    speech_output = names[3]
    reprompt_text = ""
    should_end_session = True 
    return build_response(session_attributes, build_speechlet_response_without_card(speech_output, reprompt_text, should_end_session))

def americus_response(intent, session):
    session_attributes = {}
    speech_output = biographies[2]
    reprompt_text = "Did you want to hear about any other staff or faculty at the Wharton School?"
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response_without_card(speech_output, reprompt_text, should_end_session))

def americus_name_response(intent, session):
    session_attributes = {}
    speech_output = names[3]
    should_end_session = True 
    return build_response(session_attributes, build_speechlet_response_without_card(speech_output, reprompt_text, should_end_session))

def wharton_bio_response(intent, session):
    session_attributes = {}
    speech_output = "Name a staff or faculty member you'd like to hear more information about."
    reprompt_text = "Did you still need my guidance in regards to a biography?"
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response_without_card(speech_output, reprompt_text, should_end_session))

def wharton_places_response(intent, session):
    session_attributes = {}
    speech_output = "Ask me about a place on campus for it's location"
    reprompt_text = "Did you still need my guidance in being your tour guide?"
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response_without_card(speech_output, reprompt_text, should_end_session))

def wharton_hrlocation_response(intent, session):
    session_attributes = {}
    speech_output = "You can find Wharton HR at" + locations[0]
    reprompt_text = ""
    should_end_session = True
    return build_response(session_attributes, build_speechlet_response_without_card(speech_output, reprompt_text, should_end_session))

def wharton_store_response(intent, session):
    session_attributes = {}
    speech_output = "The Wharton Store, located at" + locations[1]
    reprompt_text = ""
    should_end_session = True 
    return build_response(session_attributes, build_speechlet_response_without_card(speech_output, reprompt_text, should_end_session))

def leadership_program_response(intent, session):
    session_attributes = {}
    speech_output = "You can find the McNulty Leadership Program at" + locations[2]
    should_end_session = True
    return build_response(session_attributes, build_speechlet_response_without_card(speech_output, should_end_session))

def student_support_response(intent, session):
    session_attributes = {}
    speech_output = "You can find Student Support at" + locations[3]
    reprompt_text = ""
    should_end_session = True 
    return build_response(session_attributes, build_speechlet_response_without_card(speech_output, reprompt_text, should_end_session))

def wharton_computing_response(intent, session):
    session_attributes = {}
    speech_output = "Sorry to hear you're having technology related issues... are you staff, faculty,  or are you a student?"
    reprompt_text = ""
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response_without_card(speech_output, reprompt_text, should_end_session))
    
def wharton_computingfacsupport_response(intent, session):
    session_attributes = {}
    speech_output = "To find out who your computing support is,  please visit inside, dot wharton, dot u penn, dot e.d.u, forward slash faculty, forward slash partners!"
    reprompt_text = ""
    should_end_session = True
    return build_response(session_attributes, build_speechlet_response_without_card(speech_output, reprompt_text, should_end_session))

def wharton_computingstaffsupport_response(intent, session):
    session_attributes = {}
    speech_output = "To find out who your computing support is, please visit inside, dot wharton, dot u penn, dot e.d.u, forward slash, staff!"
    reprompt_text = ""
    should_end_session = True
    return build_response(session_attributes, build_speechlet_response_without_card(speech_output, reprompt_text, should_end_session))
    
def wharton_computingstudent_response(intent, session):
    session_attributes = {}
    speech_output = "You can call Student Support at 215-898-8600, or you can submit a ticket online to support, at wharton, dot u penn, dot e.d.u, or you can \
    visit in person, by stopping by Steinberg Dietrich Hall, Suite 114."
    reprompt_text = ""
    should_end_session = True
    return build_response(session_attributes, build_speechlet_response_without_card(speech_output, reprompt_text, should_end_session))

def wharton_computingstafffac_response(intent, session):
    session_attributes = {}
    speech_output = "You should reach out to your L.S.P or the group that handles I.T. for your department. If you would like information on your support representatives, please say staff support, or say faculty support"
    reprompt_text = ""
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response_without_card(speech_output, reprompt_text, should_end_session))

def yum_coffee_response(intent, session):
    session_attributes = {}
    speech_output = "You can find THE best cup of coffee at HubBubb, located next to the Wa Wa at the corner of 38th\
    and Spruce...I hear the hazelnut mocha is delicious!!!"
    reprompt_text = ""
    should_end_session = True
    return build_response(session_attributes, build_speechlet_response_without_card(speech_output, reprompt_text, should_end_session))

def penn_bookstore_response(intent, session):
    session_attributes = {}
    speech_output = locations[4]
    reprompt_text = ""
    should_end_session = True
    return build_response(session_attributes, build_speechlet_response_without_card(speech_output, reprompt_text, should_end_session))
    
def penn_bookstoreaddl_response(intent, session):
    session_attributes = {}
    speech_output = "You can find what you're looking for at the Penn Bookstore located at" + locations[4]
    reprompt_text = ""
    should_end_session = True
    return build_response(session_attributes, build_speechlet_response_without_card(speech_output, reprompt_text, should_end_session))
    
def penn_card_response(intent, session):
    session_attributes = {}
    speech_output = "You obtain a PennCard from the PennCard center upstairs at the Penn Bookstore located at" + locations[4] + ",be sure to bring a US government issued photo I.D., or a Passport, to the PennCard Center with you!"
    reprompt_text = ""
    should_end_session = True
    return build_response(session_attributes, build_speechlet_response_without_card(speech_output, reprompt_text, should_end_session))
    
def computer_conn_response(intent, session):
    session_attributes = {}
    speech_output = "You can find all your technology needs at Computer Connection upstairs at the Penn Bookstore located at" + locations[4]
    reprompt_text = ""
    should_end_session = True
    return build_response(session_attributes, build_speechlet_response_without_card(speech_output, reprompt_text, should_end_session))

def on_session_ended(session_ended_request, session):
    print("on_session_ended requestId=" + session_ended_request['requestId'] +
          ", sessionId=" + session['sessionId'])

def handle_help_request(intent, session):
    attributes = {}
    speech_output = "You can ask me about staff and faculty members by saying biographies, to hear about places on campus say places, for technology related issues say Wharton Computing, to hear Wharton facts say facts\
    to hear about Wharton simply say wharton."
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