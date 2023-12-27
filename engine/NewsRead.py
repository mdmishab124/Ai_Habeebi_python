# import requests
# import json
# import pyttsx3
# from Jarvis_main import takeCommand

# engine = pyttsx3.init("sapi5")
# voices = engine.getProperty("voices")
# engine.setProperty("voice", voices[0].id)
# rate = engine.setProperty("rate",170)

# def speak(audio):
#     engine.say(audio)
#     engine.runAndWait()

# def latestnews():
#     api_dict = {"business" :"133beb853c4d4439b4065c4630b0578a" ,#Enter Your OWN API ,
#             "entertainment" : "133beb853c4d4439b4065c4630b0578a",#Enter Your OWN API ,
#             "health" : "133beb853c4d4439b4065c4630b0578a",#Enter Your OWN API,
#             "science" :"133beb853c4d4439b4065c4630b0578a",#Enter Your OWN API,
#             "sports" :"133beb853c4d4439b4065c4630b0578a",#Enter Your OWN API,
#             "technology" :"133beb853c4d4439b4065c4630b0578a"#Enter Your OWN API
# }

#     content = None
#     url = None
#     speak("Which field news do you want, [business] , [health] , [technology], [sports] , [entertainment] , [science]")
#     field = takeCommand().lower()
#     for key ,value in api_dict.items():
#         if key.lower() in field.lower():
#             url = value
#             print(url)
#             print("url was found")
#             break
#         else:
#             url = True
#     if url is True:
#         print("url not found")

#     news = requests.get(url).text
#     news = json.loads(news)
#     speak("Here is the first news.")

#     arts = news["articles"]
#     for articles in arts :
#         article = articles["title"]
#         print(article)
#         speak(article)
#         news_url = articles["url"]
#         print(f"for more info visit: {news_url}")

#         a = input("[press 1 to cont] and [press 2 to stop]")
#         if str(a) == "1":
#             pass
#         elif str(a) == "2":
#             break
        
#     speak("thats all")


import requests
import json
import pyttsx3
from command import takecommand

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate", 170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def latestnews():
    api_dict = {
        "business": "business",
        "entertainment": "entertainment",
        "health": "health",
        "science": "science",
        "sports": "sports",
        "technology": "technology"
    }

    content = None
    base_url = "https://newsapi.org/v2/top-headlines"
    api_key = "133beb853c4d4439b4065c4630b0578a"  # Replace with your actual API key

    speak("Which field news do you want, [business], [health], [technology], [sports], [entertainment], [science]")
    field = takecommand().lower()

    # Check if the field is present in the api_dict
    for key, value in api_dict.items():
        if key.lower() in field:
            category = value
            print(category)
            print("Category was found")
            break
    else:
        # If no match found, handle accordingly
        print("Category not found")
        return

    url = f"{base_url}?category={category}&apiKey={api_key}"

    news = requests.get(url).text
    news = json.loads(news)
    speak("Here is the first news.")

    arts = news.get("articles", [])
    for articles in arts:
        article = articles.get("title", "")
        if article:
            print(article)
            speak(article)
            news_url = articles.get("url", "")
            if news_url:
                print(f"For more info visit: {news_url}")
                speak("Would you like to continue? Please respond with 'yes' or 'no'.")
                continue_news = takecommand().lower()
                if continue_news == "yes":
                    pass
                elif continue_news == "no":
                    break

    speak("That's all")

# Uncomment the following line if you want to run this code directly
# latestnews()

