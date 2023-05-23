# -*- coding: utf-8 -*-
"""

create the web searchers for the app



consider
     tubi
     peacock
     roku
     Freevee
     Roku Channel
     Crackle
     Sling Freestream   The best free streaming service for watching classic shows


     Vudu  The best free streaming service for watching popular movies


    Xumo the best free streaming service for live news and sports

    Peacock The best free streaming service for TV shows

    The 47 Best Free Online Movie Streaming Sites in April 2023
    https://privacysavvy.com/geoblocking/streaming/free-streaming-sites-for-movies-tv-shows/

"""

# =================================================

if __name__ == "__main__":

    import  web_search
    web_search.main( )

    # a_web_searcer    = WebSearcher( )
    # build_web_searcher_dict()



import webbrowser



# ----------------------
class WebSearcherColletions( ):
    """
    About this class.....
    """
    #----------- init -----------
    def __init__( self, ):
        """
        init to keep colletions and methods on them - of websearchers

        """
        # next two should be variables constant for a run of the app after init
        self.web_searcher_dict          = {}
        self._build_web_searcher_dict( )

        self.web_searcher_groups        = {}
        self._build_web_searcher_groups()

        #rint( f"self.web_searcher_groups  {self.web_searcher_groups}"   )

    #--------------------
    def add_to_web_searcher_dict( self, a_web_searcher  ):
        """
        what it says

        """
        self.web_searcher_dict[ a_web_searcher.search_name ]  = a_web_searcher

    #--------------------
    def _build_web_searcher_dict( self  ):
        """
        what it says
        build the universe of searchers ... other in modules like search_objects_p1
        """
        web_searcher_dict       =     self.web_searcher_dict

        # -------- start here, un implemented list may be at top
        # ------- unimplemented
        # ---- https://www.justwatch.com/ph/tv-show/meteor-butterfly-sword/season-1


        # ---- implemented
        # ---- "https://www.limetorrents.to/search/all/",
        a_searcher         =  WebSearcher(
                                       search_name   = "Lime",
                                       base_url      = "https://www.limetorrents.to/search/all/",
                                       url_join_1    = " ",
                                       url_1to2      = "",
                                       url_join_2    = "",
                                       url_suffix    = "/",
                                       url_home      = "https://www.limetorrents.to",
                                       group_list    = ["Torrent", "Video",   ],
                                      )

        web_searcher_dict[ a_searcher.search_name ]  = a_searcher

        # ----  https://www.roku.com/whats-on/search?q=korean%20drama
        #https://www.roku.com/whats-on/search?q=star%20trek%20strange%20new%20worlds
        a_searcher         =  WebSearcher(
                                       search_name   = "Roku",
                                       base_url      = "https://www.roku.com/whats-on/search?q=",
                                       url_join_1    = " ",
                                       url_1to2      = "",
                                       url_join_2    = "",
                                       url_suffix    = "",
                                       url_home      = "https://www.roku.com",
                                       group_list    = [ "Video",   ],
                                      )

        web_searcher_dict[ a_searcher.search_name ]  = a_searcher

        # ----
        a_searcher         =  WebSearcher(
                                       search_name   = "netflix",
                                       base_url      = "https://www.netflix.com/search?q=",
                                       url_join_1    = " ",
                                       url_1to2      = "",
                                       url_join_2    = "",
                                       url_suffix    = "",
                                       url_home      = "https://www.netflix.com/",
                                       group_list    = [ "Video",  ],
                                      )
        web_searcher_dict[ a_searcher.search_name ]  = a_searcher

        # ----
        a_searcher         =  WebSearcher(
                                       search_name   = "Youtube",
                                       base_url      = "https://www.youtube.com/results?search_query=",
                                       url_join_1    = "+",
                                       url_1to2      = "",
                                       url_join_2    = "",
                                       url_suffix    = "",
                                       url_home      = "https://www.youtube.com/",
                                       group_list    = [ "Video", "Howto", "Python",    ],
                                      )
        web_searcher_dict[ a_searcher.search_name ]  = a_searcher

        # ----
        a_searcher         =  WebSearcher(
                                       search_name   = "Wpedia",
                                       base_url      = "https://en.wikipedia.org/w/index.php?search=+",
                                       url_join_1    = "+",
                                       url_1to2      = "",
                                       url_join_2    = "",
                                       url_suffix    = "+&title=Special%3ASearch&ns0=1",
                                       url_home      = "https://en.wikipedia.org",
                                       group_list    = [ "Search" ],
                                      )
        web_searcher_dict[ a_searcher.search_name ]  = a_searcher

        # ---- https://yourbittorrent.com/?q=korean-costume
        a_searcher         =  WebSearcher(
                                       search_name   = "Yourbit",
                                       base_url      = "https://yourbittorrent.com/?q=",
                                       url_join_1    = "-",
                                       url_1to2      = "",

                                       url_join_2    = "",
                                       url_suffix    = "",
                                       url_home      = "https://yourbittorrent.com",
                                       group_list    = ["Torrent", "Video"],
                                      )
        web_searcher_dict[ a_searcher.search_name ]  = a_searcher

        # ----  https://www.1377x.to/search/%20word%20another%20word%20too%20/1
        a_searcher         =  WebSearcher(
                                       search_name   = "1377",
                                       base_url      = "https://www.1377x.to/search/%20",
                                       url_join_1    = "%20",
                                       url_1to2      = "",
                                       url_join_2    = "",
                                       url_suffix    = "%20/1/",
                                       url_home      = "https://www.1377x.to/",
                                       group_list    = ["Torrent", "Video"],
                                      )
        web_searcher_dict[ a_searcher.search_name ]  = a_searcher

        # ---- https://katcr.to/usearch/word%20another%20word%20too/
        a_searcher         =  WebSearcher(
                                       search_name   = "katcr",
                                       base_url      = "https://katcr.to/usearch/",
                                       url_join_1    = "%20" ,
                                       url_1to2      = "",
                                       url_join_2    = "",
                                       url_suffix    = "/",
                                       url_home      = "https://katcr.to",
                                       group_list    = ["Torrent", "Video"],
                                      )

        web_searcher_dict[ a_searcher.search_name ]  = a_searcher

        # ----  https://idope.se/torrent-list/korean%20costume/
        a_searcher         =  WebSearcher(
                                   search_name   = "idope",
                                   base_url      = "https://idope.se/torrent-list/",
                                   url_join_1    = "%20",
                                   url_1to2      = "",

                                   url_join_2    = "",
                                   url_suffix    = "/",
                                   url_home      = "https://idope.se/",
                                   group_list    = [ "Torrent", "Video" ],
                                  )

        web_searcher_dict[ a_searcher.search_name ]  = a_searcher

        # ---- https://eztv.re/search/word-another-word-too
        a_searcher         =  WebSearcher(
                                   search_name   = "Eztv",
                                   base_url      = "https://eztv.re/search/",
                                   url_join_1    = "-",
                                   url_1to2      = "",
                                   url_join_2    = "",
                                   url_suffix    = "",
                                   url_home      = "https://eztv.re/",
                                   group_list    = [ "Torrent", "Video" ],
                                  )

        web_searcher_dict[ a_searcher.search_name ]  = a_searcher

        # ----         https://torrentgalaxy.to/torrents.php?search=korean+costume+drama&lang=0&nox=2#results
        a_searcher         =  WebSearcher(
                                   search_name   = "Torrentg",
                                   base_url      = "https://torrentgalaxy.to/torrents.php?search=",
                                   url_join_1    = "+",
                                   url_1to2      = "",
                                   url_join_2    = "",
                                   url_suffix    = "&lang=0&nox=2#results",
                                   url_home      = "https://torrentgalaxy.to",
                                   group_list    = [ "Torrent", "Video" ],
                                  )

        web_searcher_dict[ a_searcher.search_name ]  = a_searcher

        # ----  https://www.amazon.com/s?k=bluetooth+headphone   works
        a_searcher         =  WebSearcher(
                                   search_name   = "Amazon",
                                   base_url      = "https://www.amazon.com/s?k=",
                                   url_join_1    = "+",
                                   url_1to2      = "",
                                   url_join_2    = "",
                                   url_suffix    = "",
                                   url_home      = "https://www.amazon.com",
                                   group_list    = [ "Shop", "Electronics", "Video",   ],
                                  )
        web_searcher_dict[ a_searcher.search_name ]  = a_searcher

        # ---- https://www.banggood.com/search/tissue-box.html?from=nav&direct=0
        a_searcher         =  WebSearcher(
                                   search_name   = "Bangg",
                                   base_url      = "https://www.banggood.com/search/",
                                   url_join_1    = "-",
                                   url_1to2      = "",
                                   url_join_2    = "",
                                   url_suffix    = ".html?from=nav&direct=0",
                                   url_home      = "https://www.banggood.com",
                                   group_list    = [ "Shop", "Electronics" ],
                                  )
        web_searcher_dict[ a_searcher.search_name ]  = a_searcher

        # ---- https://www.google.com/search?tbm=shop&hl=en&psb=1&ved=2ahUKEwiYqouDjKX9AhWMD4gJHT55DEQQu-kFegQIABAR&q=tissue+box&oq=tissue+box
        a_searcher         =  WebSearcher(
                     search_name   = "Gshop",
                     base_url      = "https://www.google.com/search?tbm=shop&hl=en&psb=1&ved=2ahUKEwiYqouDjKX9AhWMD4gJHT55DEQQu-kFegQIABAR&q=",
                     url_join_1    = "+",
                     url_1to2      = "",
                     url_join_2    = "&oq=",
                     url_suffix    = "",
                     url_home      = "xxx",
                     group_list    = [ "Search", "Shop" ],
                    )
        web_searcher_dict[ a_searcher.search_name ]  = a_searcher

        # ---- https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2380057.m570.l1313&_nkw=tissue+box&_sacat=0
        a_searcher         =  WebSearcher(
                     search_name   = "Ebay",
                     base_url      = "https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2380057.m570.l1313&_nkw=",
                     url_join_1    = "+",
                     url_1to2      = "",
                     url_join_2    = "",
                     url_suffix    = "&_sacat=0",
                     url_home      = "https://www.ebay.com/",
                     group_list    = [ "Shop", "Electronics" ],
                    )
        web_searcher_dict[ a_searcher.search_name ]  = a_searcher

        # ----   works  https://www.aliexpress.com/w/wholesale-tissue-box-covers.html?catId=0&initiative_id=SB_20230220132913&SearchText=tissue+box+covers
        a_searcher         =  WebSearcher(
                     search_name   = "Alie_Express",
                     base_url      = "https://www.aliexpress.com/w/wholesale-",
                     url_join_1    = "-",
                     url_1to2      = ".html?catId=0&initiative_id=SB_20230220132913&SearchText=",
                     url_join_2    = "+",
                     url_suffix    = "",
                     url_home      = "https://www.aliexpress.com/",
                     group_list    = [ "Shop", "Electronics" ],
                    )
        web_searcher_dict[ a_searcher.search_name ]  = a_searcher

        # ---- https://www.imdb.com/wind and water
        a_searcher         =  WebSearcher(
                                   search_name   = "Imdb",
                                   base_url      = "https://www.imdb.com/find/?q=",
                                   url_join_1    = " ",
                                   url_1to2      = "",
                                   url_join_2    = "",
                                   url_suffix    = "",
                                   url_home      = "https://www.imdb.com/",
                                   group_list    = [ "Video", ],
                                  )
        web_searcher_dict[ a_searcher.search_name ]  = a_searcher

        # ----  https://duckduckgo.com/?q=best+korean+costume+dramas

        a_searcher         =  WebSearcher(
                                   search_name   = "DuckGo",
                                   base_url      = "https://duckduckgo.com/?q=",
                                   url_join_1    = "+",
                                   url_1to2      = "",
                                   url_join_2    = "",
                                   url_suffix    = "",
                                   url_home      =  "https://duckduckgo.com/",
                                   group_list    = [ "Search" ],
                                  )
        web_searcher_dict[ a_searcher.search_name ]  = a_searcher

        # ---- https://www.viki.com/search?q=best%20costume
        a_searcher         =  WebSearcher(
                                   search_name   = "Viki",
                                   base_url      = "https://www.viki.com/search?q=",
                                   url_join_1    = " ",
                                   url_1to2      = "",
                                   url_join_2    = "",
                                   url_suffix    = "",
                                   url_home      = "https://www.viki.com/",
                                   group_list    = [ "Video",  ],
                                  )
        web_searcher_dict[ a_searcher.search_name ]  = a_searcher

        # ---- https://www.ondemandchina.com/en/search?q=beautiful%20sister
        a_searcher         =  WebSearcher(
                                   search_name   = "ChinaVideo",
                                   base_url      = "https://www.ondemandchina.com/en/search?q=",
                                   url_join_1    = " ",
                                   url_1to2      = "",
                                   url_join_2    = "",
                                   url_suffix    = "",
                                   url_home      = "https://www.ondemandchina.com/en/",
                                   group_list    = [ "Video",   ],
                                  )
        web_searcher_dict[ a_searcher.search_name ]  = a_searcher

        # ---- https://www.iq.com/play/monkey-king-uproar-in-dragon-palace-2019-19rqvvh4ds?lang=en_us
        # https://www.iq.com/search?query=costume%20drama&originInput=costume%20drama

        a_searcher         =  WebSearcher(
                                   search_name   = "IqVideo",
                                   base_url      = "https://www.iq.com/search?query=",
                                   url_join_1    = "%20",
                                   url_1to2      = "&originInput=",
                                   url_join_2    = "%20",
                                   url_suffix    = "",
                                   url_home      = "https://www.iq.com",
                                   group_list    = [ "Video",  ],
                                  )
        web_searcher_dict[ a_searcher.search_name ]  = a_searcher

        # ---- xxx https://www.crackle.com/watch/24012835-27AA-4C43-A5D6-EC05FE854591  blocks add blockers

        a_searcher         =  WebSearcher(
                                   search_name   = "Crackle",
                                   base_url      = "https://www.crackle.com/search?term=",
                                   url_join_1    = "+",
                                   url_1to2      = "",
                                   url_join_2    = "",
                                   url_suffix    = "",
                                   url_home      = "https://www.crackle.com",
                                   group_list    = [  "Video", ],
                                  )
        web_searcher_dict[ a_searcher.search_name ]  = a_searcher

        # ---- xxx https://therokuchannel.roku.com/
        #   https://therokuchannel.roku.com/search/asian%20drama
        a_searcher         =  WebSearcher(
                                   search_name   = "Roku",
                                   base_url      = "https://therokuchannel.roku.com/search/",
                                   url_join_1    = "%20",
                                   url_1to2      = "",
                                   url_join_2    = "",
                                   url_suffix    = "",
                                   url_home      = "https://therokuchannel.roku.com/",
                                   group_list    = [ "Video"],
                                  )
        web_searcher_dict[ a_searcher.search_name ]  = a_searcher

        # ---- https://www.kocowa.com/en_us/profile   may need sign up, not much content
        #  https://www.kocowa.com/en_us/media/58720214/p1h-a-new-world-begins
        # https://www.kocowa.com/en_us/search?q=costume%20drama
        a_searcher         =  WebSearcher(
                                   search_name   = "Kocowa",
                                   base_url      = "https://www.kocowa.com/en_us/search?q=",
                                   url_join_1    = "%20",
                                   url_1to2      = "",
                                   url_join_2    = "",
                                   url_suffix    = "",
                                   url_home      = "https://www.kocowa.com",
                                   group_list    = [ "Video"],
                                  )
        web_searcher_dict[ a_searcher.search_name ]  = a_searcher

        # ----
        a_searcher         =  WebSearcher(
                                   search_name   = "Pirate_bay",
                                   base_url      = "https://thepiratebay.org/search.php?q=",
                                   url_join_1    = "+",
                                   url_1to2      = "",

                                   url_join_2    = "",
                                   url_suffix    = "&all=on&search=Pirate+Search&page=0&orderby=",
                                   url_home      = "https://thepiratebay.org",
                                   group_list    = [ "Torrent", "Video",    ],
                                  )
        web_searcher_dict[ a_searcher.search_name ]  = a_searcher

        return web_searcher_dict

    #------------------
    def _build_web_searcher_groups( self  ):
        """
        dict with group key to names in group ( or to searchers themselves ?? )
        after searchers are built
        !! change to poperty ??
        assign to self ?
        _ or not needed
        """
        web_searcher_dict          = self.web_searcher_dict

        web_searcher_groups        = {}

        for i_key, i_value in web_searcher_dict.items():
            # i_key is the name, value is the object

            for  i_group   in i_value.group_list:
                #rint( i_group )
                a_list    = web_searcher_groups.get( i_group, None )  # runtime eval or compile ??
                if a_list is None:
                    a_list = []
                    web_searcher_groups[ i_group ] = a_list
                a_list.append(  i_key )

        #  sort
        web_searcher_groups  = {a_key: a_value for a_key, a_value in
                                sorted( web_searcher_groups.items(), key = lambda item: item[0])}

        self.web_searcher_groups    = web_searcher_groups
        #rint( f"\nbuild_web_searcher_groups web_searcher_groups = {web_searcher_groups}" )
        return web_searcher_groups

    #------------------
    def build_web_searcher_list_from_groups( self, group_names = None  ):
        """
        names is a list of names of searchers
        quite possible to get dups, so we use a set to eliminate them
        Args:
            group_names    list of group name strings
        Return
            list like struct of names of web searchers
        """
        if group_names is None:
            group_names = []

        web_searcher_set  = set()

        # !! ?? list comp
        for i_group_name in group_names:

            search_names = self.web_searcher_groups[ i_group_name ]
            #rint( f"search_names {search_names}")
            for i_search_name in search_names:
                web_searcher_set.add( i_search_name )

        # !! consider sort and convert to list
        #self.web_searcher_list   = web_searcher_list
        #rint( web_searcher_set )
        web_searcher_list  = sorted( web_searcher_set, )  # implicet key....
        return web_searcher_list

    #------------------
    def build_web_searcher_list_from_names( self, names = None  ):
        """
        names is a list of names of searchers
        consider alpha sort
        """
        if names is None:
            names = []
        #rint( f"names>>>>>>>>>>>>>>>>>>>>>> {names}" )
        web_searcher_list  = []

        # !! ?? list comp
        for i_site in names:
            #rint( i_site, flush = True )
            web_searcher_list.append( self.web_searcher_dict[ i_site ]  )

        return web_searcher_list

    # --------------------------------------------------
    def __str__( self ):
        """
        the usual, read
        """
        line_begin  = "\n    "  # formatting aid

        a_str       =  ""
        a_str       = f"{a_str}\n>>>>>>>>>>* WebSearcherCollections()  needs to be written *<<<<<<<<<<<<"
        # a_str       = f"{a_str}{line_begin}search_name         >{self.search_name}<"
        a_str       = f"{a_str}{line_begin}web_searcher_dict        >{self.self.web_searcher_dict}<"
        a_str       = f"{a_str}{line_begin}web_searcher_groups      >{self.self.web_searcher_groups}<"
        # a_str       = f"{a_str}{line_begin}url_suffix          >{self.url_suffix}<"
        # a_str       = f"{a_str}{line_begin}url_join_1          >{self.url_join_1}<"
        # a_str       = f"{a_str}{line_begin}url_1to2            >{self.url_1to2}<"

        return a_str

