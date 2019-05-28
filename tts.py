# Import the required module for text  
# to speech conversion 
from gtts import gTTS 
  
# This module is imported so that we can  
# play the converted audio 
import os 
  
# The text that you want to convert to audio 
mytext = 'Welcome to the GitHub repository of ujjwal singh baghel!'
mytext2 = 'ujjwal ke GitHub repository me aapka swagat hai'
  
# Language in which you want to convert 
language = 'en'
  
# Passing the text and language to the engine,  
# here we have marked slow=False. Which tells  
# the module that the converted audio should  
# have a high speed 
myobj = gTTS(text=mytext, lang=language, slow=False) 
myobj2 = gTTS(text=mytext2, lang=language, slow=False) 
  
# Saving the converted audio in a mp3 file named 
# welcome  
myobj.save("welcome.mp3") 
myobj2.save("welcome_hindi.mp3") 
  
# Playing the converted file 
os.system("mpg321 welcome.mp3") 
os.system("mpg321 welcome_hindi.mp3") 