# -*- coding: utf-8 -*-
#! /usr/bin/python3
#!python3
# above for windows ??
#     /usr/bin/python


"""
main module for the web_search app

"""

import os
import logging
import sys
import importlib
import time
import datetime


#----- local imports

sys.path.append( "../rshlib" )  # just for rsh, harmless unless the directory
                                # exists on your computer, safe to delete it

import parameters
import gui
from   app_global import AppGlobal
import search_objects

# ------------------------------
def   print_uni( a_string_ish ):
    """
    print even if unicode char messes it conversion
    maybe doing as a call is over kill
    """
    print(  a_string_ish.encode( 'ascii', 'ignore') )

# ============================================
class App(  ):
    """
    this class is the "main" or controller for the whole app
    to run see end of this file
    it is the controller of an mvc app
     """
    def __init__( self, ):
        """
        usual init for main app
        """
        self.app_name          = "WebSearch"
        self.app_version       = "Ver 4:  2023_05_22.01"
        AppGlobal.controller   = self
        self.gui               = None
        #self.sort_list         = None   # create later may not be a list
        self.restart_count     = -1     # count from 0
        self.logger            = None   # for access in rest of class?
        AppGlobal.logger       = None

    # ----------------------------------
    def restart(self ):
        """
        use to restart the app without ending it
        this can be very quick
        """
        self.restart_count   += 1
        print( f"========= restart {self.app_name}: restart = {self.restart_count} =================" )
            # not logged until it is turned on
        if not self.gui is None:
            self.gui.root.destroy()
            importlib.reload( parameters )    # should work on python 3 but sometimes does not

        else:
            #self.q_to_splash -- splash not implemented
            pass

        self.parameters     = parameters.Parameters( )

        self.config_logger()
        self.prog_info()

        self.web_server_collections   = search_objects.WebSearcherColletions()

        for i_module in self.parameters.more_search_objects:
            # import search_object_p1    # !! fix me

            #importlib.import_module( search_object_p1 )

            print( f"work on import of {i_module}")

            #importlib.import_module( i_module )

            #if self.restart_count == 0:

            # some not working but some doc says should
            #spam = __import__( 'search_object_p1', globals(), locals(), [], 0)
            #importlib.import_module( "search_object_p1", )
            #importlib.import_module( "search_object_p1", "./" )
            #importlib.import_module( i_module )
            # this does work ->>>
            exec_me     = f"import {i_module} "
            print( exec_me )
            exec( exec_me, globals(), locals() )

            #else:
                # would like test so done only if necessary
            exec_me     = f"importlib.reload( {i_module} )"
            print( exec_me )
            exec( exec_me, globals(), locals() )
            # importlib.reload( i_module )

        self.gui      = gui.GUI( self )

        msg           = ("Error messages may be in log file, check it "
                         "if problems -- check parameters.py for logging level " )
        #rint( msg )
        AppGlobal.print_debug( msg )
        self.logger.log( AppGlobal.fll, msg )

        self.starting_dir       = os.getcwd()    # or perhaps parse out of command line
        #self.gui.root.after( self.polling_delta, self._polling_0_ )

        self.search_obj_list      = self.web_server_collections.build_web_searcher_list_from_names(
                                        self.parameters.search_site_list )

        #Make the window jump above all
        self.gui.root.attributes( '-topmost', True  )
        self.gui.root.attributes( '-topmost', False )
        self.gui.root.mainloop()

        self.logger.info( self.app_name + ": all done" )

    # ------------------------------------------
    def config_logger( self, ):
        """
        create/configure the python logger
        """
        AppGlobal.logger_id     = "App"
        logger                  = logging.getLogger( AppGlobal.logger_id )
        logger.handlers         = []

        logger.setLevel( self.parameters.logging_level )

        # create the logging file handler
        fh = logging.FileHandler( self.parameters.pylogging_fn )

        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)

        logger.addHandler(fh)

        logger.info( "Done config_logger .. next AppGlobal msg" )
        #rint( "configed logger", flush = True )
        self.logger      = logger   # for access in rest of class?
        AppGlobal.logger = logger

        msg  = ( f"Message from AppGlobal.print_debug >> "
                 f"logger level in App = {self.logger.level} will show at level 10" )
        AppGlobal.print_debug( msg )

    # --------------------------------------------
    def prog_info( self,  ):
        """
        ?? consider gui display or with button
        """
        #logger_level( "util_foo.prog_info"  )
        fll         = AppGlobal.force_log_level
        logger      = self.logger
        logger.log( fll, "" )
        logger.log( fll, "============================" )
        logger.log( fll, "" )
        title       =  ( f"Application: {self.app_name} {AppGlobal.parameters.mode}"
                         f"  {self.app_version}" )
        logger.log( fll, title )
        logger.log( fll, "" )

        if len( sys.argv ) == 0:
            logger.info( "no command line arg " )
        else:
            for ix_arg, i_arg in enumerate( sys.argv ):
                msg = f"command line arg + {str( ix_arg ) }  =  { i_arg })"
                logger.log( AppGlobal.force_log_level, msg )

        logger.log( fll, f"current directory {os.getcwd()}"  )

        start_ts     = time.time()
        dt_obj       = datetime.datetime.utcfromtimestamp( start_ts )
        string_rep   = dt_obj.strftime('%Y-%m-%d %H:%M:%S')
        logger.log( fll, "Time now: " + string_rep )
        # logger_level( "Parameters say log to: " + self.parameters.pylogging_fn )
        # parameters and controller not available can get from logger_level

    #----------------- call backs  cb and bcb's ----------------------

    # ----------------------------------------------
    def cb_search( self,  ):
        """
        call back function
        what it says, read, search on name
        """
        if  self.gui.use_what_var.get() == self.gui.use_group_rb:   # move to gui in part
            #rint( "use group search" )

            selected_group_list   = self.gui.get_group_names()
            #rint( selected_group_list )

            search_obj_name_list      = self.web_server_collections.build_web_searcher_list_from_groups( selected_group_list )
            search_obj_list           = self.web_server_collections.build_web_searcher_list_from_names(  search_obj_name_list)

        else:
            #rint( "use list search in debug mode" )
            #debug_search_obj_list  = self.search_obj_list
            search_obj_list        = self.search_obj_list

        search_string          = self.gui.search_words_var.get( )
        msg       = "Searching using the following urls..."
        self.display_in_gui( msg )
        for i_search_obj in search_obj_list:
            url       = i_search_obj.create_search_url( search_string )
            msg       = f"    {url}"
            self.display_in_gui( msg )

            i_search_obj.run_search_url( url )

        self.gui.minimize( )

    # ----------------------------------------------
    def cb_show_search( self,  ):
        """
        call back function
        what it says, read, search on name
        """
        if  self.gui.use_what_var.get() == self.gui.use_group_rb:   # move to gui in part
            #rint( "use group search" )

            selected_group_list   = self.gui.get_group_names()
            #rint( selected_group_list )

            search_obj_name_list      = self.web_server_collections.build_web_searcher_list_from_groups( selected_group_list )
            search_obj_list           = self.web_server_collections.build_web_searcher_list_from_names(  search_obj_name_list)

            #rint( f"search_obj_list >>>>> {search_obj_list}" )

        else:
            #rint( "use list search in debug mode" )

            search_obj_list        = self.search_obj_list

        search_string          = self.gui.search_words_var.get( )

        msg       = "Search would use the following urls..."
        self.display_in_gui( msg )
        for i_search_obj in search_obj_list:
            #rint( ">>>>>>>" )

            url       = i_search_obj.create_search_url( search_string )
            msg       = f"    {url}"
            self.display_in_gui( msg )

    # ----------------------------------------------
    def cb_test( self,  ):
        """
        used as callback from gui button
        test method only in development
        """
        self.cb_search()

   # ----------------------------------------------
    def display_list_in_gui( self, a_list ):
        """
        so short inline it ??
        probably move to gui
        """
        for i_line in a_list:
            self.display_in_gui( f"    {i_line}"  )

    # ----------------------------------------------
    def null_method( self,  ):
        """
        used as callback from gui button resolve deleted methods
        """
        print("call to null_method")

    # ----------------------------------------------
    def os_open_logfile( self,  ):
        """
        used as callback from gui button
        """
        AppGlobal.os_open_txt_file( self.parameters.pylogging_fn )

    # ----------------------------------------------
    def os_open_readme( self,  ):
        """
        used as callback from gui button
        """
        AppGlobal.os_open_txt_file( self.parameters.readme_fn  )

    # ----------------------------------------------
    def os_open_parmfile( self,  ):
        """
        used as callback from gui button
        """
        a_filename = self.starting_dir  + os.path.sep + "parameters.py"
        AppGlobal.os_open_txt_file( a_filename )

    # ----------------------------------------------
    def os_open_help( self,  ):
        """
        used as callback from gui button
        """
        AppGlobal.os_open_help_file( self.parameters.help_fn )

    # ----------------------------------------------
    def build_search_list( self, key ):
        """
        what it says
        make a new search list based on ddl
        """
        search_site_list  = self.parameters.search_lists[key]

        msg  = f"search sites set to: {search_site_list}"
        self.display_in_gui( msg )

        self.search_obj_list      = self.web_server_collections.build_web_searcher_list_from_names( search_site_list )

   # ----------------------------------------------
    def display_in_gui( self, a_string ):
        """
        what it says

        """
        self.gui.write_gui( a_string )

# ----------------------------------------------
def main():
    """
    what it says, read
    """
    a_app = App( )

    if True:
        a_app.restart()
    else:

        try:
            a_app.restart()
        except Exception as exception:
            if a_app.logger is None:
                msg   = "exception in __main__ run the app -- it will end -- logger still None "
                print( msg )
            else:
                msg   = "exception in __main__ run the app -- it will end -- see logger "
                print( msg )
                a_app.logger.critical( msg )
                a_app.logger.critical( exception,  stack_info=True )
                    # just where I am full trace back most info
                raise
        finally:
            print( "here we are done with app", flush = True )
    #        sys.stdout.flush()

# ------------------
# ==============================================
if __name__ == '__main__':
    """
    run the app here, for convenience of launching
    """
    main(  )

# ======================= eof =======================

