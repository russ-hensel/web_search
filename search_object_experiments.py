# -*- coding: utf-8 -*-
"""
Created on Mon Mar  6 09:53:24 2023

@author: russ
"""


import sys
import webbrowser
import collections
Constructor   = collections.namedtuple( 'Constructor',  "class_constructor dict_args" )   # name is first argument  --- second arg space sep or a tuple
# constructor constructs the search object
# an_example   = ThreeParts( index_1  = "aaa", index_2 = "bbb", index_3 = "ccc" )     # no quotes on instance names



class AWebSearcher( ):
    """
    About this class.....
    """
    #----------- init -----------
    def __init__x(self, a_dict ):
        """
        See class doc
        """

        self.search_name           = a_dict["search_name"]
        #self.search_class          = a_dict["search_class"]
        # see create_search_url
        self.base_url              = a_dict["base_url"]
        self.url_suffix            = a_dict["url_suffix"]
        self.url_join_1            = a_dict["url_join_1"]
        self.url_1to2              = a_dict["url_1to2"]
        self.url_join              = a_dict["url_join"]
        #self.url_join              = a_dict["url_join"]
        self.url_join_2            = a_dict["url_join_2"]
        self.url_suffix            = a_dict["url_suffix"]

    #----------- init -----------
    def __init__( self,
                  search_name    = "",
                  base_url       = "",
                  url_join_1     = "",
                  url_1to2       = "",
                  url_join       = "",
                  url_join_2     = "",
                  url_suffix     = "",
                  url_home       = ""
                  ):

        # make a clipboard func for this
        self.search_name           =  search_name
        self.base_url              =  base_url
        self.url_suffix            =  url_suffix
        self.url_join_1            =  url_join_1
        self.url_1to2              =  url_1to2
        self.url_join              =  url_join
        #self.url_join              =  url_join"]
        self.url_join_2            =  url_join_2
        self.url_suffix            =  url_suffix
        self.url_home              =  url_home


    # --------------------------------------------------
    def __str__( self ):
        """
        the usual, read
        """
        line_begin  = "\n    "  # formatting aid

        a_str       =  ""
        a_str       = f"{a_str}\n>>>>>>>>>>* AWebSearcher()  *<<<<<<<<<<<<"
        a_str       = f"{a_str}{line_begin}search_name         >{self.search_name}<"
        #a_str       = f"{a_str}{line_begin}search_class        >{self.search_class}<"
        a_str       = f"{a_str}{line_begin}base_url            >{self.base_url}<"
        a_str       = f"{a_str}{line_begin}url_suffix          >{self.url_suffix}<"
        a_str       = f"{a_str}{line_begin}url_join_1          >{self.url_join_1}<"
        a_str       = f"{a_str}{line_begin}url_1to2            >{self.url_1to2}<"
        a_str       = f"{a_str}{line_begin}url_join            >{self.url_join}<"
        a_str       = f"{a_str}{line_begin}url_join_2          >{self.url_join_2}<"
        a_str       = f"{a_str}{line_begin}url_suffix          >{self.url_suffix}<"


        # a_str       = f"{a_str}{line_begin}arg3             >{self.arg3}<"
        # a_str       = f"{a_str}{line_begin}arg3             >{self.arg3}<"


        return a_str


    # --------------------------------------------------
    def create_search_url( self, search_string ):
        """
        the usual, read
        """
        print( search_string )

        search_string       = search_string.strip(   )
        search_words        = search_string.split( " " )
        new_search_words    = []

        for i_word in search_words:
            if i_word == "":
                pass
            else:
                new_search_words.append( i_word )

        search_words    = new_search_words
        print( search_words )

        # search_words  = [ "word1", "word2ddddddd", "word5", "pinus" ]

        search_word_url_1   =   self.url_join_1.join ( search_words )

        if self.url_join_2 != "":
            search_word_url_2   =  self.url_join_2.join ( search_words )

        else:
            search_word_url_2   = ""

        # base_url      = "https://www.limetorrents.to/search/all/"
        # base_url      = self.parameters.my_first_base_url

        if search_word_url_2   == "":
            url           = self.base_url + search_word_url_1 + self.url_suffix
        else:

            url           = self.base_url + search_word_url_1 + self.url_1to2 +  search_word_url_2 + self.url_suffix

        print( url )

        # url           = f"{base_url}word1%20word2%20word3/"
        # url           = f"{base_url}{search_words[0]}%20{search_words[1]}%20{search_words[2]}/"
        # url    = "https://www.limetorrents.to/search/all/word1%20word2%20word3/"

        return url

    # --------------------------------------------------
    def run_search_url( self, url ):
        """
        the usual, read
        """
        print( "run_search_url" )
        webbrowser.open( url, new = 0, autoraise = True )


    # -----------------------------------
    def bar( self, ):
        """
        what it says, read
        """
        ret_val = 0
        return ret_val


