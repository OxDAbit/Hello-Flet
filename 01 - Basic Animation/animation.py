# ------------------------------------------------------------------------------
# Name:			animation.py
# Purpose:		PoC animación de la navigation bar
# Version:		v0.0.2
#
# Author:		David Alvarez Medina aka 0xDA_bit
# Created:		27/12/2022
#-------------------------------------------------------------------------------

# Importando módulos
import flet
import time

from flet import *

def animate_icon(e, page, _icon_view, _navigation_bar):							# Animación de la iteracción con los iconos así como modificación del color para saber cual está activo
	e.control.scale = transform.Scale(0.65)
	e.control.update()
	time.sleep(0.15)
	e.control.scale = transform.Scale(1)
	e.control.content.icon_color = 'white'
	e.control.update()

	_icon_view.content.value = '{}'.format(e.control.content.icon)
	page.update()

	for control in _navigation_bar.content.controls[:]:							# Iteramos todos los iconos
		control.content.selected, control.content.icon_color = False, 'white54'		# Seteamos los iconos con el flag "selected" a False y ponemos el color correspondiente al icono desactivado
		control.update()													# Actualziamos la vista para mostrar los cambios

		if e.control.content.selected != True:								# Siempre que un icono tengo el estado "selected" a False...
			e.control.content.selected = True								# Seteamos la variable "selected" a True
			e.control.content.icon_color = 'white'							# Seleccionamos el color de icono correspondiente a "estado activo"
			e.control.content.update()										# Actualizamos la vista para mostrar los cambios

def load_icons(page, _icon_view, _navigation_bar):
	# Lista de iconos
	_icon_list = [
		icons.PERSON_ADD,
		icons.SEARCH_ROUNDED,
		icons.FAVORITE_ROUNDED,
		icons.NOTIFICATION_ADD_ROUNDED,
		icons.DISCORD_ROUNDED
	]

	for icon in _icon_list:													# Iteramos la totalidad de iconos para crear todos los botones de forma dinámica
		icon_container = Container(
			on_click=lambda e: animate_icon(e, page, _icon_view, _navigation_bar),
			animate_scale=animation.Animation(duration=500, curve='bounceOut'),
			scale=transform.Scale(1),
			content=IconButton(
				icon=icon,
				icon_size=22,
				icon_color='white54'
			)
		)
		if icon_container.content.icon == _icon_list[0]:
			icon_container.content.icon_color = 'white'						# Mostramos el icono de la izquierda como el activo por defecto
			_icon_view.content.value = '{}'.format(_icon_list[0])
		_navigation_bar.content.controls.append(icon_container)				# Añadimos el contendeor con los iconos en la Columna Principal
def load_app(page):
	# Columna Principal
	_navigation_bar = Container(
		width=280,
		height=50,
		border_radius=35,
		bgcolor='white10',
		content=Row(
			alignment=MainAxisAlignment.SPACE_BETWEEN,
			controls=[]
		)
	)

	_icon_view = Container(
		width=260,
		height=500,
		border_radius=14,
		bgcolor='red',
		alignment=alignment.center,
		content=Text(
			color='white',
			size=20
		)
	)

	load_icons(page, _icon_view, _navigation_bar)

	# Contenedor Principal
	_main_container = Container(
		width=280,
		height=590,
		border_radius=35,
		bgcolor='black',
		alignment=alignment.bottom_center,										# Aliniamos los botones a modo de Navigation Bar en la zona inferior y centrados
		padding=14,
		content=Column(
			controls=[
				_icon_view,
				_navigation_bar
			]
		)
	)

	page.add(_main_container)
	page.update()

def main(page: Page):
	page.title = 'Navigation Bar Animation'										# Incorporamos el título de la aplicación
	page.horizontal_alignment = 'center'										# Alineamos la aplicación en horizontal
	page.vertical_alignment = 'center'                                        	# Alineamos la aplicación en vertical

	load_app(page)

if __name__ == "__main__":
	flet.app(target=main)