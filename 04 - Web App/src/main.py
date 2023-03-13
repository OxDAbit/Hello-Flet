#-------------------------------------------------------------------------------
# Name:			main.py
# Purpose:		Aplicación PWA
# Version:		v0.0.1
# Author:		David Alvarez Medina
# Created:		10/03/2023
#-------------------------------------------------------------------------------

# ------------------------------------------------------------------------------
# Módulo inicial encargado de cargar la configuración y la PWA
# ------------------------------------------------------------------------------

# Importamos librerías
import flet

from webApp import WebApp
from flet import (Page,colors,theme)

def loadProperties():
	print('Loading JSON properties')
	pass
def main(page: Page):
	loadProperties()															# Cargamos los parámetros de configuración necesarios
	page.title = "Web Application"												# Título de la aplicación
	page.padding = 0															#
	page.theme = theme.Theme(font_family="Verdana")								# selección tipografía
	page.theme.page_transitions.windows = "cupertino"
	#page.fonts = {"Pacifico": "Pacifico-Regular.ttf"}
	page.bgcolor = colors.BLUE_GREY_200											# Background color
	#app = WebApp(page, InMemoryStore())
	app = WebApp(page)															# Creamos una instancia de la clase SNSObApp
	page.add(app)																# Añadimos la instancia a la página
	page.update()																# Actualizamos la página
	app.initialize()															# Inicializamos la aplicación

if __name__ == '__main__':
	flet.app(target=main, assets_dir="../assets", view=flet.WEB_BROWSER)