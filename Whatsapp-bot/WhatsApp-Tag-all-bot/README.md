# 📢 Tag-All Bot

Automate the process of tagging all members of a WhatsApp group using this Python script. This script utilizes the Selenium library to send a message to all members of a group at once.

## 🚀 Installation

1. Ensure you have Python installed on your system.
2. Clone this repository or download the provided code:

    ```bash
    git clone https://github.com/anupammaurya6767/Botzy.git
    ```

3. Navigate to the project directory:

    ```bash
    cd Botzy/WhatsApp-Tag-All-Bot
    ```
4. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```
5. Download the [ChromeDriver](https://chromedriver.chromium.org/downloads) suitable for your Chrome version and place it in the project directory.

## 📋 Usage

1. Make sure you have a compatible version of Chrome installed on your system.
2. Run the script:

    ```bash
    python tagall.py
    ```
3. A Chrome browser window will open, displaying WhatsApp Web.
4. Scan the QR code using your phone to log in to WhatsApp Web.
5. After successful login, the script will wait for 10 seconds to load the page.
6. Provide the name of the group you want to send the message to by modifying the `group_name` variable in the `tagall.py` file.
7. Run the script again.

## 📝 Notes

- This script uses the Chrome WebDriver for Selenium automation. Ensure that the `chromedriver` executable matches your Chrome browser version and is located in the project directory.
- The script waits for 10 seconds to ensure proper loading of the WhatsApp Web page before interaction. You can modify this delay if necessary.
- The provided code sends the message "@everyone" to the specified group. Modify the `message_box.send_keys()` line in the `tagall.py` file to change the message content.
