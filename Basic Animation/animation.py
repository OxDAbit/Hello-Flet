# ------------------------------------------------------------------------------
# Name:			animation.py
# Purpose:		PoC animación de la navigation bar
# Version:		v0.0.1
#
# Author:		David Alvarez Medina aka 0xDA_bit
# Created:		27/12/2022
#-------------------------------------------------------------------------------

# Importando librerías
import flet
import time

from flet import *

def main(page: Page):
	page.title = 'Navigation Bar Animation'										# Incorporamos el título de la aplicación
	page.horizontal_alignment = 'center'										# Alineamos la aplicación en horizontal
	page.vertical_alignment = 'center'                                        	# Alineamos la aplicación en vertical

	# Columna Principal
	_main_row = Container(
		width=280,
		height=50,
		border_radius=35,
		expand=True,
		bgcolor='white10',
		content=Row(
			alignment=MainAxisAlignment.SPACE_BETWEEN,
			controls=[]
		)
	)

	# Lista de iconos
	_icon_list = [
		icons.PERSON_ADD,
		icons.SEARCH_ROUNDED,
		icons.FAVORITE_ROUNDED,
		icons.NOTIFICATION_ADD_ROUNDED,
		icons.DISCORD_ROUNDED
	]

	def animate_icon(e):														# Animación de la iteracción con los iconos así como modificación del color para saber cual está activo
		e.control.scale = transform.Scale(0.65)
		e.control.update()
		time.sleep(0.15)
		e.control.scale = transform.Scale(1)
		e.control.content.icon_color = 'white'
		e.control.update()

		for control in _main_row.content.controls[:]:
			control.content.selected, control.content.icon_color = False, 'white54'
			control.update()

			if e.control.content.selected != True:
				e.control.content.selected = True
				e.control.content.icon_color = 'white'
				e.control.content.update()

	for icon in _icon_list:														# Iteramos la totalidad de iconos para crear todos los botones de forma dinámica
		icon_container = Container(
			on_click=lambda e: animate_icon(e),
			animate_scale=animation.Animation(duration=500, curve='bounceOut'),
			scale=transform.Scale(1),
			content=IconButton(
				icon=icon,
				icon_size=22,
				icon_color='white54'
			)
		)
		if icon_container.content.icon == _icon_list[0]: icon_container.content.icon_color = 'white'	# Mostramos el icono de la izquierda como el activo por defecto
		_main_row.content.controls.append(icon_container)

	# Contenedor Principal
	_main_container = Container(
		width=280,
		height=590,
		border_radius=35,
		bgcolor='black',
		alignment=alignment.bottom_center,										# Aliniamos los botones a modo de Navigation Bar en la zona inferior y centrados
		padding=20,																# Separación entre botones
		content=_main_row
	)

	page.add(_main_container)
	page.update()

if __name__ == "__main__":
	flet.app(target=main)