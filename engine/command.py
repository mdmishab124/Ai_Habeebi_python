# # import openai
# # import speech_recognition as sr
# # import pyttsx3
# # import asyncio
# # import time
# # import eel

# # # Function to convert text to speech
# # # def speak(text):
# # #     engine = pyttsx3.init('sapi5')
# # #     voices = engine.getProperty('voices') 
# # #     engine.setProperty('voice', voices[0].id)
# # #     engine.setProperty('rate', 174)
# # #     print(voices)
# # #     engine.say(text)
# # #     engine.runAndWait()

# # engine = pyttsx3.init()
# # engine.setProperty('rate', 130)  # Adjust the rate as needed

# # # Function to convert text to speech
# # def speak(text):
# #     engine.say(text)
# #     engine.runAndWait()

# # # Set up OpenAI API key (replace 'YOUR_API_KEY' with your actual key)
# # openai.api_key = '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'

# # async def process_input(query):
# #     print("Generating response with GPT-3.")
# #     # speak("Just wait, Because I am something slow")

# #     # Generate response with GPT-3
# #     response = openai.Completion.create(
# #         engine="text-davinci-003",
# #         prompt=query,
# #         max_tokens=150
# #     )
# #     reply = response.choices[0].text.strip()

# #     # Print and speak the response
# #     print("GPT-3 says:", reply)
# #     speak(reply)


# # @eel.expose
# # def takecommand():

# #     response = sr.Recognizer()

# #     with sr.Microphone() as source:
# #         print('listening....')
# #         eel.DisplayMessage('listening...')
# #         response.pause_threshold = 1
# #         response.adjust_for_ambient_noise(source)
        
# #         audio = response.listen(source, 10, 6)

# #     try:
# #         print('recognizing')
# #         query = response.recognize_google(audio, language='en-in')
# #         print(f"user said: {query}")
# #         eel.DisplayMessage(query)
# #         speak(query)
# #         asyncio.gather(process_input(query))
# #         time.sleep(2)  # Add a delay after each response to give users time to speak again
# #     except Exception as e:
# #         return ""
    
# #     return query.lower()

# import openai
# import speech_recognition as sr
# import pyttsx3
# import asyncio
# import time
# import eel

# engine = pyttsx3.init()
# engine.setProperty('rate', 130)

# # Set up OpenAI API key (replace 'YOUR_API_KEY' with your actual key)
# openai.api_key = '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'

# def speak(text):
#     engine.say(text)
#     engine.runAndWait()

# async def process_input(query):
#     print("Generating response with GPT-3.")
#     response = openai.Completion.create(
#         engine="text-davinci-003",
#         prompt=query,
#         max_tokens=150
#     )
#     reply = response.choices[0].text.strip()
#     print("GPT-3 says:", reply)
#     eel.DisplayMessage(reply)
#     speak(reply)

# @eel.expose
# def takecommand():
#     recognizer = sr.Recognizer()

#     with sr.Microphone() as source:
#         print('listening....')
#         eel.DisplayMessage('listening...')
#         recognizer.pause_threshold = 1
#         recognizer.adjust_for_ambient_noise(source)
        
#         audio = recognizer.listen(source, timeout=10, phrase_time_limit=6)

#     try:
#         print('recognizing')
#         query = recognizer.recognize_google(audio, language='en-in')
#         print(f"user said: {query}")
#         eel.DisplayMessage(query)
#         speak(query)
#         asyncio.run(process_input(query))
#         time.sleep(2)
#     except sr.UnknownValueError:
#         print("Speech Recognition could not understand audio")
#     except sr.RequestError as e:
#         print(f"Could not request results from Google Speech Recognition service; {e}")
#     except Exception as e:
#         print(f"An error occurred: {e}")
    
#     return query.lower()



# import openai
# import speech_recognition as sr
# import pyttsx3
# import asyncio
# import eel

# engine = pyttsx3.init()
# engine.setProperty('rate', 130)

# # Set up OpenAI API key (replace 'YOUR_API_KEY' with your actual key)
# openai.api_key = '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'

# def speak(text):
#     engine.say(text)
#     engine.runAndWait()

