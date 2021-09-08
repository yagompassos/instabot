import instaloader
from instaloader.structures import Profile
from credentials import username, password


L = instaloader.Instaloader()

senha = input('Digite a senha: ')
L.login(username, senha)

profile = Profile.from_username(L.context, username)


file = open("seguidores.txt","a+")

for follower in profile.get_followers():
    file.write(follower.username+"\n")
    print(follower.username)
    
#file.write(count)
#print(count)
file.close()


file = open("seguindo.txt","a+")

for followee in profile.get_followees():
    file.write(followee.username+"\n")
    print(followee.username)
    
#file.write(count)
#print(count)
file.close()