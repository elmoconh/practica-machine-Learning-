import os
from gtts import gTTS
    
    
# Options
text_to_read = "Bienvenidos a la universidad de playa ancha"
language = 'es-us'
slow_audio_speed = False
filename = 'my_file.mp3'

def reading_from_string():
    
        audio_created = gTTS(text=text_to_read, lang=language,
                             slow=slow_audio_speed)
        audio_created.save(filename)
        
        os.system(f'start {filename}')

def reading_from_user():
        user_input = input("What text should I read for you?\n")
        audio_created = gTTS(text=user_input, lang=language, slow=slow_audio_speed)
        audio_created.save(filename)
        os.system(f'start {filename}')

def reading_from_file():
        file_to_read = input("Please, insert the name of a file to read:\n") + '.txt'
        f = open(file_to_read, 'r')
        file_text = f.read()
        f.close()
        
        audio_created = gTTS(text=file_text, lang=language, slow=slow_audio_speed)
        audio_created.save(filename)
        
        os.system(f'start {filename}')

if __name__ == '__main__':
        reading_from_string()