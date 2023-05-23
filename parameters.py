# -"*- codin"g: utf-8" -*-

"""
parameters for the application



"""

import logging
import sys
import os

# ------ local ------


from   app_global import AppGlobal

# see comment in web_search.py
sys.path.append( "/media/russ/j_sg_bigcase/sync_py_3/_projects/rshlib/" )
sys.path.append( "../rshlib/" )


#-------------------------------------------
class Parameters(  ):
    """
    manages parameter values use like ini file
    a struct but with a few smarts
    modify to suit your situation but
        it is code so you can mess it up, just be a bit
        thoughtfull
    """
    # -------
    def choose_mode( self ):
        """
        just choose one of the modes below
        this will override some values in defaut mode
        """
        # ---- ---------- choose ---------
        #self.mode_example()

        # more modes, not currently in existance
        #self.mode_test_1()
        #self.test_photo_db_1()

        # self.mode_test_for_dev_1()
        #self.mode_raw_decade_scan(  )

        return

    # ---- --->> Methods to set up modes
    # -------
    def mode_example( self ):
        """
        an example and test mode for use in development
        """
        self.mode               = "mode_example"


# ---- methods not changed for different modes

# ----------------- tweaks changes for all modes for an os or computer name, to be used with other modes

    def __init__(self,   ):

        AppGlobal.parameters       = self

        # ---------  os platform... ----------------
        self.default_config()
        self.os_tweaks( )
        self.computer_name_tweaks()
        self.choose_mode()
        #rint( f"{self}")

    # -------
    def os_tweaks( self ):
        """
        tweak the default settings of "default_ _mode"
        for particular operating systems
        you may need to mess with this based on your os setup
        """
        if  self.os_win:
            pass
            #self.icon               = r"./clipboard_b.ico"    #  greenhouse this has issues on rasPi
            #self.icon              = None                    #  default gui icon

        else:
            pass

    # -------
    def computer_name_tweaks( self ):
        """
        this is an subroutine to tweak the default settings of "default_mode"
        for particular computers.  Put in settings for you computer if you wish
        these are for my computers, add what you want ( or nothing ) for your computes
        """
        print(self.computername, flush=True)

        if self.computername == "smithersxx":
            self.win_geometry       = '1250x1000+20+20'      # width x height position
            self.ex_editor          =  r"D:\apps\Notepad++\notepad++.exe"    # russ win 10 smithers

        elif self.computername == "millhousexx":
            self.ex_editor          =  r"C:\apps\Notepad++\notepad++.exe"    # russ win 10 millhouse
            self.win_geometry       = '1000x700+250+5'          # width x height position
