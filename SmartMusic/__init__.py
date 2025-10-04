from SmartMusic.core.bot import Hotty
from SmartMusic.core.dir import dirr
from SmartMusic.core.git import git
from SmartMusic.core.userbot import Userbot
from SmartMusic.misc import dbb, heroku

from SafoneAPI import SafoneAPI
from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = Hotty()
userbot = Userbot()
api = SafoneAPI()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()

APP = "HungamaMusiccRobot"  # connect music api key "Dont change it"
