# pip3 install gtts  
# pip3 install PyObjC

import gtts 
from playsound import playsound

with open('frases.txt','r') as arquivo:
    for linha in arquivo:
        frase = gtts.gTTS(linha, lang='pt',tld='com.br')
        frase.save('frase.mp3')
        playsound('frase.mp3')