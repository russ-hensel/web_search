# -*- coding: utf-8 -*-
"""
    gui for app in this package
"""

import sys
import tkinter as tk
import tkinter.ttk as ttk
import logging


#----- local
sys.path.append( "../rshlib" )   # should only be needed for rsh development
import gui_ttk_ext

#import gui_helper
from   app_global import AppGlobal

STICKY_ALL = tk.N + tk.S + tk.E + tk.W

# --------------------------------------
class GUI( ):
    """
    the entire gui and its build process
    make me newer
    """
    def __init__( self, controller  ):

        AppGlobal.gui       = self
        self.controller     = controller
        self.parameters     = controller.parameters   # or from app global
        self.logger         = logging.getLogger( AppGlobal.logger_id + ".gui")
        #self.logger.info("in class GUI init for the clip_board_1")
        # logger not currently used by here

        #gui_style           = gui_ttk_ext.GuiStyle( self.parameters.gui_style )

        # ----- start building gui
        self.root           = tk.Tk()

        self.root.title( f"{self.controller.app_name} mode: {AppGlobal.parameters.mode}"
                         f" / version: {self.controller.app_version}" )

        #        # ----- set up root for resizing
        #        self.root.grid_rowconfigure(    0, weight=0 )
        #        self.root.grid_columnconfigure( 0, weight=1 )
        #
        #        self.root.grid_rowconfigure(    1, weight=1 )
        #        self.root.grid_columnconfigure( 1, weight=1 )

        self.use_group_rb    = 0
        self.checkbox_list   = []
        self.use_what_var    = tk.IntVar()
        self.cb_scroll_var   = tk.IntVar()  #
        self.max_lines       = self.parameters.max_lines

        parent_frame         = self.root

        parent_frame.rowconfigure(    0, weight= 0 )
        parent_frame.rowconfigure(    1, weight= 0 )

        parent_frame.columnconfigure( 0, weight= 1 )

        parent_frame.configure( background="grey" )

        self._menu( parent_frame )

        # ---- make frames
        ix_row   = -1  # increment to 0 later
        # ----- ._make_meta_controls_frame
        # a_frame   = self._make_meta_controls_frame( self.root,  )
        # ix_row   += 1
        # a_frame.grid( row=ix_row, column=0, columnspan = 2, sticky = STICKY_ALL )

        # # ----- _make_command_frame_
        # a_frame   = self._make_command_frame_( self.root,  )
        # ix_row   += 1
        # a_frame.grid( row=ix_row, column=0, columnspan = 2, sticky= STICKY_ALL )

        # ----- _make_list_frame
        a_frame   = self._make_list_frame( self.root,  )
        ix_row   += 1
        a_frame.grid( row = ix_row, column=0, columnspan = 2, sticky = STICKY_ALL )

        # ----- _make_group_frame_
        a_frame   = self._make_group_frame( self.root,  )
        ix_row   += 1
        a_frame.grid( row = ix_row, column=0, columnspan = 2, sticky = STICKY_ALL )

        # ----- _make_search_word_frame
        a_frame   = self._make_search_word_frame( self.root,  )
        ix_row   += 1
        a_frame.grid( row = ix_row, column=0, columnspan = 2, sticky = STICKY_ALL )

        # ----------- message frame
        ix_row   += 1
        frame0    = self._make_message_frame( self.root )
        frame0.grid( row=ix_row, column=0, sticky = STICKY_ALL )
        self.root.grid_rowconfigure(    ix_row, weight=1 )

        # ------ end of frames
        self.root.geometry( self.controller.parameters.win_geometry )
        print( "next icon..." )

        if self.parameters.os_win:
            import ctypes
            myappid = self.parameters.icon # arbitrary string
            ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
            #rint( "in windows setting icon" )
            self.root.iconbitmap( self.parameters.icon )
        # msg       = "... icon done...."
        # rint( msg )

    #---------------------
    def _menu (self, parent ) :
        """
        adds a menu bar to the parent
        returns:
            nothing

        some might go directly to AppGlobal

        """
        # ---- configuration
        menubar    = tk.Menu( parent )

        a_menu     = tk.Menu( menubar, tearoff = 0)

        # !! should add
        a_menu.add_command( label   = "Show Parameters",
                            command = self.show_parms )

        a_menu.add_command( label   = "Edit Parameters File",
                            command = self.controller.os_open_parmfile )

        # a_menu.add_command( label   = "Edit Snippets File",
        #                     command = self.controller.os_open_snippets )

        # a_menu.add_command( label   = "Edit Snip Files",
        #                     command = self.controller.os_open_snip_file )

        if self.parameters.readme_fn is not None:

            a_menu.add_command( label   = "Edit Readme",
                                command = self.controller.os_open_readme )

        # a_menu.add_command( label   = "Default Gui",
        #                     command = self.controller.default_gui  )

        # a_menu.add_command( label   = "Wiki Gui",
        #                     command = self.controller.wiki_gui )

        a_menu.add_command( label   = "Edit Log File",
                            command = self.controller.os_open_logfile )

        a_menu.add_command( label   = "Restart",
                            command = self.controller.restart )

        menubar.add_cascade( label  = "Configuration",   menu = a_menu )

        # ---- About
        # a_menu = tk.Menu( menubar, tearoff = 0)
        # a_menu.add_command( label   = "Info", ) #command = self.__showInfo)
        # a_menu.add_command( label   = "Check Update", ) #command = self.__chkUpdate)
        # menubar.add_cascade( label  = "Aboutx", menu = a_menu)

        # ---- help
        a_menu = tk.Menu( menubar, tearoff = 0 )

        a_menu.add_command( label   = "Show Help",
                            command = self.controller.os_open_help )

        a_menu.add_command( label   = "About",
                            command = AppGlobal.about )

        menubar.add_cascade( label  = "Help", menu = a_menu )

        parent.config( menu = menubar )

    # ------------------------------------------
    def _make_meta_controls_frame( self, parent_frame,  ):
        """
        this contains a button area for app control stuff
        passed a parent
        returns this main_frame
        """
        tframe_1      = gui_ttk_ext.TitledFrame( parent_frame, "System Operations:",
                                     self.parameters.id_color )
        a_frame       = tframe_1.frame

        a_button      = tframe_1.make_button( button_text = "Ed Log",
                                         command = self.controller.os_open_logfile  )
        #a_button.config( command = self.controller.os_open_logfile  )

        a_button      = tframe_1.make_button( button_text =  "Ed Parms" )
        a_button.config( command = self.controller.os_open_parmfile  )

        if self.parameters.readme_fn is not None:
            a_button = tframe_1.make_button( button_text =  "Ed Readme" )
            a_button.config( command = self.controller.os_open_readme  )

        a_button = tframe_1.make_button( button_text =  "Restart" )
        a_button.config( command = self.controller.restart  )

        a_button = tframe_1.make_button( button_text =  "Help" )
        a_button.config( command = self.controller.os_open_help  )

        a_button = tframe_1.make_button( button_text =  "About" )
        a_button.config( command = AppGlobal.about  )

        return a_frame

    # ------------------------------------------
    def _make_search_word_frame( self, parent_frame,  ):
        """
        buttons for commands that operate on files
        returns this frame
        !! have function make the button with the command
        """
        a_frame     = tk.Frame( parent_frame )

        # self.use_what_var      = tk.IntVar()
        # --------
        ix_row      = -1
        ix_col      = 0

        # --------
        ix_row      += 1
        ix_col      = 0
        a_widget              = ttk.Label(a_frame, text="Search Words:", )
        a_widget.grid(  column = ix_col, row = ix_row, )

        # --------
        ix_col   += 1
        self.search_words_var = tk.StringVar()     # does the tetvariable change anything??
        a_widget              = ttk.Entry( a_frame ,
                                   width        = 100,
                                   text         = "search words",
                                   textvariable = self.search_words_var )
        self.search_words_var.set( AppGlobal.parameters.default_search_string )
        a_widget.grid(  column = ix_col, row = ix_row, ) #sticky= E+W+N+S ))
        self.search_word_widget   = a_widget

        # --------
        ix_col   += 1
        a_widget = ttk.Button( a_frame , width = 12,   text = "Search Web", )
        a_widget.config( command = self.controller.cb_search  )
        a_widget.grid( row = ix_row, column = ix_col    )

        ix_col   += 1
        a_widget = ttk.Label( a_frame ,    text = "Remember to open a new window", )  # width = 12,
        a_widget.grid( row = ix_row, column = ix_col    )

        # --------
        ix_col   += 1
        a_widget = ttk.Button( a_frame , width = 12,   text = "Show Search", )
        a_widget.config( command = self.controller.cb_show_search  )
        a_widget.grid( row = ix_row, column = ix_col    )

        return a_frame

    # ------------------------------------------
    def _make_list_frame( self, parent_frame,  ):
        """
        buttons for commands that operate on files
        returns this frame
        !! have function make the button with the command
        """
        a_frame     = tk.Frame( parent_frame )

        # self.use_what_var      = tk.IntVar()
        # --------
        ix_row      = 0
        ix_col      = 0
        a_widget    = ttk.Radiobutton( a_frame,
                                       text        = "Use Lists",
                                       variable    = self.use_what_var,
                                       value       = 1, # and other buttons 1
                                       command     = self.rb_command )

        a_widget.grid(  column = ix_col, row = ix_row, )

        # --------
        #ix_row      = 0
        ix_col      += 1
        a_widget    = ttk.Label(a_frame, text="Search Site Lists", )
        a_widget.grid(  column = ix_col, row = ix_row, )

        ix_col   += 1
        values      = [i_list_name for i_list_name in self.parameters.search_lists.keys() ]
        a_widget    = ttk.Combobox( a_frame, values = values, width = 100  )

        # may be able to set combo box by index of its list, try next put in ex-tk_combobox

        # first_key   = next( iter( AppGlobal.parameters.search_lists) ) ok
        # a_widget.set_text( first_key )  ng

        a_widget.current( 0 )  # was working? now not ??? but used var below

        a_widget.bind("<<ComboboxSelected>>", self.setup_search )
        comb_var      = tk.StringVar()
        a_widget['state'] = 'readonly'
        a_widget.config( textvariable  =  comb_var )   # use get, but works better in a class

        first_key   = next( iter( AppGlobal.parameters.search_lists) )
        comb_var    = first_key
        a_widget.current( 2 ) # !! right now seems not to be working
        a_widget.grid(  column = ix_col, row = ix_row, )
        self.search_site_widget  = a_widget

        # # --------
        # ix_row      += 1
        # ix_col      = 0
        # a_widget              = ttk.Label(a_frame, text="Search Words:", )
        # a_widget.grid(  column = ix_col, row = ix_row, )

        # ix_col   += 1
        # self.search_words_var = tk.StringVar()     # does the tetvariable change anything??
        # a_widget              = ttk.Entry( a_frame ,
        #                            width        = 100,
        #                            text         = "search words",
        #                            textvariable = self.search_words_var )
        # self.search_words_var.set( AppGlobal.parameters.default_search_string )
        # a_widget.grid(  column = ix_col, row = ix_row, ) #sticky= E+W+N+S ))
        # self.search_word_widget   = a_widget

        return a_frame

    # ------------------
    def rb_command( self, ):
        """
        command when radio button called, just prints (see code )
        debug only may not be in use
        """
        print("rb_command_function")


    # ------------------------------------------
    def _make_group_frame( self, parent_frame,  ):
        """
        groups are as set up in search_objects group_lists
        returns this frame
        !! have function make the button with the command
        """
        a_frame     = tk.Frame( parent_frame )

        # --------
        ix_col_max  = 10
        placer      = gui_ttk_ext.PlaceInGrid( a_max = ix_col_max, by_rows = False )

        a_widget            = ttk.Radiobutton( a_frame,
                                       text        = "Use Groups",
                                       variable    = self.use_what_var,
                                       value       = self.use_group_rb,
                                       # command     = self.controller.group_check_button_clicked
                                       )

        placer.place(  a_widget, columnspan = None,   rowspan = None, sticky = None )

        # ----
        a_widget = ttk.Button( a_frame , width = 10,  text = "Clear" )
        a_widget.config( command = self.cb_clear_groups )

        placer.place(  a_widget, columnspan = None,   rowspan = None, sticky = None )

        web_searcher_groups    = self.controller.web_server_collections._build_web_searcher_groups()
        placer.new_row( delta_row = 1, indent = 1 )
        for i_group in web_searcher_groups:
            a_widget = ttk.Checkbutton( a_frame ,
                                        width     = 20,
                                        text      = i_group,
                                        # variable  = group_var,
                                        command   = self.group_check_button_clicked )

            self.checkbox_list.append( a_widget )
            #a_widget.state(['selected'])
            a_widget.state( ['!alternate'])  # seems to be required to make next work
            a_widget.state( ['!disabled','!selected'] )   #  !selected ok   selected not working

            placer.place(  a_widget, columnspan = None,   rowspan = None, sticky = None )

        return a_frame

    # ------------------------------------------
    def _make_message_frame( self, parent,  ):
        """
        make the message frame for user feedback
        """
        a_frame              = gui_ttk_ext.MessageFrame( parent,  )
        self.message_frame   = a_frame
        return a_frame

    # ==================== end construction ====================
    # construction helpers

    def _make_titled_listbox( self, parent_frame, a_title ):
        """
        return ( famelike_thing, listbox_thing)  ?? make a class, better acces to components
        """
        a_frame      = ttk.Frame(parent_frame)
        a_listbox    = ttk.Listbox( a_frame, height=5 )
        a_listbox.grid( column=0, row=1, sticky= STICKY_ALL )
        a_scrolbar   = ttk.Scrollbar( a_frame, orient=tk.VERTICAL, command=a_listbox.yview)
        a_scrolbar.grid(column=1, row=1, sticky=(tk.N, tk.S))
        a_listbox['yscrollcommand'] = a_scrolbar.set
        a_label      = ttk.Label( a_frame, text= a_title )
        a_label.grid( column=0, row=0, sticky=( tk.N, tk.E, tk.W) )
        #  ttk.Sizegrip().grid(column=1, row=1, sticky=(tk.S, tk.E)) size grip not appropriate here
        a_frame.grid_columnconfigure( 0, weight=1 )
        a_frame.grid_rowconfigure(    0, weight=0 )
        a_frame.grid_rowconfigure(    1, weight=1 )
        return ( a_frame, a_listbox )

    #----------------------------------------------------------------------
    def print_string( self,       a_string,         plus_newline = True,
                     title = "", clear = False,     update_now   = False ):
        """
        same as the message box extension
        """
        self.message_frame.print_string( self, a_string,
                                         plus_newline = plus_newline,
                                         title        = title,
                                         clear        = clear,
                                         update_now   = update_now )

    #----------------------------------------------------------------------
    def write_gui_wt(self, title, a_string ):
        """
        write to gui with a title.
        title     the title
        a_string  additional stuff to write
        make a better function with title = ""  ??
        title the string with some extra formatting
        clear and write string to input area
        """
        self.write_gui( f" =============== { title } ==> \n {a_string}" )

    #----------------------------------------------------------------------
    def write_gui( self, string, add_nl = True ):
        """
        clear and write string to input area
        leave disabled
        """
        if add_nl:
            string   = string +"\n"
        self.message_frame.display_string( string )

    # ------------------------------------------
    def enable_ht_buttons( self, enable_if_true ):
        """
        for the clear button
        clear the text area
        even can be anything
        enable_if_true       True enable else disable
        """
        if enable_if_true:
            new_state  = tk.NORMAL
            #rint( f"enable_ht_buttons tk.NORMAL" )
        else:
            new_state  = tk.DISABLED
            #rint( f"enable_ht_buttons tk.DISABLED" )
        self.widget_run_process.config(      state = new_state )
        # self.widget_define_db.config(        state = new_state )
        # self.widget_explore_keeps.config(    state = new_state )
        # self.widget_explore_dups.config(     state = new_state )
        # self.widget_write_file_dups.config(  state = new_state )

    # ------------------------------------------
    def do_clear_button( self, event):
        """
        for the clear button
        clear the text area
        even can be anything
        """
        self.message_frame.do_clear_button( event )

    # ------------------------------------------
    def setup_search( self,  event ):
        """
        for the search see:
        """
        #rint( "setup_search" )
        key     = self.search_site_widget.get()
        #rint( f"setup_search {key}" )
        self.controller.build_search_list( key )
        self.site_search_list_clicked()

    # ------------------------------------------
    def minimize( self,  ):
        """
        what it says
        """
        gui_ttk_ext.minimize_gui( self.root )

    # ------------------------------------------
    def cb_clear_groups( self,  ):
        """
        what it says
        """
        for i_group   in  self.checkbox_list:

            i_group.state( ['!alternate'])               # seems to be required to make next work
            i_group.state( ['!disabled','!selected'] )   # ['!disabled','selected']

    # ------------------------------------------
    def get_group_names( self,  ):
        """
        return
            list of the group names checked
        """
        selected_group_list    = []

        for i_group   in  self.checkbox_list:
            group_name    = i_group.cget( "text" )
            instate       = i_group.instate(['selected'])
            #rint( "get_group_names", " ", group_name, " ", a_state, "", instate )
            if instate:
                selected_group_list.append( group_name )

        print( f"get_group_names selected_group_list {selected_group_list}" )
        return selected_group_list

    # ------------------------------------------
    def setup_search_group( self,  event ):
        """
        for the search see:
        """
        print( "setup_search_group not done !!!!!!!!!!!!!!!!!!!!" )
        # key     = self.search_site_widget.get()
        # print( f"setup_search {key}" )
        # self.controller.build_search_list( key )setup_search_group

   # ----------------------------------------------
    def site_search_list_clicked( self,   ):
        """
        what it says
        for prompt display need to have multi threading
        """
        #msg   = "site_searh_list_clicked"
        # set rb for group
        self.use_what_var.set( 1 ) # need correct magic value, make symbolic
        #self.write_gui( msg )

   # ----------------------------------------------
    def group_check_button_clicked( self,   ):
        """
        what it says
        """
        #msg   = "group_check_button_clicked"
        # set rb for group
        self.use_what_var.set( 0 )    # need correct magic value, make symbolic
        #self.gui.write_gui( msg )

    #----------------------------------------------------------------------
    def show_parms(self, ):
        """
        what it says, read
        """
        msg     = f"{AppGlobal.parameters}"
        title   = "Parameters"
        #rint( msg )
        self.write_gui_wt( title, msg )

# =================================================

if __name__ == "__main__":

    import  web_search
    web_search.main( )

# =================== eof ==============================
