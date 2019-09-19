import os
import pyttsx3
import speech_recognition as sr
import time
import random
import winsound
import pip
import numpy as np
from numpy import random_intel

#import tensorflow as tf
#from tensorflow.keras import backend as K
#K.set_session(
#tf.Session(config=tf.ConfigProto(intra_op_parallelism_threads=32, inter_op_parallelism_threads=2)))



def countdown(n):   #setting time
    while n > 0:
        n = n - 1
    if n ==0:
        winsound.PlaySound('sound.wav', winsound.SND_FILENAME)
greet = ['hiee', 'hello', 'yo', 'bonjour', 'holaa', 'salaam' ,'namaste']
sayingbye = ['Goodbye..', 'Adios..', 'Take care....', 'See yaa...', 'Aastala Vista']
donno = ['Come again', "I don't get it",'Speak up' , 'Say something!' , 'Yes?' , "What's your command my lord"]
blus = ['So sweet of you..., Thankyou!', 'Thanks a lot', 'That means a lot, thanks']
engine = pyttsx3.init()
sound=engine.getProperty('voices')
engine.setProperty('voice',sound[2].id)
engine.setProperty('rate',180)  #180 words per minute
engine.setProperty('volume',0.9)
b=1
print("Hi...!")
while b>0:

    # Record Audio
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        try:
            i=r.recognize_google(audio)
            #i=input()
            print(i)
            if i=='exit' or i=='stop' or i=='bye' or i=='quit':
                a1=random.choice(sayingbye)
                print(a1)
                engine.say(a1)
                engine.runAndWait();
                break
            else:
                a=i.split( )
                b=len(a)
                for j in range(0,b):
                    if a[j].lower()=='hello' or a[j].lower=='hi':
                        a2=random.choice(greet)
                        print(a2)
                        engine.say(a2)
                        engine.runAndWait();
                    elif a[j].lower()=='who':
                        if (a[j+1]=='are') and (a[j+2]=='you'):
                            print("I am bubbles. My creator is Bhawani")
                            engine.say("I am bubbles. My creator is Bhawani")
                            engine.runAndWait();
                    elif a[j].lower()=='how':
                        if a[j+1].lower()=='are':
                            print("Everything is awesome, so am i.")
                            engine.say("Everything is awesome, so am i.")
                            engine.runAndWait();
                    elif a[j].lower()=='my':
                        if a[j+1]=='name':
                            if a[j+3].lower()=='sam':
                                print("Hello Intel, It's great to see you...i am sure ur smiling while looking at this, how are you?")
                                engine.say("Hello Intel, It's great to see you...i am sure ur smiling while looking at this, how are you?")
                                engine.runAndWait();

                            elif a[j+3].lower()=='jack':
                                print('Hello DAD, how are you?')
                                engine.say('Hello DAD, how are you?')
                                engine.runAndWait();

                            elif a[j+3].lower()=='duffy':
                                print('Hello MOM, how are you?')
                                engine.say('Hello MOM, how are you?')
                                engine.runAndWait();

                            elif a[j+3].lower()=='tuffy' or a[j+3].lower()=='tuffy':
                                print('Hello sis, how are you?')
                                engine.say('Hello sis, how are you?')
                                engine.runAndWait();
                            else:
                                print("Hello",a[j+3])
                                engine.say("Hello",a[j+3])
                                engine.runAndWait();

                    elif a[j].lower()=='NIT':
                        print("It's my creators college")
                        engine.say("It's my creators college")
                        engine.runAndWait();
                    elif a[j].lower()=='i':
                        if a[j+1].lower()=='am':
                            print("Hello",a[j+2])
                            engine.say("Hello",a[j+2])
                            engine.runAndWait();
                        elif a[j+1].lower()=='want':
                            print("Dont expect much from me, I am in Beta stage")
                            engine.say("Dont expect much from me, I am in Beta stage")
                            engine.runAndWait();
                        elif a[j+1].lower()=="didn't":
                            print("Oh don't deny you liar")
                            engine.say("Oh don't deny you liar")
                            engine.runAndWait();
                    elif a[j].lower()=='start':
                        print("Starting...",a[j+1])
                        engine.say("Starting...",a[j+1])
                        engine.runAndWait();
                        #os.system(a[j+1])
                        if a[j+1].lower()=='calculator':
                            os.system('start calc.exe')
                        elif a[j+1].lower()=='command' and a[j+2].lower()=='prompt':
                            os.system('start cmd')
                        elif a[j+1].lower()=='vlc':
                            os.system('start vlc.exe')
                        elif a[j+1].lower()=='spotify':
                            os.system('start spotify.exe')
                        #elif a[j+1].lower()=='i' and a[j+2].lower()=='heart':
                            #os.system('start iHeartRadio')
                        elif a[j+1].lower()=='chrome':
                            os.system('start chrome.exe')
                        elif a[j+1].lower()=='saavn' or a[j+1].lower()=='sawan':
                            os.system('start saavn')

                            
                    elif a[j].lower()=='set' and a[j+2].lower()=='alarm':
                        print('Setting an alarm for',a[j+4],'seconds')
                        engine.say('Setting an alarm for given seconds')
                        engine.runAndWait();
                        countdown(int(a[j+4])*100)
                    #elif a[j+2].lower()=='awesome' or a[j+2].lower()=='great' or a[j+2].lower()=='intelligent':
                        #a4=random.choice(blus)
                        #print(a4)
                        #engine.say(a4)
                        #engine.runAndWait();
                    elif a[j].lower()=='what' or a[j].lower()=="what's":
                        if a[j+3].lower()=='time':
                            a5=time.strftime("%I:%M:%S")
                            print(a5)
                            engine.say(a5)
                            engine.runAndWait();
                        elif a[j+3].lower()=='date':
                            a6=time.strftime("%d/%m/%Y")
                            print(a6)
                            engine.say(a6)
                            engine.runAndWait();

                    elif (a[j].lower()=='kiki') and a[j+1].lower()=='do' and a[j+2].lower()=='you' and a[j+3].lower()=='love':
                        kiki='Are you riding, say you never ever leave from beside me, cause i need you and i want you, and im down for you always!'
                        print(kiki)
                        engine.say(kiki)
                        engine.runAndWait();   
                    #set reminder

                    elif ((a[j].lower()=='tell') or (a[j].lower()=='any')) and ((a[j+1].lower()=='any') or (a[j+1].lower()=='random') and (a[j+2].lower()=='numbers')):
                        ri=np.random_intel.RandomState(10000)
                        print(ri)
                        engine.say(ri)
                        engine.runAndWait();
                    
        except sr.UnknownValueError:
            a3=random.choice(donno)
            print(a3)
            engine.say(a3)
            engine.runAndWait();
        except sr.RequestError as e:
            print("Oops, there was an error; {0}".format(e))
            engine.say("Oops, there was an error; {0}".format(e))
            engine.runAndWait();

                       
                        
                
                        


            
        
