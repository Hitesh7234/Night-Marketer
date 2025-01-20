# Night-Marketer
t Marketer is an automated solution for downloading videos, editing them with motivational quotes, and sharing them via WhatsApp. The project combines video processing, API integration, and browser automation to streamline repetitive tasks.

---

## Table of ContentsNight Marketer

Nigh

1. [Features](#features)
2. [Requirements](#requirements)
3. [Installation](#installation)
4. [Usage](#usage)
   - [Video Downloading](#video-downloading)
   - [Video Editing](#video-editing)
   - [Automated WhatsApp Messaging](#automated-whatsapp-messaging)
5. [Configuration](#configuration)
6. [License](#license)

---

## Features

- **Download Videos**: Fetch videos from Pixabay using an API.
- **Edit Videos**: Add motivational quotes and background music while adjusting aspect ratios for optimal viewing.
- **Automated Messaging**: Send the edited videos via WhatsApp using Selenium automation.

---

## Requirements

- Python 3.7+
- Required Python packages (see `requirements.txt`):
  - moviepy
  - selenium
  - requests
  - matplotlib (optional for font detection)
- Chrome browser and Chromedriver

---

## Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/Hitesh7234/Night-Marketer.git
   cd Night-Marketer
   ```

2. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

3. **Download Chromedriver**:
   Ensure that Chromedriver matches your Chrome version. You can download it [here](https://chromedriver.chromium.org/downloads).

4. **Set up Pixabay API**:

   - Obtain an API key from [Pixabay](https://pixabay.com/api/docs/).
   - Add the API key to the `API_KEY` variable in the script.

---

## Usage

### Video Downloading

Fetch videos based on a keyword:

```bash
python fetch_videos.py
```

1. Edit the `search_query` variable in the script to specify the keyword (e.g., "nature").
2. Run the script to download videos to the `Videos` folder.

### Video Editing

Edit downloaded videos by adding motivational quotes and background music:

```bash
python edit_videos.py
```

1. Place the background music file as `background_music.mp3` in the root folder.
2. The edited videos will be saved to the `OutputFolder` directory.

### Automated WhatsApp Messaging

Send edited videos via WhatsApp:

```bash
python whatsapp_automation.py
```

1. Run the script and scan the QR code for WhatsApp Web.
2. Configure the `target` variable with the recipient's phone number.
3. Videos from `OutputFolder` will be sent automatically.

---

## Configuration

### Fonts

The script uses the Arial font by default. If unavailable, it attempts to find a valid font dynamically using Matplotlib.

### Video Aspect Ratio

The videos are adjusted to a 9:16 aspect ratio for compatibility with mobile viewing.

### WhatsApp Automation

Update the `target` variable with the recipient’s number and ensure the `OutputFolder` contains the videos to be sent.
---

## Notes

- Ensure your system’s Chrome browser is updated to match the Chromedriver version.
- Video editing may require additional codecs for `moviepy`. Install `ffmpeg` if needed.
- The WhatsApp Web script relies on stable internet and may need adjustments for new WhatsApp Web updates.

---

For questions or contributions, please contact [Hitesh7234](https://github.com/Hitesh7234).

