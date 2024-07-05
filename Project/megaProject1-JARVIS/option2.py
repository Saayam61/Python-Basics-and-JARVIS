# from openai import OpenAI
# from gtts import gTTS
# import pygame
# import os

# # better sound than pyttsx3 (free for little time)
# def speak(text):
#     tts = gTTS(text)
#     tts.save('temp.mp3')
    
#     # Initialize Pygame mixer
#     pygame.mixer.init()
    
#     # Load the MP3 file
#     pygame.mixer.music.load('temp.mp3')
    
#     # Play the MP3 file
#     pygame.mixer.music.play()
    
#     # Keep the program running until the music stops playing
#     while pygame.mixer.music.get_busy():
#         pygame.time.Clock().tick(10)
        
#     pygame.mixer.music.unload()
#     # os.remove("temp.mp3 ")
    
# # open ai process
# def aiProcess(command):
#     client = OpenAI(
#     api_key="sk-proj-Xh8BPFHKTlKqeACGOrBcT3BlbkFJnv5TAcPELnJGn2ptzDQa",
#     #   api_key="sk-proj-q4MnyT55ILi8uAIVBxbTT3BlbkFJxf9ANh7QhcLsP9pVr3S4",
#     ) 

#     completion = client.chat.completions.create(
#     model="gpt-3.5-turbo",
#     messages=[
#         {"role": "system", "content": "You are a virtual assistant named jarvis, skilled in general tasks like Alexa and Google Cloud. Give short responses please."},
#         {"role": "user", "content": command}
#     ]
#     )

#     return completion.choices[0].message.content