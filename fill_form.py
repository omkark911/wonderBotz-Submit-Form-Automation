from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# List of browsers to test
browsers = ["chrome", "firefox", "edge"]
# Define test data
resume_file_path = r"/Users/omkarkale/Desktop/CV/1 col/Omkar Kale New.pdf"  # Absolute file path for the resume
test_data = {
    "resumator-firstname-value": "Omkar",
    "resumator-lastname-value": "Kale",
    "resumator-email-value": "omkar@axonator.com",
    "resumator-phone-value": "8329951114",
    "resumator-address-value": "17, A2, Sinhagad PMAY Society",
    "resumator-city-value": "Pune",
    "resumator-state-value": "Maharashtra",
    "resumator-postal-value": "411041",      
    "resumator-relocate-value": "Yes",#dropdown
    "resumator-linkedin-value": "https://www.linkedin.com/in/omkark911/",
    "resumator-salary-value": "12 LPA",
    "resumator-start-value": "2025-02-28", #calender selector
    "resumator-felony-value": "No",
    "resumator-wmyu-value": "This form is automatically filled using a Python script with Selenium. GitHub: https://github.com/omkark911/wonderBotz-Submit-Form-Automation",
    "resumator-questionnaire-q731494": "30-60 days", # dropdown
}

def init_driver(browser_name):
    """Initialize WebDriver for the specified browser."""
    if browser_name == "chrome":
        # Set up Selenium and the web driver
        service = Service(ChromeDriverManager().install())
        options = webdriver.ChromeOptions()
        options.add_argument('--start-maximized')  # Maximize the browser window
        driver = webdriver.Chrome(service=service, options=options)
    elif browser_name == "firefox":
        driver = webdriver.Firefox()
    elif browser_name == "edge":
        driver = webdriver.Edge()
    else:
        raise ValueError(f"Unsupported browser: {browser_name}")

    driver.maximize_window()
    return driver

def upload_resume(driver, wait, resume_file_path):
    """Click on 'Attach Resume' and upload a file."""
    try:
        # Click the 'Attach Resume' button
        attach_resume_button = wait.until(EC.element_to_be_clickable((By.ID, "resumator-choose-upload")))
        attach_resume_button.click()
        time.sleep(2)  # Allow time for the file input to appear, if necessary
        
        # Upload the file
        file_input = wait.until(EC.presence_of_element_located((By.ID, "resumator-resume-value")))
        file_input.send_keys(resume_file_path)
        
        print("Resume uploaded successfully!")
        return True
    except Exception as e:
        print(f"Error during file upload: {e}")
        return False

def fill_form(driver, wait, test_data):
    formResults = False
    try:
        for field_id, value in test_data.items():
            try:
                element = driver.find_element(By.ID, field_id)
                
                # Handle dropdowns
                if element.tag_name == "select":
                    select = Select(element)
                    select.select_by_visible_text(value)
                
                # Handle calendar fields
                elif field_id in ["resumator-start-value"]:  # Adjust based on your field IDs
                    element.click()  # Open the calendar popup
                    element.send_keys(value)
                    driver.find_element(By.ID, "resumator-salary-value").click()
                
                # Handle regular input fields
                else:
                    element.clear()
                    element.send_keys(value)

                time.sleep(1)
            except Exception as e:
                print(f"Error filling field {field_id}: {e}")
        
        upload_result = upload_resume(driver, wait, resume_file_path)

        captcha = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="resumator-recaptcha-field"]/div')))
        driver.execute_script("arguments[0].scrollIntoView(true);", captcha)
        captcha.click()
        time.sleep(30)# added 30 secs delay to check the captcha

        submit_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="resumator-submit"]')))
        driver.execute_script("arguments[0].scrollIntoView(true);", submit_button)
        submit_button.click()
        
        error_messages = driver.find_elements(By.XPATH, "//div[contains(@class, 'error-message')]")
        error_texts = [error.text for error in error_messages]
    except Exception as e:
        return formResults, None, [f"Error: {e}"]

    return formResults, error_texts

# Loop through each browser
for browser in browsers:
    try:
        driver = init_driver(browser)
        driver.get("https://wonderbotz.applytojob.com/apply/lQXRHUAIQ5/Automation-Anywhere-Developer")
        wait = WebDriverWait(driver, 10)

        formResults, error_texts = fill_form(driver, wait, test_data)
        
        driver.quit()
    except Exception as e:
        if driver:
            driver.quit()

