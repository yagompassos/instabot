import instaloader
from instaloader.structures import Profile
from credentials import username, password


L = instaloader.Instaloader()

L.login(username, password)

profile = Profile.from_username(L.context, username)

for followers in profile.get_followers():
    print(followers.username)