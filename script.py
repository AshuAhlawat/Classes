from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

import time
import os


def onlineclassscript(name,id_,pass_,root,method="Microphone",mute=False,noscreen=False,sound=False):

    if sound:
        import playsound
        import speech_recognition as sr
        from gtts import gTTS

        def speak(text):
            tts = gTTS(text=text,lang="en")
            filename = "voice.mp3"
            tts.save(filename)
            playsound.playsound(filename)


    opt = Options()
    
    opt.add_argument("--disable-gpu")
    opt.add_argument("--disable-extensions")

    if mute:
        opt.add_argument("--mute-audio")

    if noscreen:
        opt.add_argument("--window-size=1920,1080")
        opt.add_argument("--start-maximized")
        opt.add_argument("--no-sandbox")
        opt.add_argument('--headless')

    opt.add_experimental_option("prefs", {
        "profile.default_content_setting_values.media_stream_mic":1,
    })

    driver = webdriver.Chrome(options=opt,executable_path=root)

    button = "green"
    poll = "B"
    
    #connecting to login page
    driver.get("https://myclass.lpu.in")

    print(name+": Connecting..")
    if sound:
        speak(name+" connecting")

    #logging in
    username = driver.find_element(By.NAME,"i")
    username.send_keys(id_)
    password = driver.find_element(By.NAME,"p")
    password.send_keys(pass_)
    password.send_keys(Keys.ENTER)

    if sound:
        speak(name+"Logging in")

    print(name+": Logging in..")

    #finding and clicking on Classes/Meetings
    match_search = WebDriverWait(driver,30).until(
        expected_conditions.presence_of_element_located(
            (By.LINK_TEXT, "View Classes/Meetings")
        )
    )
    
    search = driver.find_element(By.LINK_TEXT,"View Classes/Meetings")
    search.click()
    
    #finding any running classes
    match_search = WebDriverWait(driver,30).until(
        expected_conditions.presence_of_element_located(
            (By.CLASS_NAME, "fc-content")
        )
    )

    print(name+": Seeking Class")
    if sound:
        speak(name + ": Seeking Class")
    #joining the running classes
    while True:
        try:
            search = driver.find_element(By.CSS_SELECTOR,'a[style*="background: ' + button +';"]')
            search.click()
            
            match_search = WebDriverWait(driver,30).until(
                expected_conditions.presence_of_element_located(
                    (By.CSS_SELECTOR, 'a[role="button"]')
                )
            )

            search = driver.find_element(By.CSS_SELECTOR,'a[role="button"]')
            search.click()
            

            if sound:
                speak(name+"Entered class")

            print(name+": Entered Class")
            break
        except Exception as e:
            if sound:
                speak(name+" No Class in progress. ")
            driver.close()
            print(name+": No Class in progress. ")
            time.sleep(180)
            onlineclassscript(name,id_,pass_,root,method,mute,noscreen)
        
    #switching to the audio choice frame
    match_search = WebDriverWait(driver,500).until(
        expected_conditions.presence_of_element_located(
            (By.ID, 'frame')
        )
    )
    iframe = driver.find_element(By.ID,'frame')
    driver.switch_to.frame(iframe)
    
    #choosing microphone method
    match_search = WebDriverWait(driver,30).until(
        expected_conditions.presence_of_element_located(
            (By.CSS_SELECTOR, 'button[aria-label="' + method +'"]')
        )
    )
    search = driver.find_element(By.CSS_SELECTOR,'button[aria-label="' + method +'"]')
    search.click()
    if sound:
        speak(name+"Joined via "+method)
    print(name+": Joined via "+method)

    
    #doing echo test
    if method=="Microphone":
        time.sleep(1)
        match_search = WebDriverWait(driver,80).until(
            expected_conditions.presence_of_element_located(
                (By.CSS_SELECTOR, 'button[aria-label="Echo is audible"]')
            )
        )
        search = driver.find_element(By.CSS_SELECTOR,'button[aria-label="Echo is audible"]')
        search.click()
        print(name + ": Echo test cleared")
    
    
    while True:
        try:#to find if class ended
            match_search = WebDriverWait(driver,3).until(
                expected_conditions.presence_of_element_located(
                    (By.CSS_SELECTOR, 'button[aria-label="OK"]')
                )
            )
            #reruning func if class ended to look for new ones 
            driver.close()
            onlineclassscript(name,id_,pass_,root,method,mute,noscreen)
        except:
            try:#to search for polls
                match_search = WebDriverWait(driver,117).until(
                    expected_conditions.presence_of_element_located(
                        (By.CSS_SELECTOR, 'div[class*="pollingContainer"]')
                    )
                )
                #if found
                try:#to click B on poll
                    search = driver.find_element(By.CSS_SELECTOR,'button[aria-label="'+poll+'"]')
                    time.sleep(5)
                    search.click()
                    if sound:
                        speak(name+" Poll Attended B")
                    print(name+": Poll Attended B")
                except Exception as e:#and click Yes if poll doesnt have B
                    search = driver.find_element(By.CSS_SELECTOR,'button[aria-label="Yes"]')
                    time.sleep(5)
                    search.click()
                    if sound:
                        speak(name+" Poll Attended Yes")
                    print(name+": Poll Attended Yes")
            except Exception as e:#if no poll during last 2 mins
                print(name+": class in progress...")
