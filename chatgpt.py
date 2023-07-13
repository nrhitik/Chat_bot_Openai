import openai
import pyttsx3
import speech_recognition as sr
import os
  
openai.api_key = os.getenv("OPENAI_API_KEY")

Engine=pyttsx3.init()

def speak(text):
    Engine.say(text)
    Engine.runAndWait()

def audio_to_text():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("reconginzing..")
        query = r.recognize_google(audio, language='en-in')
        return query
    except Exception as e:
        print(e)
        speak("Please say that again...")
        return 'None'

def askbot(question):
    response = openai.Completion.create(
        model='text-davinci-003',
        prompt=question,
        temperature=0.3,
        max_tokens=150,
        top_p=1,
        frequency_penalty=0.5,
        presence_penalty=0.6
    )
    data = response.choices[0].text
    return "bot: " + data.strip()

while True:
    input_text = audio_to_text()
    print(input_text)
    output_text = askbot(input_text)
    print(output_text)
    speak(output_text)

# while True:
#     query = input("Ask a question from Bot: ")
#     text = askbot(query)
#     print(text)

# speak("Hello")
