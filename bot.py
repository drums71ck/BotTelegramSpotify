# -*- coding: utf-8 -*-

from ast import arg
from asyncore import dispatcher
from cgitb import text
from codecs import charmap_build
from email.mime import audio
from gc import callbacks
from http import client
from lib2to3.pgen2 import token
from multiprocessing import context
from nturl2path import url2pathname
from time import sleep
from tkinter import Button
from turtle import onclick
from unittest import result
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import sys
from tkinter.tix import ButtonBox
from time import sleep
import pyautogui

from pprint import pprint
from telegram.ext import (Updater, CommandHandler)
from telegram import InlineKeyboardMarkup, InlineKeyboardButton, Voice # Necesario para bfrom telebot.types import InlineKeyboardMarkup, InlineKeyboardButtonotones


client_id = "766b6ab76dbc438e8055498cf29f246b"
client_secret ="705f489444d74a478589a453024f50c8"

import webbrowser # for make a link
sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials (client_id,client_secret))
def start(update, context):
	''' START '''
	# Enviar un mensaje a un ID determinado.
	context.bot.send_message(update.message.chat_id, "Bienvenido a ListeBot")
	context.bot.send_message(update.message.chat_id, "Soy un bot que te mostrara lista de lo mas escuchado en Spotify")
	context.bot.send_message(update.message.chat_id, "Si quieres escuchar los 30 segundos de la cancion mas escuchada  de cada lista inserta: ")
	context.bot.send_message(update.message.chat_id, "/comands mes, /comands hoy, /comands mejor")
	context.bot.send_message(update.message.chat_id, "Que quieres buscar?\n-/track\n-/artist\n-/album\n-/playlist")
	
	#-------------------------------------------------------------------
	
		
	
	
	
	# all_pairs = list(album.items())
	
	# context.bot.send_message(update.message.chat_id, album['external_urls']['spotify'])
	# webbrowser.open(album['uri'])
	#print(album)
    
	# botones--------------------------------------------------------
	Button1 = InlineKeyboardButton (
		text = 'Lo mejor del mes',
		url = 'https://open.spotify.com/playlist/37i9dQZF1DWZoF06RIo9el?si=97d7d3b264b34114',
		callback_data = '1'

	)
	Button2 = InlineKeyboardButton (
		text = 'Top Mundial',
		url = 'https://open.spotify.com/playlist/37i9dQZEVXbMDoHDwVN2tF?si=5d179803be4449b4',
		
	)
	Button3 = InlineKeyboardButton (
		text = 'Hits del momento',
		url = 'https://open.spotify.com/playlist/37i9dQZF1DXcBWIGoYBM5M?si=18e57129af6342f6',
		callback_data = '3'	
	)
	
	update.message.reply_text ( # elegir al usuario
		text = '¿Que quieres escuchar hoy?',
		reply_markup=InlineKeyboardMarkup([
			[Button1, Button2, Button3]
			])

	)


	#----------------------------------------------------------------

def comands(update , context):
	args = context.args
	chat_id = update.message.chat_id
	
		
	
	if(len(args) > 0):
		if(args[0].lower() == "mes"):
			msg = '30 Segundos de las canciones del mes'
			for track in sp.playlist_tracks("spotify:playlist:37i9dQZF1DWZoF06RIo9el")["items"][:2]:
				#Track name
				
				track_name = track["track"]["name"]
				track_audio = track["track"]["preview_url"]

				track_pop = track["track"]["popularity"]
				
				print(track_pop," ",track_name)
	
				
		
		if(args[0].lower() == "hoy"):
			msg = '30 Segundos de los hits del momento'
			for track in sp.playlist_tracks("spotify:playlist:37i9dQZF1DXcBWIGoYBM5M")["items"][:2]:
				#Track name
				
				track_name = track["track"]["name"]
				track_audio = track["track"]["preview_url"]

				track_pop = track["track"]["popularity"]
				
				print(track_pop," ",track_name)
	
				
			
		if(args[0].lower() == "mejor"):
			msg = '30 Segundos de las canciones de lo mejor'
			for track in sp.playlist_tracks("spotify:playlist:37i9dQZEVXbMDoHDwVN2tF")["items"][:2]:
				#Track name
				
				track_name = track["track"]["name"]
				track_audio = track["track"]["preview_url"]

				track_pop = track["track"]["popularity"]
				
				print(track_pop," ",track_name)
	
	context.bot.sendVoice(chat_id=chat_id, voice = track_audio, caption = track_name)
	context.bot.sendMessage(chat_id=chat_id, text=msg)
	