# async def process_input(query):
#     print("Generating response with GPT-3.")
#     response = openai.Completion.create(
#         engine="text-davinci-003",
#         prompt=query,
#         max_tokens=150
#     )
#     reply = response.choices[0].text.strip()
#     print("GPT-3 says:", reply)
#     speak(reply)

# @eel.expose
# def takecommand():
#     recognizer = sr.Recognizer()

#     while True:
#         with sr.Microphone() as source:
#             print('listening....')
#             eel.DisplayMessage('listening...')
#             recognizer.pause_threshold = 1
#             recognizer.adjust_for_ambient_noise(source)
            
#             audio = recognizer.listen(source, timeout=10, phrase_time_limit=6)

#         try:
#             print('recognizing')
#             query = recognizer.recognize_google(audio, language='en-in')
#             print(f"user said: {query}")
#             eel.DisplayMessage(query)
#             speak(query)
#             asyncio.run(process_input(query))
#         except sr.UnknownValueError:
#             print("Speech Recognition could not understand audio")
#         except sr.RequestError as e:
#             print(f"Could not request results from Google Speech Recognition service; {e}")
#         except Exception as e:
#             print(f"An error occurred: {e}")



















# import openai
# import speech_recognition as sr
# import pyttsx3
# import asyncio
# import eel

# engine = pyttsx3.init()
# engine.setProperty('rate', 130)

# # Set up OpenAI API key (replace 'YOUR_API_KEY' with your actual key)
# openai.api_key = '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'

# def speak(text):
#     engine.say(text)
#     engine.runAndWait()
    
# async def process_input(query):
#     print("Generating response with GPT-3.")
#     response = openai.Completion.create(
#         engine="text-davinci-003",
#         prompt=query,
#         max_tokens=150
#     )
#     reply = response.choices[0].text.strip()
#     print("GPT-3 says:", reply)
#     eel.DisplayMessage(reply)
#     speak(reply)

# @eel.expose
# def takecommand():
#     recognizer = sr.Recognizer()

#     while True:
#         with sr.Microphone() as source:
#             print('listening....')
#             eel.DisplayMessage('listening...')
#             recognizer.pause_threshold = 1
#             recognizer.adjust_for_ambient_noise(source)
            
#             audio = recognizer.listen(source, timeout=10, phrase_time_limit=6)

#         try:
#             print('recognizing')
#             eel.DisplayMessage('recognizing...')
#             query = recognizer.recognize_google(audio, language='en-in')
#             print(f"user said: {query}")           

#             if query.lower() == "stop":
#                 print("Stopping the program.")
#                 speak("Okey sir, Have a good day")
#                 break

#             asyncio.run(process_input(query))
#         except sr.UnknownValueError:
#             print("Speech Recognition could not understand audio")
#         except sr.RequestError as e:
#             print(f"Could not request results from Google Speech Recognition service; {e}")
#         except Exception as e:
#             print(f"An error occurred: {e}")












# import openai
# import speech_recognition as sr
# import pyttsx3
# import asyncio
# import eel
# import os  # Import the os module

# engine = pyttsx3.init()
# engine.setProperty('rate', 130)

# # Set up OpenAI API key (replace 'YOUR_API_KEY' with your actual key)
# openai.api_key = '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'

# listening = True  # Variable to control the listening state

# def speak(text):
#     engine.say(text)
#     engine.runAndWait()

# async def process_input(query):
#     print("Generating response with GPT-3.")
#     response = openai.Completion.create(
#         engine="text-davinci-003",
#         prompt=query,
#         max_tokens=150
#     )
#     reply = response.choices[0].text.strip()
#     print("GPT-3 says:", reply)
#     eel.DisplayMessage(reply)
#     speak(reply)

# @eel.expose
# def takecommand():
#     global listening

#     recognizer = sr.Recognizer()

#     while listening:
#         with sr.Microphone() as source:
#             print('listening....')
#             eel.DisplayMessage('listening...')
#             recognizer.pause_threshold = 1
#             recognizer.adjust_for_ambient_noise(source)

#             audio = recognizer.listen(source, timeout=10, phrase_time_limit=6)

#         try:
#             print('recognizing')
#             eel.DisplayMessage('recognizing...')
#             query = recognizer.recognize_google(audio, language='en-in')
#             print(f"user said: {query}")

