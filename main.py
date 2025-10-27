import pyttsx3

def speak(text):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.setProperty('rate', 150)
    engine.setProperty('volume', 1.0)
    engine.say(text)
    engine.runAndWait()
    engine.stop()

print("🤖 Hello, I am AI bot. Type something for me to say.")
print("Type 'exit' to stop.\n")

while True:
    text = input("User: ").strip()
    if text.lower() == "exit":
        speak("Goodbye! Talk soon!")
        print("👋 Shutting down...")
        break
    if text:
        speak(text)