def search(update,context):
	global type_registered
	global user_query_type
	global user_query
	if type_registered == True:
		try:
			args=context.args
			for n in args:
				user_query = user_query + " " + n
			spotifyBrowser (update,context,user_query, user_query_type)
		except:
			context.bot.send_message(update.message.chat_id, "Necesitas escribir algo mas\n/Search")

	else:
		context.bot.send_message(update.message.chat_id, "Necesitas especificar el tipo de busqueda")
	user_query = ""

	
def track(update,context):
	global type_registered
	global user_query_type
	user_query_type = "track"
	print(user_query_type)
	context.bot.send_message(update.message.chat_id, "Estas buscando una canción ...\nAhora puedes escribir /search + (nombre de la canción)")
	type_registered = True

def artist(update,context):
	global type_registered
	global user_query_type
	user_query_type = "artist"
	print(user_query_type)
	context.bot.send_message(update.message.chat_id, "Estas buscando un artista...\nAhora puedes escribir /search + (nombre del artista)")
	type_registered = True

def album(update,context):
	global type_registered
	global user_query_type
	user_query_type = "album"
	print(user_query_type)
	context.bot.send_message(update.message.chat_id, "Estas buscando un album...\nAhora puedes escribir /search + (nombre del album)")
	type_registered = True

def playlist(update,context):
	global type_registered
	global user_query_type
	user_query_type = "playlist"
	print(user_query_type)
	context.bot.send_message(update.message.chat_id, "Estas buscando un playlist...\nAhora puedes escribir /search + (nombre ede la playlist)")
	type_registered = True

def spotifyBrowser (update,context,query, query_type):
    # replace all spaces with %20 as per Spotify Web API
	print(query)
	search_query = query.lower().strip().replace(" ", "%20")
	print(search_query)
	api_base_url = "https://open.spotify.com/search/"
	search_types = {
        "track" : api_base_url + search_query + "",
        "artist" : api_base_url + search_query + "/artists",
        "album" : api_base_url + search_query + "/albums",
        "playlist" : api_base_url + search_query + "/playlists"
    }
	search_url = search_types[query_type]
	"""request = urllib.request.Request(search_url)
    request.add_header("Authorization", "Bearer " + auth_token)
    content_data = json.loads(urllib.request.urlopen(request).read())
	"""
	print(search_url)
	context.bot.send_message(update.message.chat_id, search_url)
	#context.bot.send_message(update.message.chat_id, webbrowser.open(search_url))	
	#solo para buscar auto en spotify
	#sleep(7)
	song = search_types["track"] 
	'''
	if (search_url == song ):
		for i in range(23):
			pyautogui.press("tab")
		pyautogui.press("enter")
	'''
	
def main():
	TOKEN="5681916450:AAEaLRcvNbApeDLfTLlW4YDqXVW5Fua43ms"
	updater=Updater(TOKEN, use_context=True)
	dp=updater.dispatcher
	
	# Eventos que activarán nuestro bot.
	dp.add_handler(CommandHandler('start',	start))
	dp.add_handler(CommandHandler('comands', comands))
	dp.add_handler(CommandHandler('start',start))
	dp.add_handler(CommandHandler('track',track))
	dp.add_handler(CommandHandler('artist',artist))
	dp.add_handler(CommandHandler('album',album))
	dp.add_handler(CommandHandler('playlist',playlist))
	dp.add_handler(CommandHandler('search',search))
	# Comienza el bot
	updater.start_polling()
	# Lo deja a la escucha. Evita que se detenga.
	updater.idle()

if __name__ == '__main__':
	main()