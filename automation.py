import time
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Set up the Chrome driver
service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

# Open WhatsApp Web
driver.get('https://web.whatsapp.com')

# Wait for the QR code scan to complete
print("Scan the QR code and press Enter when ready...")
input("Press Enter after scanning the QR code")

# Wait for WhatsApp Web to load
time.sleep(2)
print("Automate Start")

# Define the target contact/group and the message
target = '8510094805'  # Update with your target contact number
message = '''Hello, this is an automated message from Hitesh Singh regarding the data analyst internship opportunity that I came across on Indeed. Here is the link to my assignment, along with two automated videos.
You can find the complete code and details in the following GitHub repository: 
Feel free to explore the project!'''
output_folder = 'OutputFolder'  # Folder containing the edited videos

# Find the chat using the contact name or group name
search_box = driver.find_element(By.XPATH, '//*[@id="side"]/div[1]/div/div[2]/div[2]/div/div/p')
search_box.send_keys(target)
search_box.send_keys(Keys.ENTER)

# Wait for the chat to load
# time.sleep(2)

# Send the message
message_box = driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span/div/div[2]/div[1]/div[2]/div[1]/p')
message_box.send_keys(message)
message_box.send_keys(Keys.ENTER)

    # Loop through all files in the "Edited_Videos" folder
for video_filename in os.listdir(output_folder):
     if video_filename.endswith(".mp4"):
        # Full path to the video
        video_path = os.path.join(output_folder, video_filename)
        video_path =f'C:\\Users\\pc\\Desktop\\Techosto\\night marketer\\{video_path}'
        # Attach the video
        attachment_button = driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span/div/div[1]/div/button/span')
        attachment_button.click()   

        # Wait for the media options to appear
        time.sleep(2)
                
        # Click on the 'Camera' option to upload a video
        video_button = driver.find_element(By.XPATH, '//*[@id="app"]/div/span[5]/div/ul/div/div/div[2]/li/div/input')
        video_button.send_keys(video_path)

        # Wait for the video to upload and then send it
        time.sleep(2)
        send_button = driver.find_element(By.XPATH, '//*[@id="app"]/div/div[3]/div/div[2]/div[2]/span/div/div/div/div[2]/div/div[2]/div[2]/div/div')
        send_button.click()

        # Wait a few seconds to ensure the video is sent
        time.sleep(5)


# Close the browser after sending all videos
driver.quit()
