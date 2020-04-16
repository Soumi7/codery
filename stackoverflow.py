import requests
import logging
import re
import urllib

from typing import Optional, Any, Dict

# See readme.md for instructions on running this code.
'''

class StackOverflowHandler(object):
    
    This plugin facilitates searching Stack Overflow for a
    specific query and returns the top 3 questions from the
    search. It looks for messages starting with '@mention-bot'

    In this example, we write all Stack Overflow searches into
    the same stream that it was called from.
    
'''
    

def get_stackoverflow_response(content, bot_handler: Any) -> Optional[str]:

    help_text = 'Please enter your query after @codery-bot to search StackOverflow'


    query = content
    if query == '' or query == 'help':
        return help_text

    query_stack_url = 'http://api.stackexchange.com/2.2/search/advanced'
    query_stack_params = dict(
        order='desc',
        sort='relevance',
        site='stackoverflow',
        title=query
    )
    try:
        data = requests.get(query_stack_url, params=query_stack_params)

    except requests.exceptions.RequestException:
        logging.error('broken link')
        return 'Uh-Oh ! Sorry ,couldn\'t process the request right now.:slightly_frowning_face:\n'             

        
    if data.status_code != 200:
        logging.error('Page not found.')
        return 'Uh-Oh ! Sorry ,couldn\'t process the request right now.:slightly_frowning_face:\n' 
        new_content = 'For search term:' + query + '\n'

        # Checking if there is content for the searched term
    if len(data.json()['items']) == 0:
        new_content = 'I am sorry. The search term you provided is not found :slightly_frowning_face:'
    else:
        for i in range(min(3, len(data.json()['items']))):
            search_string = data.json()['items'][i]['title']
            link = data.json()['items'][i]['link']
            new_content += str(i+1) + ' : ' + '[' + search_string + ']' + '(' + link + ')\n'
    return new_content

