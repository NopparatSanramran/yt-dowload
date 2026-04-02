import yt_dlp
import questionary

# screen - application
def screen():
    youtube_url = questionary.text("youtube url").ask()    
    option = questionary.select(
        "type",
        choices=[
            "mp3",
            "mp4",
            "wav"
        ],
        pointer="-"
    ).ask()
    dowloads(youtube_url, option)

# system dowload
def dowloads(youtube_url, format_type):

    ydl_opts = {
        'outtmpl': '%(title)s.%(ext)s',
        'ffmpeg_location': './ffmpeg/ffmpeg.exe',
    }

    if format_type == "mp3" :
        ydl_opts.update({
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '320',
            }],
        })
    elif format_type == "wav" :
        ydl_opts.update({
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'wav',
            }],
        })
    elif format_type == "mp4" :
        ydl_opts.update({
            'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
            'postprocessors': [{
                'key': 'FFmpegVideoConvertor',
                'preferedformat': 'mp4',
            }]
        })
    else :
        print("invalid type")
    with yt_dlp.YoutubeDL(ydl_opts) as ydl :
        ydl.download(youtube_url)

screen()