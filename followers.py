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
    #seguidoresList.append(follower)
    #countW += 1
file.close()


file = open("seguindo.txt","a+")

for followee in profile.get_followees():
    file.write(followee.username+"\n")
    #seguindoList.append(followee)
    #countE += 1
file.close()