# ---------------------
class WebSearcher( ):
    """
    About this class.....
    a web_searcher contains the info to search a single site and
    to run that search
    """
    #----------- init -----------
    def __init__( self,
                  search_name           = "",
                  base_url              = "",
                  url_join_1            = "",
                  url_1to2              = "",
                  url_join_2            = "",
                  url_suffix            = "",
                  url_home              = "",
                  group_list            = None,
                  search_description    = "",
                  ):

        # make a clipboard func for this ??
        self.search_name           = search_name
        self.base_url              = base_url
        self.url_suffix            = url_suffix
        self.url_join_1            = url_join_1
        self.url_1to2              = url_1to2
        self.url_join_2            = url_join_2
        self.url_suffix            = url_suffix
        self.url_home              = url_home
        self.group_list            = group_list
        self.search_description    = search_description

    # --------------------------------------------------
    def __str__( self ):
        """
        the usual, read
        """
        line_begin  = "\n    "  # formatting aid

        a_str       =  ""
        a_str       = f"{a_str}\n>>>>>>>>>>* WebSearcher()  *<<<<<<<<<<<<"
        a_str       = f"{a_str}{line_begin}search_name         >{self.search_name}<"
        a_str       = f"{a_str}{line_begin}search_description  >{self.search_description}<"
        a_str       = f"{a_str}{line_begin}url_home            >{self.url_home}<"
        a_str       = f"{a_str}{line_begin}base_url            >{self.base_url}<"
        a_str       = f"{a_str}{line_begin}url_suffix          >{self.url_suffix}<"
        a_str       = f"{a_str}{line_begin}url_join_1          >{self.url_join_1}<"
        a_str       = f"{a_str}{line_begin}url_1to2            >{self.url_1to2}<"
        #a_str       = f"{a_str}{line_begin}url_join            >{self.url_join}<"
        a_str       = f"{a_str}{line_begin}url_join_2          >{self.url_join_2}<"
        a_str       = f"{a_str}{line_begin}url_suffix          >{self.url_suffix}<"
        a_str       = f"{a_str}{line_begin}group_list          >{self.group_list}<"

        # a_str       = f"{a_str}{line_begin}arg3             >{self.arg3}<"
        # a_str       = f"{a_str}{line_begin}arg3             >{self.arg3}<"

        return a_str

    # --------------------------------------------------
    def create_search_url( self, search_string ):
        """
        use info on site and search string to construct the
        needed url for the search
        """
        #rint( search_string )
        search_string       = search_string.strip(   )
        search_words        = search_string.split( " " )
        new_search_words    = []

        for i_word in search_words:
            if i_word == "":
                pass
            else:
                new_search_words.append( i_word )

        search_words    = new_search_words
        #rint( search_words )

        search_word_url_1   =   self.url_join_1.join ( search_words )

        if self.url_join_2 != "":
            search_word_url_2   =  self.url_join_2.join ( search_words )

        else:
            search_word_url_2   = ""

        # base_url      = "https://www.limetorrents.to/search/all/"
        # base_url      = self.parameters.my_first_base_url

        if search_word_url_2   == "":
            url           = ( self.base_url + search_word_url_1 + self.url_suffix )
        else:
            url           = ( self.base_url + search_word_url_1 + self.url_1to2 +
                              search_word_url_2 + self.url_suffix )

        #rint( url )
        return url

    # --------------------------------------------------
    def run_search_url( self, url ):
        """
        the usual, read
        """
        #rint( "run_search_url" )
        webbrowser.open( url, new = 0, autoraise = True )