#             if query.lower() == "stop":
#                 print("Stopping the replies. Listening is paused.")
#                 speak("Okey sir, replies paused. Say 'start' to resume.")
#                 listening = False
#             else:
#                 asyncio.run(process_input(query))

#         except sr.UnknownValueError:
#             print("Speech Recognition could not understand audio")
#         except sr.RequestError as e:
#             print(f"Could not request results from Google Speech Recognition service; {e}")
#         except Exception as e:
#             print(f"An error occurred: {e}")

# @eel.expose
# def resume_listening():
#     global listening
#     listening = True
#     print("Resuming listening. Say 'stop' to pause replies again.")

# eel.init("www")

# # Use double quotes for the command and URL to avoid escaping issues
# os.system('start msedge.exe --app="http://localhost:8000/index.html"')

# # Use a more specific host and port for eel.start
# eel.start('index.html', mode=None, host='localhost', port=8000, block=True)





# import openai
# import speech_recognition as sr
# import pyttsx3
# import asyncio
# import eel
# import os  # Import the os module

# engine = pyttsx3.init()
# engine.setProperty('rate', 130)

# # Set up OpenAI API key (replace 'YOUR_API_KEY' with your actual key)
# openai.api_key = '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'

# listening = True  # Variable to control the listening state

# def speak(text):
#     engine.say(text)
#     engine.runAndWait()

# async def process_input(query):
#     print("Generating response with GPT-3.")
#     response = openai.Completion.create(
#         engine="text-davinci-003",
#         prompt=query,
#         max_tokens=150
#     )
#     reply = response.choices[0].text.strip()
#     print("GPT-3 says:", reply)
#     return reply

# @eel.expose
# def takecommand():
#     global listening

#     recognizer = sr.Recognizer()

#     while listening:
#         with sr.Microphone() as source:
#             print('listening....')
#             eel.DisplayMessage('listening...')
#             recognizer.pause_threshold = 1
#             recognizer.adjust_for_ambient_noise(source)

#             audio = recognizer.listen(source, timeout=10, phrase_time_limit=6)

#         try:
#             print('recognizing')
#             eel.DisplayMessage('recognizing...')
#             query = recognizer.recognize_google(audio, language='en-in')
#             print(f"user said: {query}")

#             if query.lower() == "stop":
#                 print("Stopping the replies. Listening is paused.")
#                 speak("Okey sir, replies paused. Say 'start' to resume.")
#                 listening = False
#             else:
#                 reply = asyncio.run(process_input(query))
#                 eel.DisplayMessage(reply)
#                 speak(reply)

#         except sr.UnknownValueError:
#             print("Speech Recognition could not understand audio")
#         except sr.RequestError as e:
#             print(f"Could not request results from Google Speech Recognition service; {e}")
#         except Exception as e:
#             print(f"An error occurred: {e}")

# @eel.expose
# def resume_listening():
#     global listening
#     listening = True
#     print("Resuming listening. Say 'stop' to pause replies again.")

# eel.init("www")

# # Use double quotes for the command and URL to avoid escaping issues
# os.system('start msedge.exe --app="http://localhost:8000/index.html"')

# # Use a more specific host and port for eel.start
# eel.start('index.html', mode=None, host='localhost', port=8000, block=True)





# BEST CODE 




import openai
import speech_recognition as sr
import pyttsx3
import asyncio
import eel
import os

eel.init('web') 

engine = pyttsx3.init()
engine.setProperty('rate', 130)

# Set up OpenAI API key (replace 'YOUR_API_KEY' with your actual key)
openai.api_key = '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'

listening = True  # Variable to control the listening state

def speak(text):
    engine.say(text)
    engine.runAndWait()

async def process_input(query):
    print("Generating response with GPT-3.")
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=query,
        max_tokens=150
    )
    reply = response.choices[0].text.strip()
    print("GPT-3 says:", reply)
    return reply

@eel.expose
def start_assistant():
    eel.controller('startAssistant();')

@eel.expose
def stop_assistant():
    eel.controller('stopAssistant();')

