#Importing the necessary libraries
from googleapiclient.discovery import build
import pandas as pd

#YouTube API key
api_key = '#Insert your API Key here'

#List of Channel IDs
channel_ids = ['#Insert_Channel_ID'] #ChannelName

#creating the youtube service
youtube = build('youtube', 'v3', developerKey=api_key)

#Function to get channel statistics
def get_channel_stats(youtube, channel_ids):
    alldata=[]
    request = youtube.channels().list(
        part='snippet,contentDetails,statistics',
        id=','.join(channel_ids)
    )
    response = request.execute()

    for i in range(len(response['items'])):
        data = dict(Channel_name = response['items'][i]['snippet']['title'],
                Subscribers = response['items'][i]['statistics']['subscriberCount'],
                Views = response['items'][i]['statistics']['viewCount'],
                TotalVideos = response['items'][i]['statistics']['videoCount'],
                Playlist_id = response['items'][i]['contentDetails']['relatedPlaylists']['uploads']
                )
        alldata.append(data)
    return alldata

#Getting Channel statistics
channel_statistics = get_channel_stats(youtube, channel_ids)
channel_data = pd.DataFrame(channel_statistics)

#Converting data types
channel_data['Subscribers'] = pd.to_numeric(channel_data['Subscribers'])
channel_data['Views'] = pd.to_numeric(channel_data['Views'])
channel_data['TotalVideos'] = pd.to_numeric(channel_data['TotalVideos'])

#Getting playlist IDs for a specific channel
Playlist_id = channel_data.loc[channel_data['Channel_name']=='#insert_channel_name', 'Playlist_id'].iloc[0]

# Function to get video IDs
def get_video_ids(youtube, playlist_id):
    video_ids = []

    request = youtube.playlistItems().list(
        part='contentDetails,snippet,status',
        playlistId=playlist_id,
        maxResults=50
    )
    response = request.execute()

    while 'items' in response:
        for item in response['items']:
            video_ids.append(item['contentDetails']['videoId'])

        if 'nextPageToken' in response:
            request = youtube.playlistItems().list(
                part='contentDetails,snippet,status',
                playlistId=playlist_id,
                maxResults=50,
                pageToken=response['nextPageToken']
            )
            response = request.execute()
        else:
            break

    return video_ids

video_ids = get_video_ids(youtube, Playlist_id)

# Function to get video details
def get_video_details(youtube, video_ids):
    all_video_stats = []

    for i in range(0, len(video_ids), 50):
        request = youtube.videos().list(
            part='snippet,statistics,contentDetails',
            id=','.join(video_ids[i:i+50])
        )
        response = request.execute()

        for video in response['items']:
            video_stats = dict(
                Video_URL=f'https://www.youtube.com/watch?v={video["id"]}',
                Title=video['snippet']['title'],
                Description=video['snippet']['description'],
                Keywords=video['snippet'].get('tags', []),
                Published_date=video['snippet']['publishedAt'],
                Views=video['statistics']['viewCount'],
                Likes=video['statistics'].get('likeCount', 0),
                Favourites=video['statistics']['favoriteCount'],
                Comments=video['statistics'].get('commentCount', 0),
                Duration=video['contentDetails']['duration'],
            )

            duration = video_stats['Duration']
            duration = duration.replace('PT', '').lower()
            video_stats['Duration'] = duration

            all_video_stats.append(video_stats)

    return all_video_stats

#Getting video details
video_details = get_video_details(youtube, video_ids)
video_data = pd.DataFrame(video_details)

#Converting data types
video_data['Likes'] = pd.to_numeric(video_data['Likes'])
video_data['Comments'] = pd.to_numeric(video_data['Comments'])
video_data['Views'] = pd.to_numeric(video_data['Views'])
video_data['Favourites'] = pd.to_numeric(video_data['Favourites'])

#Saving data to an excel file
video_data.to_excel("#insert_file_name.xlsx")