import pyttsx3

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Sample list of statements
statements = [
"आज की ताजा खबर, हिंदी न्यूज़ 24 अगस्त 2024",
"Hello Aryakumar!!You are good person.",
"Soon you will meet your future wife"
]
i=0
# Loop through each statement and speak it
while(i<=1):

    for statement in statements:
        print(statement)  # Print the statement
        engine.say(statement)  # Speak the statement
        engine.runAndWait()  # Blocks while processing all the currently queued commands
    i+=1