@eel.expose
def takecommand():
    global listening
    speak("You can start talking.")
    recognizer = sr.Recognizer()
    while True:
        with sr.Microphone() as source:
            print('listening....')
            eel.DisplayMessage('listening...')
            recognizer.pause_threshold = 1
            recognizer.adjust_for_ambient_noise(source)
            # audio = recognizer.listen(source, timeout=10, phrase_time_limit=6)
            audio = recognizer.listen(source)


        try:
            print('recognizing')
            eel.DisplayMessage('recognizing...')
            query = recognizer.recognize_google(audio, language='en-in')
            print(f"user said: {query}")
            eel.DisplayMessage("User Said :" + query)
                
            if "wake up" in query.lower():
                print("Resuming listening.")
                speak("Resuming replies. You can start talking.")
                listening = True
                eel.start_assistant()
            elif "go to sleep" in query.lower():
                print("Stopping the replies. Listening is paused.")
                speak("Okey sir, replies paused. Say 'wake up' to resume.")
                listening = False
                eel.stop_assistant()
            elif "google" in query or "Google" in query.lower():
                from SearchNow import searchGoogle
                searchGoogle(query)
            elif "youtube" in query or "Youtube" in query.lower():
                from SearchNow import searchYoutube
                searchYoutube(query)
            elif "wikipedia" in query.lower():
                from SearchNow import searchWikipedia
                searchWikipedia(query)
            else:
                reply = asyncio.run(process_input(query))
                eel.DisplayMessage(reply)
                speak(reply)

        except sr.UnknownValueError:
            print("Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")
        except Exception as e:
            print(f"An error occurred: {e}")






# import openai
# import speech_recognition as sr
# import pyttsx3
# import asyncio
# import eel
# import os

# engine = pyttsx3.init()
# engine.setProperty('rate', 130)

# # Set up OpenAI API key (replace 'YOUR_API_KEY' with your actual key)
# openai.api_key = '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'
# completion = openai.Completion()

# listening = True  # Variable to control the listening state

# def speak(text):
#     engine.say(text)
#     engine.runAndWait()

# async def process_input(query):
#     print("Generating response with GPT-3.")
#     response = openai.Completion.create(
#         engine="text-davinci-003",
#         prompt=query,
#         max_tokens=150
#     )
#     reply = response.choices[0].text.strip()
#     print("GPT-3 says:", reply)
#     return reply

# # Replay of Habeebi
# def ReplyIt(question,chat_log = None):
        
#     prompt = f'{chat_log}You : {question}\nJarvis : '
#     response = completion.create(
#         model = "text-davinci-003",
#         prompt=prompt,
#         temperature = 0.5,
#         max_tokens = 60,
#         top_p = 0.3,
#         frequency_penalty = 0.5,
#         presence_penalty = 0)
#     answer = response.choices[0].text.strip()
#     return answer

# # @eel.expose
# # def start_assistant():
# #     eel.execute_js('startAssistant();')

# # @eel.expose
# # def stop_assistant():
# #     eel.execute_js('stopAssistant();')

# @eel.expose
# def takecommand():
#             global listening

#             recognizer = sr.Recognizer()

            
#             with sr.Microphone() as source:
#                 print('listening....')
#                 eel.DisplayMessage('listening...')
#                 recognizer.pause_threshold = 1
#                 recognizer.adjust_for_ambient_noise(source)

#                 # audio = recognizer.listen(source, timeout=10, phrase_time_limit=6)
#                 audio = recognizer.listen(source)
#             try:
#                 print('recognizing')
#                 eel.DisplayMessage('recognizing...')
#                 query = recognizer.recognize_google(audio, language='en-in')
#                 print(f"user said: {query}")
                        
#                         # if "wake up" in query.lower():
#                         #     print("Resuming listening.")
#                         #     speak("Resuming replies. You can start talking.")
#                         #     listening = True
#                         #     @eel.expose
#                         #     def start_assistant():
#                         #         eel.execute_js('startAssistant();')
#                         # if "go to sleep" in query.lower():
#                         #     print("Stopping the replies. Listening is paused.")
#                         #     speak("Okey sir, replies paused. Say 'wake up' to resume.")
#                         #     listening = False
#                         #     @eel.expose
#                         #     def stop_assistant():
#                         #         eel.execute_js('stopAssistant();')

#             except sr.UnknownValueError:
#                 print("Speech Recognition could not understand audio")
#             except sr.RequestError as e:
#                 print(f"Could not request results from Google Speech Recognition service; {e}")
#             except Exception as e:
#                 print(f"An error occurred: {e}")
#             return query


