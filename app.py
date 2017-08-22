from chalice import Chalice

app = Chalice(app_name='alexa_chalice')

@app.route('/')
def index():
    with open('chalicelib/test.json') as f:
        data = f.read()
    return data



def template(title, ssml):
    t = {
      "version": "1.0",
      "response": {
        "outputSpeech": {
          "type": "SSML",
          "ssml": ssml
        },
        "card": {
          "type": "Simple",
          "title": title,
          "content": ssml,
        },
        "shouldEndSession": True
      }
    }
    return t
    


@app.lambda_function()
def alexa_handler(event, context):
    if event['request']['type'] == "LaunchRequest":
        with open('chalicelib/hello.ssml') as f:
            ssml = f.read()
        return template('Hello', ssml)
    elif event['request']['type'] == "IntentRequest":
        intent = event['request']['intent']['name']
        if intent == "prosody":
            with open('chalicelib/prosody.ssml') as f:
                ssml = f.read()
            return template('Prosody', ssml)
        elif intent == "number":
            with open('chalicelib/number.ssml') as f:
                ssml = f.read()
            return template('Numbers', ssml)
        elif intent == "audio":
            with open('chalicelib/audio.ssml') as f:
                ssml = f.read()
            return template('Audio', ssml)
        elif intent == "phonenumbers":
            with open('chalicelib/phonenumbers.ssml') as f:
                ssml = f.read()
            return template('Phone Numbers', ssml)
        elif intent == "units":
            with open('chalicelib/units.ssml') as f:
                ssml = f.read()
            return template('Units', ssml)
        elif intent == "spell":
            with open('chalicelib/spell.ssml') as f:
                ssml = f.read()
            return template('Spelling', ssml)
        elif intent == "phonemic":
            with open('chalicelib/phonemic.ssml') as f:
                ssml = f.read()
            return template('Phonemic', ssml)
        elif intent == "role":
            with open('chalicelib/role.ssml') as f:
                ssml = f.read()
            return template('Role', ssml)
        elif intent == "date":
            with open('chalicelib/date.ssml') as f:
                ssml = f.read()
            return template('Dates', ssml)
        elif intent == "speechcon":
            with open('chalicelib/speechcon.ssml') as f:
                ssml = f.read()
            return template('Speechcons', ssml)
        
            
            
