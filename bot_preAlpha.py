# -*- coding: utf-8 -*-
# author: Eduardo Apaza y Diego Fernández
# Version: Pre-alpha 
# link: https://github.com/drums71ck/BotTelegramSpotify.git
from http import client
from multiprocessing import context
from unittest import result
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import sys
from pprint import pprint
from telegram.ext import (Updater, CommandHandler)

client_id = "766b6ab76dbc438e8055498cf29f246b"
client_secret ="705f489444d74a478589a453024f50c8"


def start(update, context):
	''' START '''
	# Enviar un mensaje a un ID determinado.
	context.bot.send_message(update.message.chat_id, "Bienvenido a listenBot")
	
	
	if len(sys.argv) > 1:
		urn=sys.argv[1]
	else:
		urn ='spotify:album:7L6gLnSJBTU0tOneX0Ol91'
	
	sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials (client_id,client_secret))
	album = sp.album(urn)
	song = result["tracks"]["items"]
	print(album)
	

	
	

def main():
	TOKEN="5681916450:AAEaLRcvNbApeDLfTLlW4YDqXVW5Fua43ms"
	updater=Updater(TOKEN, use_context=True)
	dp=updater.dispatcher

	# Eventos que activarán nuestro bot.
	dp.add_handler(CommandHandler('start',	start))

	# Comienza el bot
	updater.start_polling()
	# Lo deja a la escucha. Evita que se detenga.
	updater.idle()

if __name__ == '__main__':
	main()
