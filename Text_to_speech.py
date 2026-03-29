from gtts import gTTS
import os

# Text to convert
mytext = 'Hello shubham pawar'
language = 'en'

# Generate speech
myobj = gTTS(text=mytext, lang=language, slow=False)
myobj.save("hello.mp3")

# Cross-platform playback (works everywhere)
if os.name == 'nt':  # Windows
    os.system('start hello.mp3')
elif os.name == 'posix':  # macOS/Linux
    os.system('afplay hello.mp3')  # macOS
    # os.system('mpg321 hello.mp3')  # Linux (if mpg321 installed)
else:
    print("Generated hello.mp3 - play manually")
