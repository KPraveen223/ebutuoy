# ebutuoy
YouTube Channel and Video Analytics

This repository contains Python scripts to retrieve and analyze data from YouTube channels and their videos using the YouTube Data API v3.

## Overview
The scripts provided here utilize the YouTube Data API v3 to fetch channel statistics, video details, and other relevant information. The data fetched includes:

- Channel Statistics:
  - Subscribers
  - Total Views
  - Total Videos

- Video Details:
  - Title
  - Description
  - Published Date
  - Views
  - Likes
  - Favorites
  - Comments
  - Duration

## Prerequisites
Before using the scripts, ensure you have:
- Python 3.x installed.
- Necessary Python libraries (`google-api-python-client`, `pandas`).

## Getting Started
1. Obtain YouTube API Key:
   - Generate a YouTube Data API key from the [Google Developers Console](https://console.developers.google.com/).
2. Set Up:
   - Replace `#Insert your API Key here` with your YouTube API key in the script.
3. Installation:
   - Install the required Python packages:
 	```bash
 	pip install google-api-python-client pandas
 	```
4. Usage:
   - Modify `channel_ids` list with the desired channel IDs.
   - Run the script to fetch channel statistics and video details.

## Files
- `youtube_analytics.py`: Python script to fetch channel statistics and video details.
- **`#insert_file_name.xlsx`**: Excel file containing fetched video details.

## Notes
- The script fetches video details from the "uploads" playlist of the specified channel. Ensure the playlist ID is correctly assigned to `Playlist_id`.
- Pagination is handled automatically for fetching all videos in a playlist.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments
- This project was created to demonstrate using the YouTube Data API v3 for fetching channel and video data.
Make sure to replace `#insert_file_name.xlsx` with the actual filename used in your script for saving the Excel file. Adjust any placeholders (`#Insert your API Key here`, `#Insert_Channel_ID`, etc.) with actual values as applicable.