# might do similar with an eval
# a dict with a tuple: constructor and dict of arguments
# a_dict_object   = {  "name":  ( AClass, {"arg1": "something for arg1"} ),
#                      "name2": ( AClass, {"arg1": "something"} ) }

# a_dict_object   = {  "name":  Constructor( class_constructor       = AWebSearcher,
#                                            dict_args               = {"arg1": "something for arg1",
#                                                                       "arg2": "something for arg2",
#                                                                       "arg3": "something for arg3", } ),
#                      "netflix": ( AWebSearcher, {"arg1": "something"} ) }


# ---- if objects are large keep a constructor_dict and make on demand
#      but if not why not make and store, for these objects second seems better option

def  test_ver_1():
    "build from dict"
    constructor_dict   = {  "netflix":  Constructor( class_constructor = AWebSearcher,
                                           dict_args               = {"search_name":  "netflix",
                                                                      "base_url":     "https://www.netflix.com/search?q=",
                                                                      "url_join_1":   " ",
                                                                      "url_1to2":     "",
                                                                      "url_join":     "",
                                                                      "url_join_2":   "",  # "" suppress second search
                                                                      "url_suffix":   "",
                                                                      "url_home":     "https://www.netflix.com/",

                                                                      } ),

                          "netflix2":  Constructor( class_constructor       = AWebSearcher,
                                           dict_args               = {"search_name":  "netflix2",
                                                                      "base_url":     "https://www.netflix.com/search?q=",
                                                                      "url_join_1":   " ",
                                                                      "url_1to2":     "",
                                                                      "url_join":     "",
                                                                      "url_join_2":   "",  # "" suppress second search
                                                                      "url_suffix":   "",
                                                                      "url_home":     "https://www.netflix.com/",

                                                                      } ),

                                                                   }

    # two step and a little less of nested ().,,

    a_constructor  = Constructor(
                          class_constructor       = AWebSearcher,
                      dict_args               = {"search_name":  "netflix3",
                                                 "base_url":     "https://www.netflix.com/search?q=",
                                                 "url_join_1":   " ",
                                                 "url_1to2":     "",
                                                 "url_join":     "",
                                                 "url_join_2":   "",  # "" suppress second search
                                                 "url_suffix":   "",
                                                 "url_home":     "https://www.netflix.com/",

                                                 } )

    constructor_dict[a_constructor.dict_args["search_name"]]  = a_constructor

    #print( a_dict_object )


               # obj                 = SearchObject_1( )
               # obj.search_name     = "netflix"
               # obj.base_url        = "https://www.netflix.com/search?q="
               # obj.url_join_1      = " "
               # obj.url_1to2        = ""
               # obj.url_join_2      = ""   # = "" to supress second search
               # obj.url_suffix      = ""
               # obj.url_home        = "https://www.netflix.com/"



    # construct by name
    a_construct     = constructor_dict[ "netflix3" ]
    # print( a_construct )
    # print( a_construct[0] )

    # make the call to construct
    a_search_obj    = a_construct[ 0 ]( a_construct[ 1] ) # construct object unnamed
    a_search_obj    = a_construct.class_constructor( a_construct.dict_args ) # construct object named


    print( a_search_obj )

    for key, value in constructor_dict.items():
        print( key, "\n", value, "\nn")

    # could just build all and keep in a dict, not keep all the construction info


def  test_ver_2():
    "build and save in dict"


    web_searcher_dict  = {}
    a_searcher         =  AWebSearcher(
                                   search_name   = "netflix",
                                   base_url      = "https://www.netflix.com/search?q=",
                                   url_join_1    = " ",
                                   url_1to2      = "",
                                   url_join      = "",
                                   url_join_2    = "",  # "" suppress second search
                                   url_suffix    = "",
                                   url_home      =      "https://www.netflix.com/",
                                  )

    print( a_searcher.search_name )
    web_searcher_dict[ a_searcher.search_name ]   = a_searcher

    print( web_searcher_dict[ "netflix" ] )

    print( f"sys.getsizeof( web_searcher_dict )      >>{sys.getsizeof( web_searcher_dict )}<<" )

test_ver_2()



