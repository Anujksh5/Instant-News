import sys
def speak(str):
    from win32com.client import Dispatch 
    speak = Dispatch("SAPI.SpVoice")
    speak.Speak(str)

try:
    if __name__ == '__main__':
        import requests
        import json
        # Hello World
        url = ('http://newsapi.org/v2/top-headlines?'
            'country=in&'
            'apiKey=f4c7466fc5ea463cbb0f1a69941c1f3a')
        response = requests.get(url)
        text = response.text
        jscomp = json.loads(text)
        print("_______________Indian News________________")
        speak("Some Indian News headlines")
        for i in range(10):
            print("News " + str(i+1)+ " : " + jscomp['articles'][i]['title'])
            speak("News " + str(i+1)+ " : " + jscomp['articles'][i]['title'])

except KeyboardInterrupt:
    sys.exit()







