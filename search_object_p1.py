# -*- coding: utf-8 -*-
"""
example extension configurable through parameters


for each search you want to conduct you need to construct a
WebSearcher
and add it to the
web_server_collections
as show below

see the code below for an explination of each attribute in the WebSearcher you
construct.

    generally it is best to go to the site, run a search on a couple of words, and
    then copy back that url for reference.




"""


import search_objects
from   app_global import AppGlobal

AppGlobal.controller.web_server_collections

#rint( f"_p1.............................................")



web_searcher_colletions   = AppGlobal.controller.web_server_collections

# ---- construct and add a new web searcher

# model search url"
#      https://www.instructables.com/search/?q=hose%20repair&projects=all
#     https://www.instructables.com/
a_searcher         =  search_objects.WebSearcher(
                                search_name   = "Instructables",
                                # a name or nick name if you wish for each search, use something you find
                                # meaningfull or menomic for yourself, has no other function


                                base_url      = "https://www.instructables.com/search/?q=",
                                # a string to begin to build a web search url -- see model search above

                                url_join_1    = "%20",
                                # a connector to join the search words together, see model to determin what it is
                                # here by inspection it is a -

                                url_1to2      = "",
                                # a connector between the first set of words and second, if "" then there is
                                # no second set of words

                                url_join_2    = "",  # "" suppress second search

                                url_suffix    = "&projects=all", # suffix at end of search url

                                url_home      = "https://www.instructables.com/",
                                # the home url of the site, not used in the search, perhap not used at all so far

                                group_list    = ["HowTo", "Electronics",     ]
                                # groups the searcher belongs to

                                )

web_searcher_colletions.add_to_web_searcher_dict( a_searcher )


# =============================== eof ========================


