
from gi.repository import Gtk
from gi.repository import Gdk


class imageWindow(object):
	def __init__(self, config, message):
		self._config = config
		self._window = Gtk.Window(title=message)
		self._canvas = Gtk.Image()
		self._window.add(self._canvas)
		self._window.connect("delete-event", Gtk.main_quit)
		self._window.show_all()

class MainGUI(object):
	
	def __init__(self, config):
        	self._config = config
        	self._windows = {}
	
	
	def start(self):
		'''Start handling events.'''
		Gtk.main()

	def get_screen_width(self):
		return Gtk.Window().get_screen().get_width()

	def get_screen_height(self):
		return Gtk.Window().get_screen().get_height()
		


