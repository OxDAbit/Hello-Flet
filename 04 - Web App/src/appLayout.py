#-------------------------------------------------------------------------------
# Name:			appLayout.py
# Purpose:		Aplicación PWA
# Version:		v0.0.1
# Author:		David Alvarez Medina
# Created:		10/03/2023
#-------------------------------------------------------------------------------

# ------------------------------------------------------------------------------
# Módulo para gestionar las vistas de la aplicación
# ------------------------------------------------------------------------------

# Importamos librerías
from flet import (Row,Page,Control,Column,Text)
from sidebar import Sidebar

class AppLayout(Row):
	def __init__(self, app, page: Page, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.app = app
		self.page = page
		self.page.on_resize = self.pageResize									# Configuración para asociar el método "pageResize" a la aplicación

		self.login_view = Text('Vista de Login', color='black')					# Creamos la vista correspondiente al menú de login
		self.config_view = Text('Vista de configuración', color='black')		# Creamos la vista correspondiente al menú de configuración

		self._active_view: Control = self.login_view							# Seleccionamos la vista "login" como la vista inicial
		self.controls = [self.active_view]										# Listamos la totalidad de componentes que tendrá la vista principal

	@property
	def active_view(self):														# Propiedad para gestionar la vista actual
		return self._active_view
	@active_view.setter
	def active_view(self, view):												# Método encargado de configurar la nueva vista actual
		self._active_view = view
		self.controls[-1] = self._active_view
		self.update()

	def setLoginView(self):														# Método que setea la vista "Login" como la actual tras la selección del usuario en la AppBar
		self.active_view = self.login_view
		self.page.update()
	def setSettingsView(self):													# Método que setea la vista "Configuración" como la actual tras la selección del usuario en la AppBar
		self.active_view = self.config_view
		self.page.update()
	def pageResize(self, e=None):												# Método que se ejecuta al modifcar el tamaño de la PWA
		print('Re escalando el tamaño de la vista')
		self.page.update()