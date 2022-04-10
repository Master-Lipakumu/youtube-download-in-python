import pafy
""" Master Lipakumu crée un téléchargeur des videos
  et audios sur youtube très facilement """
# importer pafy 

#fonction des details de la video a télécharger
def getMetaData(video):

    print("voici les detailes de votre video")

    print("Titre : ", video.title)

    print(f"total vues : {video.viewcount} | temps : {video.length} seconds")

    print(f"longueur de la video {video.duration}| nombre de like: {video.likes}")

    print("nom de la chaine : " , video.author)

    print(f"nombre de je n'aime pas  : {video.dislikes}")


#fonction du téléchargement de la video sous format audio 
def download_as_video(video):
#recuperation des détails de la video
    getMetaData(video)
#verification de la video avec la methode getbest() de pafy
    best = video.getbest()
#affichage de la resolution et de l'extension de la variable best crée précedament
    print(f"video resolution: {best.resolution} \n video extension : {best.extension}")
#téléchargement de la video sous format video
    best.download()
# affiche video est télécharger  dès que tu finis
    print("video is downloaded")


#fonction de téléchargement de la video en format audio
def download_as_audio(video):
#recuperation des détails de la video
    getMetaData(video)
#verification du format audio de la video
    bestaudio = video.getbestaudio()
#affiche le tempo du fichier
    print(f"vibration audio {bestaudio.bitrate}")
#téléchargement de la video sous format audio 
    bestaudio.download()
#affiche video est télécharger en audio dès que tu finis
    print("video is downloaded in audio")


#structure conditionnel du programme 
if __name__ =="__main__":
#demande lui d'inserer une url de youtube
    url = input("inserer l'url de la video youtube que vous souhaitez telecharger svp \n :")
# creation de l'instance
    video = pafy.new(url)
#donnons le choix a notre utilisateur 
    choice = input("télécharger en tapant v pour video ! \n télécharger en tapant a pour audio \n :")
#si tu appuis sur v ou V tu aurras ta video en format video mp4
    if choice.upper() == "V" or choice.lower() == "v":

        download_as_video(video)
#si tu appuis sur a ou A tu aurras ta video sous format audio
    elif choice.upper() == "A" or choice.lower() == "a":

        download_as_audio(video)
# sinon le programme ne connais la touche saisie
    else:
        print('la touche que vous avez entrez n\'est pas valide')
