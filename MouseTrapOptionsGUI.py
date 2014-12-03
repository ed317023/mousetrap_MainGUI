""" 
Name of Component: 
	MouseTrapOptionsGUI
Authors of Components:
	Andrew Galisa
	Elise Duquette
Originally Developed:
Last Updated:
	12/03/2014
Description:
This is the class where the MouseTrap Options Graphical User Interface is created and displayed. The User has the ability ot change the cursor speed of the MouseTrap program to one of 5 "Level" settings:
Level 1 (slowest) == 1 loop per second
Level 2 (standard)== 10 loops per second
Level 3 	  == 100 loops per second
Level 4		  == 1000 loops per second
Level 5	(fastest) == 10000 loops per second

After clicking on the desired speed, the mousetrap.yaml file is altered to implement the desired cursor speed setting. 
The User also has the option of accessing the File menu and quitting the applicaiton.

"""
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

class MainGUI(Gtk.Window):

""" __init__ 
    sets the default window size, creates the menu bar and sets the window orientation.
    return type void, takes in self
"""
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

""" add_file_menu_actions
    This add the File actions to the menu bar.
    return type void, takes in self and action_group, which is created by the UIManager in the Gtk. 
"""
    def add_file_menu_actions(self, action_group):
        action_filemenu = Gtk.Action("FileMenu", "File", None, None)
        action_group.add_action(action_filemenu)
	# Adds the File Quit option
        action_filequit = Gtk.Action("FileQuit", None, None, Gtk.STOCK_QUIT)
        action_filequit.connect("activate", self.on_menu_file_quit)
        action_group.add_action(action_filequit)

""" add_cursorspeed_menu_actions
    This adds the Cursor Speed actions to the menu bar.
    return type void, takes in self and action_group, which is created by the UIManager in the Gtk.
"""
    def add_cursorspeed_menu_actions(self, action_group):
        action_group.add_actions([
            ("CursorSpeedMenu", None, "Cursor Speed"),
            ("CursorSpeedLevel1", None, "Level 1 (slowest)", None, None,
             self.on_menu_cursor_speed),
	    ("CursorSpeedLevel2", None, "Level 2 (standard)", None, None,
             self.on_menu_cursor_speed),
	    ("CursorSpeedLevel3", None, "Level 3", None, None,
             self.on_menu_cursor_speed),
            ("CursorSpeedLevel4", None, "Level 4", None, None,
             self.on_menu_cursor_speed),
            ("CursorSpeedLevel5", None, "Level 5 (fastest)", None, None,
             self.on_menu_cursor_speed)
        ])
""" create_ui_manager
    This creates the UIManager from the Gtk library. The UIManager constructs a user interface (menus and toolbars) from one or more UI definitions, which reference actions from one or more action groups.
    return type UIManager, takes in self
"""
    def create_ui_manager(self):
        user_interface = Gtk.UIManager()

        # Throws exception if something went wrong
        user_interface.add_ui_from_string(UI_INFO)

        # Add the accelerator group to the toplevel window
        accelgroup = user_interface.get_accel_group()
        self.add_accel_group(accelgroup)
        return user_interface

""" on_menu_file_quit
    This closes the application when the right-hand corner of the GUI, where the 'X' is clicked. 
    return type void, takes in self and widget which is the item selected.
"""
    def on_menu_file_quit(self, widget):
        Gtk.main_quit()

""" on_menu_cursor_speed
    This determines the actions that occur when the cursor speed is selected.
    return type void, takes in self and widget which is the item selected.
"""
    def on_menu_cursor_speed(self, widget):
	with open('mousetrap.yaml', 'r') as file:
		#read a list of lines into array named data
		data = file.readlines()
	print("Menu item " + widget.get_name() + " selected")
	if widget.get_name() == "CursorSpeedLevel1":
		#modify line 105 in mousetrap.yaml		
		data[104] = 'loops_per_second: 1'
	elif widget.get_name() == "CursorSpeedLevel2":
		#modify line 105 in mousetrap.yaml	
		data[104] = 'loops_per_second: 10'
	elif widget.get_name() == "CursorSpeedLevel3":
		#modify line 105 in mousetrap.yaml	
		data[104] = 'loops_per_second: 100'
	elif widget.get_name() == "CursorSpeedLevel4":
		#modify line 105 in mousetrap.yaml	
		data[104] = 'loops_per_second: 1000'
	elif widget.get_name() == "CursorSpeedLevel5":
		#modify line 105 in mousetrap.yaml	
		data[104] = 'loops_per_second: 10000'
	with open('mousetrap.yaml', 'w') as file:
		file.writelines(data)
	#closes file
	file.close()

""" on_button_press_event
    This occurs when a button is clicked.
    rteurn type boolean, takes in self, widget (which is the item selected), and event (which is the action that occured).
"""
    def on_button_press_event(self, widget, event):
            return True # event has been handled

################################################################################################

"""Creates the main GUI Window """

# Creates the MainGUI
window = MainGUI()        
window.connect("delete-event", Gtk.main_quit)
# Shows the GUI Window
window.show_all()
# Initializes the application
Gtk.main()
