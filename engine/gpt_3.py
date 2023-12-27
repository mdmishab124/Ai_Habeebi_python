import openai
import speech_recognition as sr
import pyttsx3
import asyncio
import time
import eel

# Set up text-to-speech engine with a slower rate
engine = pyttsx3.init()
engine.setProperty('rate', 130)  # Adjust the rate as needed

# Function to convert text to speech
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Set up OpenAI API key (replace 'YOUR_API_KEY' with your actual key)
openai.api_key = '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'

async def process_input(query):
    print("Generating response with GPT-3.")
    # speak("Just wait, Because I am something slow")

    # Generate response with GPT-3
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=query,
        max_tokens=150
    )
    reply = response.choices[0].text.strip()

    # Print and speak the response
    print("GPT-3 says:", reply)
    speak(reply)

@eel.expose
async def main():
    while True:
        print("Call me Habeebi, After ask me something...")
        speak("Asssalaamu aalaikum, Call me Habeebi, After ask me something...")
        try:
            # Listen for voice input
            with sr.Microphone() as source:
                recognizer = sr.Recognizer()
                recognizer.adjust_for_ambient_noise(source, duration=1)
                audio = recognizer.listen(source, timeout=5)

            # Convert voice to text
            query = recognizer.recognize_google(audio)
            print("You said:", query)

            # Check if the user said "habibi" to generate response
            if "habibi" in query.lower():
                if "habibi" and "what is your name" in query.lower():
                    speak("Habeebi, I am Habeebi")
                else:
                    # Start the response generation asynchronously
                    await asyncio.gather(process_input(query))
                    time.sleep(2)  # Add a delay after each response to give users time to speak again

        except sr.UnknownValueError:
            print("Sorry, I couldn't understand the audio. Please try again.")

        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")

if __name__ == "__main__":
    asyncio.run(main())
