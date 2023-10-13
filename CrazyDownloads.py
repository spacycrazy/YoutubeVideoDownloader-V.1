import os
from pytube import YouTube

# Function to download a video
def download_video(url, download_as_mp3, file_name, download_directory):
    try:
        # Create a YouTube object
        yt = YouTube(url)

        # Ask for confirmation
        confirm = input(f"Do you want to download '{yt.title}'? (yes/no): ")
        if confirm.lower() != 'yes':
            print("Download canceled.")
            return

        # Choose the stream (MP3 or MP4)
        if download_as_mp3:
            stream = yt.streams.filter(only_audio=True).first()
        else:
            stream = yt.streams.filter(progressive=True, file_extension='mp4').first()

        # Download the video to the specified directory
        stream.download(output_path=download_directory, filename=file_name)

        print("Download completed!")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Prompt for video URL
    video_url = input("Enter the video URL: ")

    # Ask for MP3 or MP4
    download_as_mp3 = input("Download as an MP3? (yes/no): ").lower() == 'yes'

    # Ask for file name
    file_name = input("Enter the file name with extension that you desire: ")
    file_name = f"CRAZYDOWNLOADS - {file_name}"

    # Specify the download directory
    download_directory = r'D:\'  # Change this to your desired directory

    # Create the download directory if it doesn't exist
    if not os.path.exists(download_directory):
        os.makedirs(download_directory)

    # Call the download function
    download_video(video_url, download_as_mp3, file_name, download_directory)
