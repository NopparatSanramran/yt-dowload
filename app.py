import yt_dlp
import questionary

def screen():
    option = questionary.select(
        "type",
        choices=[
            "mp3",
            "mp4",
            "wav"
        ],
        pointer="-"
    ).ask()


screen()