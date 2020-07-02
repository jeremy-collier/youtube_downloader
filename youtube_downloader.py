from pytube import YouTube

#Set's the path where the video will be saved to.
SAVE_PATH = "C:\\Users\\perpl\\Videos"

#Allows for a prompt to get the video URL and set a filename
link = input('Paste the video URL from YouTube: ')
new_filename = input("What do you want to name the file? ")

#If the URL is invalid, or if there is any other error, it'll let the user know
try:
    yt = YouTube(link)
except:
    print("Connection Error, please check your url format and try again.")

print('\nHere are the available formats.\n')

#Get only mp4 files and prints them in a format easily readable
#Then allows the user to select which format they want by using the itag
video_formats = yt.streams.filter(file_extension = "mp4")
for item in video_formats:
    print(item)
chosen_itag = int(input("\nSelect the video format you want to download by typing in the itag: "))

#Downloads the video, or gives an error letting the user know it was not successful
try:
    yt.streams.get_by_itag(chosen_itag).download(SAVE_PATH, filename = new_filename)
    print('Video has been downloaded successfully')
except:
    print('Sorry, there was an error, please try again.')
