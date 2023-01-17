# ------------------------------------------------------------------------------
# Name:			sidebarAPP.py
# Purpose:		Aplicación con menú lateral (sidebar)
# Version:		v0.0.1
#
# Author:		David Alvarez Medina aka 0xDA_bit
# Created:		10/01/2023
#-------------------------------------------------------------------------------

# Importando módulos
import flet
from flet import *
from sidebar import ModernNavBar

# Creamos la clase correspondiente al stack principal
class MainStackContainer(UserControl):
	def __init__(self):
		super().__init__()

	# Abrir y cerrar sidebar menú
	def HideMenu(self,e):
		main = self.controls[0].content.controls[0].controls[0]
		menu = self.controls[0].content.controls[1].controls[0]
		if menu.width == 185:
			menu.width = 0
			menu.border = None
			menu.update()

			main.opacity = 1
			main.update()
		else:
			pass

	def ShowMenu(self, e):
		main = self.controls[0].content.controls[0].controls[0]
		menu = self.controls[0].content.controls[1].controls[0]
		if menu.width == 0:
			menu.width = 185
			menu.border = border.only(right=border.BorderSide(2, 'purple300'))
			menu.update()

			main.opactity = 0.35
			main.update()
		else:
			menu.width = 0
			menu.border = None
			menu.update()

			main.opactity = 1
			main.update()

	def build(self):
		return Container(
			width=280,
			height=600,
			bgcolor='white',
			border_radius=32,
			border=border.all(8, 'black'),
			padding=padding.only(top=25, left=5, right=5, bottom=25),
			content=Stack(
				expand=True,
				controls=[
					MainPage(self.ShowMenu, self.HideMenu),							# Este control (clase) corresponde a la vista principal
					MenuPage(self.ShowMenu)											# Este control (clase) corresponde al menú sidebar
				]
			)
		)

class MainPage(UserControl):
	def __init__(self, function, function2):
		super().__init__()
		self.function = function
		self.function2 = function2

	# Lista dummy para imprimir en la ListView
	def MakeList(self):
		dummy_list = ListView(
			expand=True,
			spacing=10,
			padding=20,
			auto_scroll=False
		)

		for i in range(60):
			dummy_list.controls.append(
				Container(
					alignment=alignment.center,
					padding=8,
					height=40,
					bgcolor='#1d1d1d',
					border_radius=8,
					content=Text(i),
					visible=True,
					animate=animation.Animation(200, 'decelerate')
				)
			)

		return dummy_list

	# Método de filtrado de los valores impresos en la ListView
	def FilterList(self, e):
		if e.data == 'true':													# Valor devuelto por el checkbox cuando está clickado
			if e.control.label == 'Impares':
				for item in self.controls[0].content.controls[3].controls[:]:
					if item.content.value % 2 == 0:
						item.height = 0
						item.update()
			if e.control.label == 'Pares':
				for item in self.controls[0].content.controls[3].controls[:]:
					if item.content.value % 2 != 0:
						item.height = 0
						item.update()
		else:
			if e.control.label == 'Impares':
				for item in self.controls[0].content.controls[3].controls[:]:
					if item.content.value % 2 == 0:
						item.height = 40
						item.update()
			if e.control.label == 'Pares':
				for item in self.controls[0].content.controls[3].controls[:]:
					if item.content.value % 2 != 0:
						item.height = 40
						item.update()

	# Creamos la topbar con los dos botones para filtrar los resultados
	def FilterBoxes(self):
		return Container(
			bgcolor='#1d1d1d',
			border_radius=8,
			content=Row(
				expand=True,
				alignment=MainAxisAlignment.CENTER,
				controls=[
					Row(
						spacing=0,
						controls=[
							Checkbox(
								label='Pares',
								fill_color='purple300',
								on_change=lambda e: self.FilterList(e)
							)
						]
					),
					Row(
						spacing=0,
						controls=[
							Checkbox(
								label='Impares',
								fill_color='purple300',
								on_change=lambda e: self.FilterList(e)
							)
						]
					)
				]
			)
		)

	def build(self):
		return Container(
			expand=True,
			clip_behavior=ClipBehavior.HARD_EDGE,
			opacity=1,
			animate_opacity=300,
			on_click=self.function2,
			content=Column(
				controls=[
					Row(
						controls=[
							Row(
								expand=1,
								alignment=MainAxisAlignment.START,
								controls=[
									IconButton(
										icon=icons.MENU_ROUNDED,
										icon_size=15,
										icon_color='black',
										on_click=self.function
									)
								]
							),
							Row(
								expand=3,
								alignment=MainAxisAlignment.START,
								controls=[
									Text(
										'Filtrar datos',
										size=15,
										color='black',
										weight='bold'
									)
								]
							)
						]
					),
					Container(
						padding=padding.only(left=15, right=15),
						opacity=0.85,
						content=Divider(height=5, color='black')
					),
					self.FilterBoxes(),
					self.MakeList()
				]
			)
		)
class MenuPage(UserControl):
	def __init__(self, function):
		super().__init__()
		self.function = function

	def build(self):
		return Container(
			width=0,
			bgcolor='white',
			animate=animation.Animation(400, 'decelerate'),
			clip_behavior=ClipBehavior.HARD_EDGE,
			content=Column(
				expand = True,
				controls=[
					Row(
						controls=[
							Text()
						]
					),
					Column(
						expand=True,
						controls=[
							ModernNavBar()
						]
					)
				]
			)
		)

def main(page: Page):
	page.horizontal_alignment = 'center'
	page.vertical_alignment = 'center'
	page.bgcolor = 'deeppurple200'

	page.add(MainStackContainer())
	page.update()

if __name__ == '__main__':
	flet.app(target=main)