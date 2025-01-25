import win32com.client as wcl

speaker = wcl.Dispatch("SAPI.SpVoice") 
li= ["Abeer" , 'nono', "samir", "koko"] # a list pf my friend in fb


speaker.Speak("Hello, I am your computer, I am here to help you with your shoutout project") 
def shoutOut():
    for i in li:
        shout= "Shout out to "+i
        speaker.Speak(shout)
shoutOut()