b=1
print("ENTER THE TEXTS IN THE GIVEN FIELD....TO EXIT THE PROGRAM, TYPE ""exit""")
while b>0:
    i=input("Text: ")
    if i=='exit':
        break
    else:
        a=i.split( )
        b=len(a)
        for j in range(0,b):
            if a[j].lower()=='hello':
                print("Hi...I am your virtual assistant, bubbles")
            elif a[j].lower()=='who':
                if (a[j+1]=='are') and (a[j+2]=='you'):
                    print("I am bubbles. My creator is HoloCaust511")
            elif a[j].lower()=='my':
                if a[j+1]=='name':
                    if a[j].lower()=='harshita':
                        print("Hello Harshita, It's great to see you...i am sure ur smiling while looking at this, how are you?")

                    elif a[j].lower()=='awadhesh':
                        print('Hello DAD, how are you?')

                    elif a[j].lower()=='madhu':
                        print('Hello MOM, how are you?')

                    elif a[j].lower()=='shiwani':
                        print('Hello sis, how are you?')
                    else:
                        print("Hello",a[j+3])

            elif a[j].lower()=='bit':
                print("It's my creators college")
            elif a[j].lower()=='akshay':
                print(a[j],"is my creators' room mate")
            elif a[j].lower()=='harshita':
                print(a[j],"is my dearest friend")
            elif a[j].lower()=='i':
                if a[j+1].lower()=='am':
                    print("Hello",a[j+2])
                elif a[j+1].lower()=='want':
                    print("Dont expect much from me, I am in Beta stage")
            
                    


            
        
