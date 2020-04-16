import sys, os
sys.path.insert(0,os.getcwd())

import requests
import json
from typing import Any,Dict,List

import logging
from urllib import parse

import requests

from bs4 import BeautifulSoup

from typing import Dict, Any, Union, List



def get_courses(content, bot_handler: Any) -> str:
	words = content.lower().split()
	print(words)
	courses = requests.get('https://www.udemy.com/api-2.0/courses/238934?fields[course]=title,headline').json()
	res = "" 
	res=courses["courses"]
	return res


