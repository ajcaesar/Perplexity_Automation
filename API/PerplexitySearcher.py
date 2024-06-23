from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException


#checks for punctuation at the end of a child element indicating that a full sentence has occurred
def has_full_sentence(driver, locator):
    element = driver.find_element(*locator)
    
    # select the children of the div
    children = element.find_elements(By.XPATH, "./*")
    
    # Define a tuple of punctuation marks that can end a sentence
    sentence_endings = ('.', '!', '?')
    
    # Check each child element for a full sentence ending in one of the specified punctuation marks
    for child in children:
        if child.text.strip() and child.text.strip()[-1] in sentence_endings:
            return True
    return False

def GetPerplexityResponse(prompt, chrome_driver_path, max_retries=1, waitTime=10, fullSentence=False, headless=True):   # Replace with the actual path
    service = Service(chrome_driver_path)
    driver = webdriver.Chrome(service=service)

    attempt = 0
    while attempt < max_retries:
        try:
            
            # Navigate to perplexity
            driver.get("https://perplexity.ai")

            # find the textarea and input into it 
            element = driver.find_element(By.CSS_SELECTOR, "textarea[placeholder='Ask anything...']")
            element.send_keys(prompt)
            
            # one second for prompt to load in
            time.sleep(1)

            # find the submit button and execute it using javascript 
            button = driver.find_element(By.CSS_SELECTOR, "button[aria-label='Submit']")
            
            #execute with JS rather than directly editing HTML in case of popups
            driver.execute_script("arguments[0].click();", button)
            
            # this is the element that contains the spans which hold the text response
            parent_locator = (By.CSS_SELECTOR, "div.prose")
            
            # if the user wants one sentence then wait until a sentence is detected (or until waitTime)
            if(fullSentence):
                WebDriverWait(driver, waitTime).until(lambda driver: has_full_sentence(driver, parent_locator))
            
            # if not, then wait the specified wait time
            else:
                time.sleep(waitTime)

            # Retrieve the text of the element which now contains at least one full sentence
            response = driver.find_element(*parent_locator).text
            break

        except TimeoutException as e:
            print(f"Timeout on attempt {attempt+1}: {e}")
            attempt += 1

        except Exception as e:
            print(e)
            response = "Failed to retrieve response."
            break

    driver.close()
    return response
