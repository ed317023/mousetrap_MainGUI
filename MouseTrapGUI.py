from gi.repository import Gtk, Gdk

# The UIGenerator information in XML 
UI_INFO = """
<ui>
  <menubar name='MenuBar'>
    <menu action='FileMenu'>
      <menuitem action='FileQuit' />
    </menu>
    <menu action='CursorSpeedMenu'>
      <menuitem action='CursorSpeedLevel1' />
      <menuitem action='CursorSpeedLevel2' />	
      <menuitem action='CursorSpeedLevel3' />	
      <menuitem action='CursorSpeedLevel4' />	
      <menuitem action='CursorSpeedLevel5' />		
    </menu>   
  </menubar>
</ui>
"""
########### This is the MainGUI class where the MouseTrap Options Interface is created and displayed.###########

class MainGUI(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="MouseTrap Options")

	# Sets the default window size
        self.set_default_size(250, 200)

        action_group = Gtk.ActionGroup("actions")
	
	# Adds the File and Cursor Speed items to the Menu Bar
        self.add_file_menu_actions(action_group)
        self.add_cursorspeed_menu_actions(action_group)

	# Creates the UI Manager
        user_interface = self.create_ui_manager()
        user_interface.insert_action_group(action_group)

	# Creates the Menu Bar
        menubar = user_interface.get_widget("/MenuBar")

	# Sets orientation
        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        box.pack_start(menubar, False, False, 0)

        eventbox = Gtk.EventBox()
        eventbox.connect("button-press-event", self.on_button_press_event)
        box.pack_start(eventbox, True, True, 0)

        self.add(box)

# Adds the File Menu options and their actions
    def add_file_menu_actions(self, action_group):
        action_filemenu = Gtk.Action("FileMenu", "File", None, None)
        action_group.add_action(action_filemenu)
	
        action_filequit = Gtk.Action("FileQuit", None, None, Gtk.STOCK_QUIT)
        action_filequit.connect("activate", self.on_menu_file_quit)
        action_group.add_action(action_filequit)

# Adds Cursor Speed Menu options and their actions
    def add_cursorspeed_menu_actions(self, action_group):
        action_group.add_actions([
            ("CursorSpeedMenu", None, "Cursor Speed"),
            ("CursorSpeedLevel1", None, "Level 1 (slowest)", None, None,
             self.on_menu_cursor_speed),
	    ("CursorSpeedLevel2", None, "Level 2", None, None,
             self.on_menu_cursor_speed),
	    ("CursorSpeedLevel3", None, "Level 3 (standard)", None, None,
             self.on_menu_cursor_speed),
            ("CursorSpeedLevel4", None, "Level 4", None, None,
             self.on_menu_cursor_speed),
            ("CursorSpeedLevel5", None, "Level 5 (fastest)", None, None,
             self.on_menu_cursor_speed)
        ])
   
    def create_ui_manager(self):
        user_interface = Gtk.UIManager()

        # Throws exception if something went wrong
        user_interface.add_ui_from_string(UI_INFO)

        # Add the accelerator group to the toplevel window
        accelgroup = user_interface.get_accel_group()
        self.add_accel_group(accelgroup)
        return user_interface

# When Quit is selected, quits the application
    def on_menu_file_quit(self, widget):
        Gtk.main_quit()

# Detects when a cursor speed option is selected and performs the corresponding action
    def on_menu_cursor_speed(self, widget):
	print("Menu item " + widget.get_name() + " selected")
	if widget.get_name() == "CursorSpeedLevel1":
		print "1"
	elif widget.get_name() == "CursorSpeedLevel2":
		print "2"
	elif widget.get_name() == "CursorSpeedLevel3":
		print "3"
	elif widget.get_name() == "CursorSpeedLevel4":
		print "4"
	elif widget.get_name() == "CursorSpeedLevel5":
		print "5"

# When a Button is Clicked
    def on_button_press_event(self, widget, event):
            return True # event has been handled
# Creates window
window = MainGUI()        
window.connect("delete-event", Gtk.main_quit)
# Shows window
window.show_all()
# Calls Main
Gtk.main()