# if __name__ == "__main__":
#     while True:
#         query = takecommand().lower()
#         if "wake up" in query.lower():
#             print("Resuming listening.")
#             speak("Resuming replies. You can start talking.")
#             # listening = True
#             from GreetMe import greetMe
#             greetMe()
#             @eel.expose
#             def start_assistant():
#                 eel.execute_js('startAssistant();')
#             while True:
#                 query = takecommand().lower()
#                 if "go to sleep" in query.lower():
#                     print("Stopping the replies. Listening is paused.")
#                     speak("Okey sir, replies paused. Say 'wake up' to resume.")
#                     # listening = False
#                     @eel.expose
#                     def stop_assistant():
#                         eel.execute_js('stopAssistant();')
#                     break
#                 elif "google" in query:
#                     from SearchNow import searchGoogle
#                     searchGoogle(query)
#                 elif "Youtube" in query:
#                     from SearchNow import searchYoutube
#                     searchYoutube(query)
#                 elif "wikipedia" in query:
#                     from SearchNow import searchWikipedia
#                     searchWikipedia(query)
#                 elif listening:
#                     reply = asyncio.run(process_input(query))
#                     eel.DisplayMessage(reply)
#                     speak(reply)
#                 else:
#                     # def MAIN():
#                         # speak("Hello Sir, I'm Habeebi")
#                         while True:
#                             Data = takecommand()
#                             Data = str(Data)

#                             if len(Data) < 3:
#                                 pass

#                             else:
#                                 Reply = ReplyIt(Data)
#                                 print("AI  : ",Reply)
#                                 speak(Reply)
#                                 break

#                     # MAIN()









# import openai
# import speech_recognition as sr
# import pyttsx3
# import asyncio
# import eel
# import os
# # Update the import statement in controller.py
# from SearchNow import searchGoogle, searchYoutube, searchWikipedia


# engine = pyttsx3.init()
# engine.setProperty('rate', 130)

# # Set up OpenAI API key (replace 'YOUR_API_KEY' with your actual key)
# openai.api_key = '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'

# listening = True  # Variable to control the listening state

# def speak(text):
#     engine.say(text)
#     engine.runAndWait()

# async def process_input(query):
#     print("Generating response with GPT-3.")
#     response = openai.Completion.create(
#         engine="text-davinci-003",
#         prompt=query,
#         max_tokens=150
#     )
#     reply = response.choices[0].text.strip()
#     print("GPT-3 says:", reply)
#     return reply



# @eel.expose
# def takecommand():
#     global listening

#     recognizer = sr.Recognizer()

#     while True:
#         with sr.Microphone() as source:
#             print('listening....')
#             eel.DisplayMessage('listening...')
#             recognizer.pause_threshold = 1
#             recognizer.adjust_for_ambient_noise(source)

#             # audio = recognizer.listen(source, timeout=10, phrase_time_limit=6)
#             audio = recognizer.listen(source)


#         try:
#             print('recognizing')
#             eel.DisplayMessage('recognizing...')
#             query = recognizer.recognize_google(audio, language='en-in')
#             print(f"user said: {query}")
                
#             if "wake up" in query.lower():
#                 print("Resuming listening.")
#                 speak("Resuming replies. You can start talking.")
#                 listening = True
#                 eel.startAssistant()
#             elif "go to sleep" in query.lower():
#                 print("Stopping the replies. Listening is paused.")
#                 speak("Okey sir, replies paused. Say 'wake up' to resume.")
#                 listening = False
#                 eel.stopAssistant()
#             elif "google" in query or "Google" in query.lower():
#                 searchGoogle(query)
#             elif "youtube" in query or "Youtube" in query.lower():
#                 searchYoutube(query)
#             elif "wikipedia" in query.lower():
#                 searchWikipedia(query)
#             else:
#                 reply = asyncio.run(process_input(query))
#                 eel.DisplayMessage(reply)
#                 speak(reply)

#         except sr.UnknownValueError:
#             print("Speech Recognition could not understand audio")
#         except sr.RequestError as e:
#             print(f"Could not request results from Google Speech Recognition service; {e}")
#         except Exception as e:
#             print(f"An error occurred: {e}")



