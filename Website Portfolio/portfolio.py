# ------------------------------------------------------------------------------
# Name:			portfolio.py
# Purpose:		Web estilo portfolio
# Version:		v0.0.1
#
# Author:		David Alvarez Medina aka 0xDA_bit
# Created:		27/12/2022
#-------------------------------------------------------------------------------

# Importando módulos
import flet
import time
from flet import *

def main(page: Page):
	page.title = 'Portfolio'

	# Acciones de la Navigation Bar
	## Modifica el color del contenido de la Navigation Bar al poner el ratón encima del texto
	def change_text_color(e):
		if e.control.content.color == 'white':
			e.control.content.color = '#475569'
			e.control.content.update()
		elif e.control.content.color != 'white':
			e.control.content.color = 'white'
			e.control.content.update()
	## Modifica la visibilidad del contenido de la Navigation Bar al modificar el tamaño de la ventan
	def on_resize(e):
		if page.width <= 730:
			_navbar.controls[0].visible = False
			_navbar.update()
			_min_navbar.visible = True
			_min_navbar.update()
		else:
			_navbar.controls[0].visible = True
			_navbar.update()
			_min_navbar.visible = False
			_min_navbar.update()

	# Acciones botón redes sociales
	## Muestra los iconos al pasar el ratón por encima del texto
	def _animate_social(e):
		if e.data == 'true':
			_icon_text.offset, _icon_text.opacity=transform.Offset(0, 0.05), 0
			_icon_text.update()
			for btn in _social_button.controls[:]:
				btn.offset, btn.opacity = transform.Offset(0, 0.15), 100
				btn.update()
				time.sleep(0.1)
		else:
			for btn in _social_button.controls[:]:
				btn.offset, btn.opacity = transform.Offset(0, -0.9), 0
				btn.update()
				time.sleep(0.1)
			_icon_text.offset, _icon_text.opacity=transform.Offset(0, -1.1), 100
			_icon_text.update()

	# Navigation Bar
	_navbar = Row(
		alignment='end',
		controls=[
			Container(
				padding=padding.only(right=20),
				height=64,
				content=Row(
					controls=[
						Container(
							on_hover=lambda e: change_text_color(e),
							content=
								Text(
									'Posts',
									weight='w600',
									color='white'
								)
						),
						Container(
							on_hover=lambda e: change_text_color(e),
							content=
								Text(
									'Sobre Mi',
									weight='w600',
									color='white'
								),
						),
						Container(
							on_hover=lambda e: change_text_color(e),
							content=
								Text(
									'Contacto',
									weight='w600',
									color='white'
								)
						)
					]
				)
			)
		]
	)
	# Miminizar Navigation Bar
	_min_navbar = Row(
		visible=False,
		alignment='end',
		controls=[
			PopupMenuButton(
				items=[
					PopupMenuItem(icon=icons.POST_ADD, text='Posts'),
					PopupMenuItem(icon=icons.MAN, text='Sobre Mi'),
					PopupMenuItem(icon=icons.DESIGN_SERVICES, text='Servicios')
				]
			)
		]
	)

	# Títulos
	_tittle = ResponsiveRow(
		alignment='center',
		controls=[
			Container(
				col={'xs':12, 'sm':10, 'md':10, 'lg':10, 'xl':12},
				alignment=alignment.top_center,
				padding=20,
				content=
					Text(
						'Título largo\nWeb Portfolio',
						size=45,
						weight='w600',
						text_align='center'
					)
			)
		]
	)
	# Sub título del portfolio
	_sub_tittle = ResponsiveRow(
		alignment='center',
		controls=[
			Container(
				col={'xs':12,'sm':10,'md':10, 'lg':10, 'xl':12},
				padding=20,
				alignment=alignment.top_center,
				content=Text(
					'Bienvenidos a mi blog personal!\nEcha un vistazo ;)',
					text_align='center',
					size=16,
					weight='w500'
				)
			)
		]
	)

	# Botón redes sociales
	_icon_list = [
		icons.FACEBOOK,
		icons.SHARE_SHARP,
		icons.MAIL
	]
	_social_button = Row(
		alignment='center',
		vertical_alignment='center'
	)
	_icon_text = Text(
		'Conectamos?',
		size=16,
		color='white',
		weight='w800',
		animate_opacity=50,
		offset=transform.Offset(0, -1.1),
		animate_offset=animation.Animation(duration=1000, curve='elasticout'),
	)

	for icon in _icon_list:
		_icon = IconButton(
			icon=icon,
			icon_size=22,
			icon_color='white',
			offset=transform.Offset(0, -0.9),
			animate_offset=animation.Animation(duration=1000, curve='elasticout'),
			animate_opacity=50,
			opacity=0
		)
		_social_button.controls.append(_icon)
	_icon_container = Container(
		width=145,
		height=50,
		bgcolor='blue800',
		border_radius=8,
		alignment=alignment.center,
		on_hover=lambda e: _animate_social(e),
		content=Column(
			spacing=0,
			alignment='center',
			horizontal_alignment='center',
			controls=[
				_social_button,
				Row(
					alignment='center',
					controls=[
						_icon_text
					]
				)
			]
		)
	)

	# Rejilla responsive del portfolio
	_items = ['PRIMER POST', 'SEGUNDO POST', 'TERCER POST', 'CUARTO POST', 'QUINTO POST', 'SEXTO POST', 'SEPTIMO POST', 'OCTAVO POST']
	_item_row = ResponsiveRow(alignment='start')
	_container_item = Container(
		padding=20,
		content=_item_row
	)
	for item in _items:
		_item_container = Container(
			width=300,
			height=300,
			bgcolor='white',
			aspect_ratio=1,
			padding=35,
			border_radius=12,
			alignment=alignment.center,
			col={'xs':12, 'sm':4, 'md':4, 'lg':6, 'xl':4},
			content=Container(
				aspect_ratio=1,
				border_radius=8,
				bgcolor='black',
				alignment=alignment.center,
				content=Text(
					f'{item}',
					size=21
				)
			)
		)
		_item_row.controls.append(_item_container)

	# Columna principal
	_main_column = Column(
		horizontal_alignment='center',
		scroll='auto'
	)
	_main_column.controls.append(_navbar)
	_main_column.controls.append(_min_navbar)
	_main_column.controls.append(_tittle)
	_main_column.controls.append(_sub_tittle)
	_main_column.controls.append(Container(padding=padding.only(top=40)))
	_main_column.controls.append(_icon_container)
	_main_column.controls.append(Container(padding=padding.only(bottom=40)))
	_main_column.controls.append(_container_item)

	# Background container
	_bkg = Container(
		height=page.height,
		expand=True,
		margin=-10,
		gradient=LinearGradient(
			begin=alignment.bottom_left,
			end=alignment.bottom_right,
			colors=[
				'#13457a',
				'#80d0c7'
			]
		),
		content=_main_column
	)

	page.add(_bkg)
	page.on_resize = on_resize

if __name__ == "__main__":
	flet.app(target=main)