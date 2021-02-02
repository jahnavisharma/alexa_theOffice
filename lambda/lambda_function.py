# -*- coding: utf-8 -*-

# This sample demonstrates handling intents from an Alexa skill using the Alexa Skills Kit SDK for Python.
# Please visit https://alexa.design/cookbook for additional examples on implementing slots, dialog management,
# session persistence, api calls, and more.
# This sample is built using the handler classes approach in skill builder.
import logging
import ask_sdk_core.utils as ask_utils
import random
from ask_sdk_core.skill_builder import SkillBuilder
from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_core.dispatch_components import AbstractExceptionHandler
from ask_sdk_core.handler_input import HandlerInput

from ask_sdk_model import Response

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


class LaunchRequestHandler(AbstractRequestHandler):
    """Handler for Skill Launch."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool

        return ask_utils.is_request_type("LaunchRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "Welcome, you can ask me any quote from The Office."

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )


# class HelloWorldIntentHandler(AbstractRequestHandler):
#     """Handler for Hello World Intent."""
#     def can_handle(self, handler_input):
#         # type: (HandlerInput) -> bool
#         return ask_utils.is_intent_name("HelloWorldIntent")(handler_input)

#     def handle(self, handler_input):
#         # type: (HandlerInput) -> Response
#         speak_output = "Hello World!"

#         return (
#             handler_input.response_builder
#                 .speak(speak_output)
#                 # .ask("add a reprompt if you want to keep the session open for the user to respond")
#                 .response
#         )

class QuotesIntentHandler(AbstractRequestHandler):
    """Handler for Quotes Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("QuotesIntent")(handler_input)

    def handle(self, handler_input):
        name = ""
        slots = handler_input.request_envelope.request.intent.slots
        
        if str(slots['name'].value) != "None":
            name = str(slots['name'].value)
            name = name.lower()
        # type: (HandlerInput) -> Response
        jim = ["One day Michael came in and complained about a speed bump on the highway. I wonder who he ran over then."]
        pam = ["There’s a lot of beauty in ordinary things. Isn’t that kind of the point?", "I don't care what they say about me. I just want to eat."]
        dwight = ["Identity theft is not a joke, Jim! Millions of families suffer every year.", "Bears. Beets. Battlestar Galactica.", "Today, smoking is going to save lives.", "If I were buying my coffin, I would get one with thicker walls so you couldn’t hear the other dead people.", "Whenever I'm about to do something, I think, 'Would an idiot do that?' and if they would, I do not do that thing.", "You only live once? False. You live every day. You only die once."]
        michael = ["Sometimes I’ll start a sentence and I don’t even know where it’s going. I just hope I find it along the way.", "Would I rather be feared or loved? Easy. Both. I want people to be afraid of how much they love me.", "I’m not superstitious, but I am a little stitious.", "The worst thing about prison was the dementors.", "Today, smoking is going to save lives.", "And I knew exactly what to do. But in a much more real sense, I had no idea what to do.", "I am running away from my responsibilities and it feels good.","Should have burned this place down when I had the chance.", "I want people to be afraid of how much they love me.", "That's what she said."]
        andy = ["I wish there was a way to know you're in the good old days before you've actually left them.", "Sorry I annoyed you with my friendship."]
        kevin = ["I just want to lie on the beach and eat hot dogs. That’s all I’ve ever wanted.", "Mini cupcakes? As in the mini version of regular cupcakes? Which is already a mini version of cake? Honestly, where does it end with you people?"]
        angela = ["Sometimes the clothes at Gap Kids are too flashy, so I’m forced to go to the American Girl store and order clothes for large colonial dolls."]
        stanley = ["I’m not superstitious, but I am a little stitious.", "The doctor said, if I can't find a new way to relate more positively to my surroundings, I'm going to die. I'm going to die."]
        kelly = ["I talk a lot, so I’ve learned to tune myself out.", "I am one of the few people who looks hot eating a cupcake."]
        creed = ["I stopped caring a long time ago."]
        general_quotes = jim + pam + dwight + michael + andy + kevin + angela + stanley + kelly + creed 
        speak_output = "Sorry! I don't recognize that."
        if name == "":
            speak_output = random.choice(general_quotes)
        elif name == "jim":
            speak_output = random.choice(jim)
        elif name == "pam":
            speak_output = random.choice(pam)
        elif name == "dwight":
            speak_output = random.choice(dwight)
        elif name == "michael":
            speak_output = random.choice(michael)
        elif name == "andy":
            speak_output = random.choice(andy)
        elif name == "kevin":
            speak_output = random.choice(kevin)
        elif name == "angela":
            speak_output = random.choice(angela)
        elif name == "stanley":
            speak_output = random.choice(stanley)
        elif name == "kelly":
            speak_output = random.choice(kelly)
        elif name == "creed":
            speak_output = random.choice(creed)
            
        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )


class HelpIntentHandler(AbstractRequestHandler):
    """Handler for Help Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("AMAZON.HelpIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "You can say hello to me! How can I help?"

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )


class CancelOrStopIntentHandler(AbstractRequestHandler):
    """Single handler for Cancel and Stop Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return (ask_utils.is_intent_name("AMAZON.CancelIntent")(handler_input) or
                ask_utils.is_intent_name("AMAZON.StopIntent")(handler_input))

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "Goodbye!"

        return (
            handler_input.response_builder
                .speak(speak_output)
                .response
        )


class SessionEndedRequestHandler(AbstractRequestHandler):
    """Handler for Session End."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_request_type("SessionEndedRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response

        # Any cleanup logic goes here.

        return handler_input.response_builder.response


class IntentReflectorHandler(AbstractRequestHandler):
    """The intent reflector is used for interaction model testing and debugging.
    It will simply repeat the intent the user said. You can create custom handlers
    for your intents by defining them above, then also adding them to the request
    handler chain below.
    """
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_request_type("IntentRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        intent_name = ask_utils.get_intent_name(handler_input)
        speak_output = "You just triggered " + intent_name + "."

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )


class CatchAllExceptionHandler(AbstractExceptionHandler):
    """Generic error handling to capture any syntax or routing errors. If you receive an error
    stating the request handler chain is not found, you have not implemented a handler for
    the intent being invoked or included it in the skill builder below.
    """
    def can_handle(self, handler_input, exception):
        # type: (HandlerInput, Exception) -> bool
        return True

    def handle(self, handler_input, exception):
        # type: (HandlerInput, Exception) -> Response
        logger.error(exception, exc_info=True)

        speak_output = "Sorry, I had trouble doing what you asked. Please try again."

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )

# The SkillBuilder object acts as the entry point for your skill, routing all request and response
# payloads to the handlers above. Make sure any new handlers or interceptors you've
# defined are included below. The order matters - they're processed top to bottom.


sb = SkillBuilder()

sb.add_request_handler(LaunchRequestHandler())
# sb.add_request_handler(HelloWorldIntentHandler())
sb.add_request_handler(HelpIntentHandler())
sb.add_request_handler(QuotesIntentHandler())
sb.add_request_handler(CancelOrStopIntentHandler())
sb.add_request_handler(SessionEndedRequestHandler())
sb.add_request_handler(IntentReflectorHandler()) # make sure IntentReflectorHandler is last so it doesn't override your custom intent handlers

sb.add_exception_handler(CatchAllExceptionHandler())

lambda_handler = sb.lambda_handler()