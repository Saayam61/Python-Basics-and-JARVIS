# 3. Install an external module and use it to perform an operation of your interest. 

# step 1: open vscode terminal
# step 2: type pip install pyttsx3 -- used for text to speech

import pyttsx3
engine = pyttsx3.init()
engine.say('''Hacking Started 
           hacking NASA using HTML
           NASA hacking successful''')
engine.runAndWait()