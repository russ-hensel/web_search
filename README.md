This application enables key word search of many web sites with just
a little typing and a few clicks.

Web sites to be searched can be set up in collections of either "lists", or
"groups".  Each individual site to be searched is setup via an object
called a "web searcher", each web searcher is given a mnemonic name, for example
"lime" might be given to a web searcher that searches "lime torrents".

    *lists:
        are named and specified in the parameter file of the application, you can
        set up pretty much any ( reasonably finite ) number of lists as
        you want. ( I have found groups more useful, only have one list now
        -- as an example of how it is done )

    *groups:
        when a searcher is defined it is assigned to a list of groups, just string
        names that define the groups.  You can have as many groups ( rf ) as you want
        and a searcher may belong to as many ( rf ) groups as you want.

Running the app:

    Start it, type in some search words, select either a list of web searchers ( via dropdown )
    or a set of groups ( via check boxes ). and press button <Search Web>

    Hint:
        before pressing <Search Web> you may wish to open a new empty web browser window
        ( in you default browser ) each web search will ( in Firefox anyway ) open in
        a new tab of that window.

Configuration:

    This involves coding!  Parameter are in parameters.py see the file and also: tbd

    To add new searches add to: search_objects_p1.py ( directions in file )

    If you want more search configuration file, build ones like search_objects_p1.py
    and modify the parameter:  self.more_search_objects

Installation:
    No installation, I run out of my development environment, just the
    directory web_searcher.  Run and discover modules are missing, installation
    and try again.  If I had a requirement.txt it might have something like:

        collections
        logging
        os
        pathlib
        psutil
        pyperclip
        subprocess
        sys
        tkinter
        tkinter.ttk
        webbrowser

The application is all Python, with a tinker.ttk user interface.

Guide to Files:
    Also see doc at top of each file.

    gui.py                          the apps gui
    help.txt                        this file
    main.py                         run the app, easy to find, little content
    parameters.py                   parameters or configuration for app
    readme_rsh.txt                  my developer notes to me
    red_search.ico                  app icon
    search.png                      another app icon
    search_object_p1.py             web searcher configured by parameters
    search_objects.py               base set of web_searchers
    web_search.py                   main module for the app
    web_search.py_log               log file for app, if missing first run
                                    of app will generate one
    app_global.py                   global variable support for app
    running_on.py                   environment introspection for parameters

