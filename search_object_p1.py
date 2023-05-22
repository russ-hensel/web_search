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
#     https://www.limetorrents.to/search/all/word1-word2-word3/
#     https://www.limetorrents.to/search/all/bad-sisters/
a_searcher         =  search_objects.WebSearcher(
                                search_name   = "limetest",
                                # a name or nick name if you wish for each search, use something you find
                                # meaningfull or menomic for yourself, has no other function

                                #                https://www.limetorrents.to/search/all/bad-sisters/
                                base_url      = "https://www.limetorrents.to/search/all/",
                                # a string to begin to build a web search url -- see model search above

                                url_join_1    = "-",
                                # a connector to join the search words together, see model to determin what it is
                                # here by inspection it is a -

                                url_1to2      = "",
                                # a connector between the first set of words and second, if "" then there is
                                # no second set of words

                                url_join_2    = "",  # "" suppress second search

                                url_suffix    = "/", # suffix at end of search url

                                url_home      = "https://www.limetorrents.to",
                                # the home url of the site, not used in the search, perhap not used at all so far

                                group_list    = ["tester",     ],
                                # groups the searcher belongs to

                                )

web_searcher_colletions.add_to_web_searcher_dict( a_searcher )





