import requests
import os

# Pixabay API configuration
API_KEY = ""  # Replace with your Pixabay API key
BASE_URL = "https://pixabay.com/api/videos/"
DOWNLOAD_FOLDER = "Videos"

# Ensure the download folder exists
os.makedirs(DOWNLOAD_FOLDER, exist_ok=True)

def fetch_videos(query, max_results=5):
    """
    Fetch videos from Pixabay API based on a query.
    :param query: The search term for videos
    :param max_results: Maximum number of videos to fetch
    """
    # Define API parameters
    params = {
        "key": API_KEY,
        "q": query,
        "video_type": "all",  # Options: 'all', 'film', 'animation'
        "per_page": max_results,
    }
    
    # Make a GET request to Pixabay API
    response = requests.get(BASE_URL, params=params)
    
    if response.status_code == 200:
        data = response.json()
        videos = data.get("hits", [])
        
        if videos:
            print(f"Found {len(videos)} videos for '{query}'. Downloading...")
            for idx, video in enumerate(videos):
                video_url = video["videos"]["medium"]["url"]
                video_id = video["id"]
                download_video(video_url, f"video_{idx + 1}.mp4")
        else:
            print(f"No videos found for query: {query}")
    else:
        print(f"Error fetching videos: {response.status_code}, {response.text}")

def download_video(url, filename):
    """
    Download video from a given URL.
    :param url: The video URL
    :param filename: The filename to save the video
    """
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        filepath = os.path.join(DOWNLOAD_FOLDER, filename)
        with open(filepath, "wb") as file:
            for chunk in response.iter_content(chunk_size=1024):
                file.write(chunk)
        print(f"Downloaded: {filepath}")
    else:
        print(f"Failed to download video from {url}")

# Example usage
if __name__ == "__main__":
    search_query = "nature"  # Replace with your desired search term
    fetch_videos(search_query, max_results=3)
