import speech_recognition as sr

# get audio from the microphone
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Speak:")
    audio = r.listen(source)

chorus = 'How Great \n Is Our God \n Sing With Me'
verse1 = 'He wraps himself in light \n And darkness tries to hide \n And trembles at His voice \n Trembles at His voice'

chorus_break = chorus.split()
verse1_break = verse1.split()

currentSlide = chorus

try:
    if r.recognize_google(audio) == chorus_break[-1] & currentSlide == 'chorus':
        print(f"The Slide is currently, {currentSlide} and is changing.")
        currentSlide = 'verse1'

    elif r.recognize_google(audio) == verse1_break[-1] & currentSlide == 'verse1':
        print(f"The Slide is currently, {currentSlide} and is changing.")
        currentSlide = 'chorus'
    # print("You said " + r.recognize_google(audio))
except sr.UnknownValueError:
    print("Could not understand audio")
except sr.RequestError as e:
    print("Could not request results; {0}".format(e))





# if r.recognize_google(audio)) == keyword:
    #Next Slide
    #Click Location



# Maybe Type Song Name, Python can go get lyrics from internet. Take the results and parse them into slides
# then label those slides and auto shift through them.
