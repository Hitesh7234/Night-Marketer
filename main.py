from moviepy import VideoFileClip, TextClip, CompositeVideoClip, AudioFileClip
import os

# Paths to assets
input_folder = "Videos"
output_folder = "OutputFolder"
background_music_path = "background_music.mp3"

# Define motivational quote and settings
motivational_quote = "Believe in yourself and all that you are."
font_size = 50
text_color = "white"
text_position = "center"

# Fallback to find a valid font dynamically
def get_font_path():
    """Returns a valid font path on the system."""
    try:
        import matplotlib
        font_path = matplotlib.font_manager.findfont("Arial")
        print(f"Font found: {font_path}")
        return font_path
    except Exception as e:
        print(f"Could not find the font dynamically. Error: {e}")
        return None

# Use Arial font or fallback
font_path = "C:/Windows/Fonts/arial.ttf"

# Function to adjust video aspect ratio to 9:16
def adjust_aspect_ratio(video_clip):
    # Get the original dimensions of the video
    width, height = video_clip.size
    
    # Define the target 9:16 aspect ratio size (height > width)
    target_height = height
    target_width = int(target_height * 9 / 16)

    # Resize or pad the video to fit the 9:16 aspect ratio
    if width / height > 9 / 16:  # Video is too wide, so crop the width
        new_width = int(height * 9 / 16)
        video_clip = video_clip.cropped(x1=(width - new_width) // 2, x2=(width + new_width) // 2)
    else:  # Video is too tall, so pad the height
        new_height = int(width * 16 / 9)
        video_clip = video_clip.resized(height=new_height).crop(y1=(new_height - target_height) // 2, y2=(new_height + target_height) // 2)

    return video_clip

def edit_video(video_path, motivational_quote, background_music_path, output_path):
    # Load the original video
    video_clip = VideoFileClip(video_path)

    # Adjust the video to maintain a 9:16 aspect ratio
    video_clip = adjust_aspect_ratio(video_clip)

    # Add the motivational quote as a text overlay
    try:
        text_clip = TextClip(
            text = motivational_quote,
            font_size=font_size,
            color=text_color,
            font=font_path,
            size=video_clip.size,
            method="caption",
        ).with_position(text_position).with_duration(video_clip.duration)
    except Exception as e:
        print(f"Font issue: {e}. Using default text settings.")
        text_clip = TextClip(
            text = motivational_quote,
            font = "C:/Windows/Fonts/arial.ttf",
            font_size=font_size,
            color=text_color,
            size=video_clip.size,
            method="caption",
        ).with_position(text_position).with_duration(video_clip.duration)

    # Combine the video with the text overlay
    edited_clip = CompositeVideoClip([video_clip, text_clip])

    # Add background music if provided
    if background_music_path:
        audio_clip = AudioFileClip(background_music_path).subclipped(0, video_clip.duration)
        edited_clip = edited_clip.with_audio(audio_clip)

    # Export the edited video
    edited_clip.write_videofile(output_path, fps=24, codec="libx264", audio_codec="aac")
    print(f"Video saved at {output_path}")

# Create the output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Loop through all video files in the input folder and process them
for video_filename in os.listdir(input_folder):
    video_path = os.path.join(input_folder, video_filename)
    if video_filename.lower().endswith(('.mp4', '.avi', '.mov')):  # Process video files
        output_video_path = os.path.join(output_folder, f"edited_{video_filename}")
        print(f"Processing {video_filename}...")
        edit_video(video_path, motivational_quote, background_music_path, output_video_path)
        print(f"Processed video saved to {output_video_path}")
