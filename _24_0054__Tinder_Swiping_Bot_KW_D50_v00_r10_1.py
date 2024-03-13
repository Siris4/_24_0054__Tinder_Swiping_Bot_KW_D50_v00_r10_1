from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager
import time
from datetime import datetime

# constants:
email = "YOUR_EMAIL"


def log_message(message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"\n{timestamp} - {message}")

def click_english_option(driver):
    try:
        # updated to use the provided css selector

        english_option = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#s1746112904 > main > div > div.Pb\\(12px\\).H\\(100\\%\\).Mah\\(800px\\)--ml.Ovy\\(s\\).Ovs\\(touch\\).Fx\\(\\$flx1\\) > ul > li:nth-child(1) > a > span:nth-child(1)")))
        english_option.click()

        # english_option = driver.find_element(By.CSS_SELECTOR, "#s1746112904 > main > div > div.Pb\\(12px\\).H\\(100\\%\\).Mah\\(800px\\)--ml.Ovy\\(s\\).Ovs\\(touch\\).Fx\\(\\$flx1\\) > ul > li:nth-child(1) > a > span:nth-child(1)")
        # english_option.click()
        log_message("selected english from the dropdown.")
    except NoSuchElementException:
        log_message("language option not found.")


def find_decline_button(driver):
    try:
        # First priority: Find by text content directly within a div
        buttons_by_text = driver.find_elements(By.XPATH, "//button[.//div[contains(text(), 'I decline')]]")
        if buttons_by_text:
            return buttons_by_text[0]  # Return the first matching element

        # Second priority: Find by a distinctive class in the button's structure
        buttons_by_class = driver.find_elements(By.CLASS_NAME, "l17p5q9z")
        if buttons_by_class:
            return buttons_by_class[0]

        # Third priority: Composite match based on class and data attributes
        buttons_by_composite = driver.find_elements(By.CSS_SELECTOR, "button.c1p6lbu0[data-size='medium'][type='button']")
        if buttons_by_composite:
            return buttons_by_composite[0]

        return None  # If no matching element found
    except NoSuchElementException:
        return None

# Initialize the webdriver
service = ChromeService(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
log_message("WebDriver initialized.")

# Navigate to Tinder's login page
driver.get("https://tinder.com/")
log_message("Navigated to Tinder's login page.")


while True:
    decline_button = find_decline_button(driver)
    if decline_button:
        decline_button.click()
        log_message("Decline button clicked.")
        break
    else:
        time.sleep(1)  # Wait a bit before trying again

try:
    log_in_button = driver.find_element(By.CLASS_NAME, 'l17p5q9z')
    log_in_button.click()
    log_message("Clicked on 'Log in' button successfully.")
except NoSuchElementException:
    log_message("Log in button not found, attempting alternative method.")
    try:
        login_button = driver.find_element(By.CSS_SELECTOR, "button.c1p6lbu0.W\\(80\\%\\).My\\(20px\\).Mx\\(a\\) div.l17p5q9z")
        login_button.click()
        log_message("Clicked on the alternative login button successfully.")
    except (NoSuchElementException, Exception) as e:
        log_message(f"An error occurred: {e}")

click_english_option(driver)  # Correctly call the function to click the English option


# try:
#     continue_with_google_spanish = driver.find_element(By.XPATH, "//span[contains(@class, 'nsm7Bb-HzV7m-LgbsSe-BPrWId') and contains(text(), 'Continuar con Google')]")
#     continue_with_google_spanish.click()
#     log_message("Clicked on 'Continuar con Google' button successfully.")
# except NoSuchElementException:
#     log_message("'Continuar con Google' button not found, attempting in English.")
#     try:
#         login_with_google_button = driver.find_element(By.XPATH, "//div[contains(text(), 'Continue with Google')]")
#         login_with_google_button.click()
#         log_message("Clicked on 'Continue with Google' button successfully.")
#     except (NoSuchElementException, Exception) as e:
#         log_message(f"An error occurred: {e}")

try:
    log_in_button = driver.find_element(By.CLASS_NAME, 'l17p5q9z')
    log_in_button.click()
    log_message("Clicked on 'Log in' button successfully.")
except NoSuchElementException:
    log_message("Log in button not found, attempting alternative method.")
    try:
        login_button = driver.find_element(By.CSS_SELECTOR, "button.c1p6lbu0.W\\(80\\%\\).My\\(20px\\).Mx\\(a\\) div.l17p5q9z")
        login_button.click()
        log_message("Clicked on the alternative login button successfully.")
    except (NoSuchElementException, Exception) as e:
        log_message(f"An error occurred: {e}")

input("Press Enter to exit...\n")

# Uncomment below to close the browser automatically.
# driver.quit()
