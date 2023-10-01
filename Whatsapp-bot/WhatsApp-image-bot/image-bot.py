from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from bs4 import BeautifulSoup

def get_contact_info(driver, person):
    try:
        # Wait for the user to scan the QR code manually for 60 seconds
        input("Scan the QR code manually and press Enter after scanning...")

        # XPath for the search input field
        inp_xpath_search = "//p[@class='selectable-text copyable-text iq0m558w g0rxnol2']"
        search_input = driver.find_element(By.XPATH, inp_xpath_search)

        # Set the value and trigger events
        search_input.clear()
        search_input.send_keys(person)
        search_input.send_keys(Keys.RETURN)
        time.sleep(5)

        # Click on the user profile
        profile = driver.find_element(By.XPATH, "//div[@class='_2au8k']")
        profile.click()
        time.sleep(10)

        # Get the page source and parse it using BeautifulSoup
        html = driver.page_source
        soup = BeautifulSoup(html, "html.parser")

        # Find the container element
        container = soup.find("div", {"class": "lhggkp7q qq0sjtgm ebjesfe0 jxacihee tkdu00h0"})

        # Find and print the user's name
        name = container.find("h2")
        if name:
            print("User's Name:", name.text)
        else:
            print("User's Name not found.")

        # Find and print the user's number
        number = container.find("div", {"class": "a4ywakfo qt60bha0"})
        if number:
            print("User's Number:", number.text)
        else:
            print("User's Number not found.")

        # Find and print the top groups the user is in, if any
        groups = container.find("div", {"class": "_3YS_f _2A1R8"})
        if groups:
            print("Top Groups:")
            group = [item.text for item in groups.find_all("div", {"class": "y_sn4"})]
            print(group)
        else:
            print("No groups in common.")

        # Find and print any common interests or details
        about = container.find("span", {"class": "cw3vfol9 _11JPr selectable-text copyable-text"})
        if about:
            print("About:", about.text)
        else:
            print("About not found.")

    except Exception as e:
        print("Exception Occurred:", str(e))

def main():
    try:
        # Initialize the Chrome WebDriver
        driver = webdriver.Chrome()

        # Open the WhatsApp Web URL
        driver.get("https://web.whatsapp.com/")

        print("Enter name of person")
        person = input()
        time.sleep(2)

        get_contact_info(driver, person)

    except Exception as e:
        print("Exception Occurred:", str(e))
    finally:
        # Close the WebDriver
        driver.quit()

if __name__ == "__main__":
    main()
