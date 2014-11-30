
from gi.repository import Gtk
from gi.repository import Gdk


class imageWindow(object):
	def __init__(self, config, message):
		self._config = config
		self._window = Gtk.Window(title="Options")
		self._canvas = Gtk.Image()
		self._window.add(self._canvas)
		self._window.connect("delete-event", Gtk.main_quit)
		self._window.show_all()

class MainGUI(object):
	
	def __init__(self, config):
        	self._config = config
        	self._windows = {}

                #creates menu bar
        	accel_group = Gtk.AccelGroup()
        	item_factory = Gtk.ItemFactory(Gtk.MenuBar, "<main>", accel_group)
        	self.create_items(self.menu_items)
        	window.add_accel_group(accel_group)
        	
        	self.menu_items = (
   	        ( "/_File",         None,         None, 0, "<Branch>" ),
   	        ( "/File/sep1",     None,         None, 0, "<Separator>" ),
	        ( "/File/Quit",     "<control>Q", gtk.main_quit, 0, None ),
   	        ( "/_Options",      None,         None, 0, "<Branch>" ),
   	        ( "/Options/Test",  None,         None, 0, None ),
   	        ( "/_Help",         None,         None, 0, "<LastBranch>" ),
   	        ( "/_Help/About",   None,         None, 0, None ),
   	        )

        	#adding spin button for cursor movement speed
        	adjustment = Gtk.Adjustment(value=0, lower=0, upper=0, step_incr=0, page_incr=0, page_size=0)
        	spin_button = Gtk.SpinButton(adjustment=None, climb_rate=0.0, digits=0)
                self.SpinButton.add(self.spin_button)

                #information within the window
                frame = Gtk.Frame("Options")
                label = Gtk.Label("Pick preferred cursor movement speed")
                frame.add(label)

        	#making buttions for apply, cancel, and help
        	bbox.set_border_width(5)
   	        frame.add(bbox)

   	        bbox.set_layout(layout)
	        bbox.set_spacing(spacing)
   
        	button = Gtk.Button(stock=Gtk.STOCK_OK)
   	        bbox.add(button)
	
   	        button = Gtk.Button(stock=Gtk.STOCK_CANCEL)
	        bbox.add(button)
   	
   	        button = Gtk.Button(stock=Gtk.STOCK_HELP)
   	        bbox.add(button)

   	        hbox = Gtk.HBox(False, 0)
   	        hbox.set_border_width(10)
   	        frame.add(hbox)
   
        	hbox.pack_start(self.create_bbox(False, "",30, Gtk.BUTTONBOX_EDGE)True, True, 5)

                #visualize everything in window
                window.show_all()
	
	def start(self):
		'''Start handling events.'''
		Gtk.main()
		return 0

	def get_screen_width(self):
		return Gtk.Window().get_screen().get_width()

	def get_screen_height(self):
		return Gtk.Window().get_screen().get_height()
