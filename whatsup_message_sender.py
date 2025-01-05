from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import csv

# Path to your Chrome WebDriver. Download from https://sites.google.com/a/chromium.org/chromedriver/downloads
webdriver_path = '/path/to/chromedriver'

# Function to send message to WhatsApp number
def send_whatsapp_message(number, message):
    # Initialize Chrome WebDriver
    driver = webdriver.Chrome(webdriver_path)
    driver.get('https://web.whatsapp.com/')
    
    # Wait for user to scan the QR code manually
    input("Scan the QR code and then press Enter to continue...")
    
    # Locate the chat search input
    search_box = driver.find_element_by_xpath('//div[@contenteditable="true"][@data-tab="3"]')
    ś
    # Type the number to search for
    search_box.send_keys(number + Keys.RETURN)
    
    time.sleep(2)  # Wait for the chat to load
    
    # Locate the input field for typing message
    input_box = driver.find_element_by_xpath('//div[@contenteditable="true"][@data-tab="1"][@spellcheck="true"]')
    
    # Type the message
    input_box.send_keys(message + Keys.RETURN)
    
    time.sleep(2)  # Wait for message to be sent
    
    # Close the browser
    driver.quit()

# Read numbers and messages from CSV file
with open('numbers.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)  # Skip header row if exists
    for row in reader:
        number = row[0]  # Assuming the number is in the first column
        message = "Hello, !"
        send_whatsapp_message(number, message)
