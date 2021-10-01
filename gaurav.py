#Download Python
#Download Chrome WebDriver Version 88 and paste it in ProgramData in C Drive
#pip install selenium

# Your id below
id_ = "12014917"
# your password below
pass_ = "Patel652002#"

methods = ["Microphone","Listen only"]
method = methods[0]

button = "green"

poll = "B"

mute = True

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

#setting permissions to the browser
opt = Options()
opt.add_argument("start-maximized")
opt.add_experimental_option("prefs", { \
    "profile.default_content_setting_values.media_stream_mic":1,
})

driver = webdriver.Chrome(options=opt,executable_path="./chromedriver")

if mute:
    driver.get("chrome://settings/content/sound")

    def expand_shadow_element(element):
        shadow_root = driver.execute_script('return arguments[0].shadowRoot', element)
        return shadow_root
    
    shadow1 = expand_shadow_element(driver.find_element_by_tag_name("settings-ui"))
    shadow2 = expand_shadow_element(shadow1.find_element_by_tag_name("settings-main"))
    shadow3 = expand_shadow_element(shadow2.find_element_by_tag_name("settings-basic-page"))
    shadow4 = expand_shadow_element(shadow3.find_element_by_tag_name("settings-privacy-page"))
    shadow5 = expand_shadow_element(shadow4.find_element_by_tag_name("settings-category-default-radio-group"))
    shadow6 = expand_shadow_element(shadow5.find_element_by_name("0"))
    match = shadow6.find_element_by_class_name("disc-wrapper")

    match.click()
   

#the class joining function
def onlineclassscript():
    
    #connecting to login page
    driver.get("https://myclass.lpu.in")

    #logging in
    username = driver.find_element_by_name("i")
    username.send_keys(id_)
    password = driver.find_element_by_name("p")
    password.send_keys(pass_)
    password.send_keys(Keys.ENTER)

    #finding and clicking on Classes/Meetings
    match_search = WebDriverWait(driver,20).until(
        expected_conditions.presence_of_element_located(
            (By.LINK_TEXT, "View Classes/Meetings")
        )
    )

    search = driver.find_element_by_link_text("View Classes/Meetings")
    search.click()
    
    #finding any running classes
    match_search = WebDriverWait(driver,20).until(
        expected_conditions.presence_of_element_located(
            (By.CLASS_NAME, "fc-content")
        )
    )
    #joining the running classes
    import time
    while True:
        try:
            time.sleep(1)
            search = driver.find_element_by_css_selector('a[style*="background: '+ button +';"]')
            search.click()
            print("Entered Class")
            break
        except Exception as e:
            print(" No Class in progress. ")
            time.sleep(180)
            onlineclassscript()
    
    match_search = WebDriverWait(driver,20).until(
        expected_conditions.presence_of_element_located(
            (By.CSS_SELECTOR, 'a[role="button"]')
        )
    )
    search = driver.find_element_by_css_selector('a[role="button"]')
    search.click()
    
    #switching to the audio choice frame
    match_search = WebDriverWait(driver,400).until(
        expected_conditions.presence_of_element_located(
            (By.ID, 'frame')
        )
    )
    iframe = driver.find_element_by_id('frame')
    driver.switch_to.frame(iframe)
    
    #choosing microphone method
    match_search = WebDriverWait(driver,20).until(
        expected_conditions.presence_of_element_located(
            (By.CSS_SELECTOR, 'button[aria-label="' + method +'"]')
        )
    )
    search = driver.find_element_by_css_selector('button[aria-label="' + method +'"]')
    search.click()
    print("Joined via "+method)
    #doing echo test
    if method=="Microphone":
        match_search = WebDriverWait(driver,20).until(
            expected_conditions.presence_of_element_located(
                (By.CSS_SELECTOR, 'button[aria-label="Echo is audible"]')
            )
        )
        search = driver.find_element_by_css_selector('button[aria-label="Echo is audible"]')
        search.click()
    
    #waiting for class end
    while True:
        try:
            match_search = WebDriverWait(driver,3).until(
                expected_conditions.presence_of_element_located(
                    (By.CSS_SELECTOR, 'button[aria-label="OK"]')
                )
            )
            #joining any next class if any 
            onlineclassscript()
        except:
            try:
                match_search = WebDriverWait(driver,117).until(
                    expected_conditions.presence_of_element_located(
                        (By.CSS_SELECTOR, 'div[class*="pollingContainer"]')
                    )
                )
                try:
                    search = driver.find_element_by_css_selector('button[aria-label="'+poll+'"]')
                    time.sleep(8)
                    search.click()
                    print("Poll Attended B")
                except Exception as e:
                    search = driver.find_element_by_css_selector('button[aria-label="Yes"]')
                    time.sleep(5)
                    search.click()
                    print("Poll Attended Yes")
            except Exception as e:
                print("class in progress...")
            

onlineclassscript()
