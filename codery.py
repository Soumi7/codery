# See readme.md for instructions on running this code.
import logging
from urllib import parse

import requests

from bs4 import BeautifulSoup

from typing import Dict, Any, Union, List

def google_search(keywords: str) -> List[Dict[str, str]]:
    query = {'q': keywords}
    # Gets the page
    page = requests.get('https://www.hackerearth.com/challenges', params=query)
    # Parses the page into BeautifulSoup
    #soup = BeautifulSoup(page.text, "lxml")

    

    # Gets all search URLs
    anchors = soup.find(id='search').findAll('a')
    results = []

    for a in anchors:
        try:
            # Tries to get the href property of the URL
            link = a['href']
        except KeyError:
            continue
        # Link must start with '/url?', as these are the search result links
        if not link.startswith('/url?'):
            continue
        # Makes sure a hidden 'cached' result isn't displayed
        if a.text.strip() == 'Cached' and 'webcache.googleusercontent.com' in a['href']:
            continue
        # a.text: The name of the page
        result = {'url': "https://www.google.com{}".format(link),
                  'name': a.text}
        results.append(result)
    return results

def get_google_result(search_keywords: str) -> str:
    help_message = "*Help for Codery bot* :robot_face: : \n\n" \
                   "The bot responds to messages starting with @codery-bot.\n\n" \
                   "`@codery-bot <search contests>` will return top Contests for the given `<search term>`.\n" \
                   "`@codery-bot top <search terms>` also returns the top Contest result.\n" \
                   "`@codery-bot list <search terms>` will return a list of contests for the given <search term>.\n \n" \
                   "Example:\n" \
                   " * @codery-bot funny cats\n" \
                   " * @codery-bot list funny dogs"

    

    search_keywords = search_keywords.strip()

    if search_keywords == 'help':
        return help_message
    elif search_keywords =='contests':
        

        URL = 'https://www.stopstalk.com/contests'


        page = requests.get(URL)
        content = requests.get(URL)
        soup = BeautifulSoup(content.text, 'html.parser')
        contentTable  = soup.find('table', { "class" : "centered bordered"}) # Use dictionary to pass key : value pair
        rows  = contentTable.find_all('tr')
        l=""
        for row in rows:
            l+=row.get_text()
        return l

    elif search_keywords == '' or search_keywords is None:
        return help_message
    else:
        try:
            results = google_search(search_keywords)
            if (len(results) == 0):
                return "Found no results."
            return "Found Result: [{}]({})".format(results[0]['name'], results[0]['url'])
        except Exception as e:
            logging.exception(str(e))
            return 'Error: Search failed. {}.'.format(e)

class GoogleSearchHandler(object):
    '''
    This plugin allows users to enter a search
    term in Zulip and get the top URL sent back
    to the context (stream or private) in which
    it was called. It looks for messages starting
    with @codery-bot.
    '''

    def usage(self) -> str:
        return '''
            This plugin will allow users to search
            for a given search term on Google from
            Zulip. Use '@mentioned-bot help' to get
            more information on the bot usage. Users
            should preface messages with
            @codery-bot.
            '''

    def handle_message(self, message: Dict[str, str], bot_handler: Any) -> None:
        original_content = message['content']
        result = get_google_result(original_content)
        bot_handler.send_reply(message, result)

handler_class = GoogleSearchHandler