#            self.pylogging_fn       = "millhouse_clipboard.py_log"   # file name for the python logging

    # -------
    def default_config( self ):
        """
        Purpose:
            set up default mode so all parms have at least an assignment
            read it
        """
        self.mode       = "default_mode"    # name of the mode of the app
        our_os          = sys.platform

        if our_os == "win32":
            self.os_win = True
        else:
            self.os_win = False

        self.platform           = our_os

        self.computername       = ( str( os.getenv( "COMPUTERNAME" ) ) ).lower()

        # ---- application primay purpose
        self.default_search_string         = "enter search string here"
        # what it says, the default search string
        self.search_lists                  = {}    # appeare in gui dropdown


        # list of web searches by name ( web_searcher.search_name )

        #---------
        search_name                        = "Shoping example list"
        search_site_list                   =  [ "Amazon",
                                                "Bangg",
                                               ]

        self.search_lists[ search_name ]   = search_site_list

        # #---------
        # search_name                        = "test"
        # search_site_list                   =  [
        #                                        "china",
        #                                        ]

        # self.search_lists[ search_name ]   = search_site_list

        self.search_site_list              =  search_site_list

        self.more_search_objects           = ["search_object_p1"]   # a list of modules with additional search objects

        # ---- appearance
        #self.title              = "File Finder for Dups"   # window title  !! drop for name version

        self.icon               = r"red_search.ico"       # icon for the app

        self.id_color           = "yellow"                # ?? not implementd

        # width x height position  x, y
        self.win_geometry       = '1500x800+20+20'
        self.win_geometry       = '900x600+700+230'
        self.win_geometry       = '1400x1000+20+20'

        # self.gui_style          = "windows"

        self.default_scroll     = True                   # check box on message widow
        self.max_lines          = 2_000                  # max line in message window

        # ---- logging
        self.pylogging_fn       = "web_search.py_log"    # file name for the python logging
        self.logging_level      = logging.DEBUG          # logging level DEBUG will log all catured text !
        self.logging_level      = logging.INFO
        self.logger_id          = "ws"                   # id in logging file

        self.gui_text_log_fn    = False    # "gui_text.log"       a file name or something false
        self.log_gui_text       = False    # True or false to log text
        self.log_gui_text_level = 10       # logging level for above

        # ------------- file names -------------------
        # this is the name of a program: its executable with path inof.
        # to be used in opening an external editor
        self.ex_editor         =  r"D:\apps\Notepad++\notepad++.exe"    # russ win 10

        self.help_fn            = "help.txt"
        #self.help_fn            = "https://opencircuits.com/index.php?title=Delete_Duplicates_Help_File"

        self.readme_fn          = "readme_rsh.txt"   # or None to supress in gui

    # -----------------------------------
    def __str__( self,   ):
        """
        this is informal, just for debugging
        sometimes it is hard to see where values have come out this may help if printed.
        not complete, add as needed -- compare across applications
        this copied from smart_terminal, commented out items might be good to use here or not
        """
        line_begin  ="\n"
        a_str = ""
        a_str = f"{a_str}\n>>>>>>>>>>* Parameters (some) *<<<<<<<<<<<<"
        a_str = f"{a_str}{line_begin}   mode                         {self.mode}"

        # ------------------------------+----------------------------+--------------------

        a_str = f"{a_str}{line_begin}   ex_editor                    {self.ex_editor}"
        a_str = f"{a_str}{line_begin}   logger_id                    {self.logger_id}"
        a_str = f"{a_str}{line_begin}   logging_level                {self.logging_level}"
        # ------------------------------+----------------------------+--------------------
        a_str = f"{a_str}{line_begin}   --- appearance ---"
        a_str = f"{a_str}{line_begin}   icon                         {self.icon}"
        a_str = f"{a_str}{line_begin}   win_geometry                 {self.win_geometry}"
        # a_str = f"{a_str}{line_begin}   win_max                  {self.win_max}"
        # ------------------------------+----------------------------+--------------------
        a_str = f"{a_str}{line_begin}   default_scroll               {self.default_scroll}"
        a_str = f"{a_str}{line_begin}   id_color                     {self.id_color}"
        #a_str = f"{a_str}{line_begin}   id_height                    {self.id_height}"

        # a_str = f"{a_str}\n   --- running on ---"
        # a_str = f"{a_str}\n   computername             {self.computername}"
        # a_str = f"{a_str}\n   our_os                   {self.our_os}"
        # ------------------------------+----------------------------+--------------------
        #a_str = f"{a_str}{line_begin}   --- misc ---"
        #a_str = f"{a_str}{line_begin}   self.running_on.computer_id  {self.running_on.computer_id}"

        a_str = f"{a_str}{line_begin}   --- logging  ---"
        # a_str = f"{a_str}{line_begin}   comm_logging_fn          {self.comm_logging_fn}"
        a_str = f"{a_str}{line_begin}   pylogging_fn                 {self.pylogging_fn}"
        a_str = f"{a_str}{line_begin}   self.ex_editor               {self.ex_editor}"

        a_str = f"{a_str}{line_begin}   --- file name related  ---"
        # a_str = f"{a_str}{line_begin}   file_out_ext_default         {self.file_out_ext_default}"
        # a_str = f"{a_str}{line_begin}   file_in_ext_default          {self.file_in_ext_default}"

        # a_str = f"{a_str}{line_begin}   file_bak_default             {self.file_bak_default}"

        # a_str = f"{a_str}{line_begin}   db_file_name                 {self.db_file_name}"
        # a_str = f"{a_str}{line_begin}   db_table_name                {self.db_table_name}"
        # a_str = f"{a_str}{line_begin}   file_out_scan_tags           {self.file_out_scan_tags}"

        # ------------------------------+----------------------------+--------------------
        # a_str = f"{a_str}{line_begin}   --- clean options ---"
        # a_str = f"{a_str}{line_begin}   self.clean_add_file          {self.clean_add_file}"
        # a_str = f"{a_str}{line_begin}   self.clean_convert_tags      {self.clean_convert_tags}"

        # ------------------------------+----------------------------+--------------------

        a_str = f"{a_str}\n   and so much more.... \n\n"
        return a_str

# =================================================

if __name__ == "__main__":

    import  web_search
    web_search.main( )


# =================== eof ==============================





