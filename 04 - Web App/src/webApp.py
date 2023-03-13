#-------------------------------------------------------------------------------
# Name:			webApp.py
# Purpose:		Aplicación PWA
# Version:		v0.0.1
# Author:		David Alvarez Medina
# Created:		10/03/2023
#-------------------------------------------------------------------------------

# ------------------------------------------------------------------------------
# Módulo encargado de montar el esqueleto de la PWA
# ------------------------------------------------------------------------------

# Importamos librerías
from appLayout import AppLayout
from flet import (Page,colors,UserControl,PopupMenuItem,PopupMenuButton,AppBar,Text,Container,margin,View,padding,TemplateRoute,icons)

class WebApp(UserControl):
	def __init__(self, page: Page):
		super().__init__()
		self.page = page
		self.page.on_route_change = self.routeChange

		# Crea los botones que irán a la derecha dentro del menú de la appbar
		self.loginProfileButton = PopupMenuItem(text='Acceder', on_click=self.logIn)
		self.settingsButton = PopupMenuItem(text='Configuración', on_click=self.settings)
		self.appbarItems = [self.loginProfileButton, self.settingsButton]

		# Crea la App Bar
		self.appBar = AppBar(
								#leading=Icon(icons.GRID_GOLDENRATIO_ROUNDED),
								leading_width=100,
								title=Text(f"Web App", font_family="Helvetica", size=28, text_align="start", color='white'),
								center_title=False,
								toolbar_height=75,
								bgcolor=colors.RED_500,
								actions=[
									Container(
										content=PopupMenuButton(
													icon=icons.MENU_ROUNDED,
													items=self.appbarItems
												),
										margin=margin.only(left=50, right=25),
									)
								]
							)

		self.page.appbar = self.appBar
		self.page.update()

	def build(self):															# Constructor de la clase
		self.layout = AppLayout(
					self,
					self.page,
					tight=True,
					expand=True,
					vertical_alignment="start"
				)
		return self.layout
	def initialize(self):														# Inicializa la clase
		self.page.views.clear()
		self.page.views.append(
			View(
				'/',
				[self.appBar, self.layout],
				padding=padding.all(0),
				bgcolor=colors.WHITE38
			)
		)
		self.page.update()
		self.page.go("/")

	# Action methods
	def routeChange(self, e):													# Cambio de vista
		print('Cambio vista <routing>')
		troute = TemplateRoute(self.page.route)
		if troute.match("/"):
			print('El routing es "/"')
			self.page.go("/")
		elif troute.match("/settings"):
			print('El routing es "/settings"')
			self.page.route('/settings')
		self.page.update()
	def logIn(self, e):															# Acceso al login de ususario
		print('Se ha pulsado el botón de login con el valor: {}'.format(e))
		self.layout.setLoginView()
		self.showMenuOptions()
	def settings(self, e):														# Acceso al menú de configuración de la aplicación
		print('Se ha pulsado el menú de configuración con el valor: {}'.format(e))
		self.layout.setSettingsView()