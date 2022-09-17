#!/usr/bin/python3
def search_replace(my_list, search, replace):
    return (my_list.translate({ord(i): replace for i in 'search'}))
