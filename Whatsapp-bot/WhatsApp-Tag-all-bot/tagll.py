from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time

def main():
    try:
        # Initialize the WebDriver
        driver = webdriver.Chrome()

        # Open WhatsApp Web
        driver.get("https://web.whatsapp.com/")

        # Wait for the user to scan the QR code manually for 10 seconds
        input("Scan the QR code manually and press Enter after scanning...")

        # Find the group name element
        group_name = find_element_with_retry(
            driver, "//span[@title='Group Name']"
        )  # Replace 'Group Name' with the name of the group you want to tag

        if group_name:
            group_name.click()

            # Find the message box
            message_box = find_element_with_retry(
                driver, "//div[@class='_2S1VP copyable-text selectable-text']"
            )

            if message_box:
                message_box.click()

                # Type the message
                message_box.send_keys("@everyone")

                # Send the message
                send_button = find_element_with_retry(
                    driver, "//button[@class='_35EW6']"
                )

                if send_button:
                    send_button.click()
                    print("Message sent successfully.")
                else:
                    print("Send button not found.")
            else:
                print("Message box not found.")
        else:
            print("Group not found.")

    except Exception as e:
        print("An error occurred:", str(e))
    finally:
        # Close the browser
        driver.quit()

def find_element_with_retry(driver, xpath, max_attempts=3):
    attempts = 0
    while attempts < max_attempts:
        try:
            element = driver.find_element_by_xpath(xpath)
            return element
        except NoSuchElementException:
            attempts += 1
            time.sleep(2)  # Wait for 2 seconds before retrying
    return None

if __name__ == "__main__":
    main()
