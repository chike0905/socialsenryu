# -*- coding: utf-8 -*-
import urllib2
import xmltodict

from IPython import embed
from IPython.terminal.embed import InteractiveShellEmbed

def yomilen(string):
  urlstr = urllib2.quote(string.encode("utf-8"))
  response = urllib2.urlopen('http://jlp.yahooapis.jp/FuriganaService/V1/furigana?appid=dj0zaiZpPU1MQ05FZHpYRzBGTiZzPWNvbnN1bWVyc2VjcmV0Jng9YzM-&sentence='+urlstr).read()
  jres = xmltodict.parse(response)
  length = len(jres["ResultSet"]["Result"]["WordList"]["Word"]["Furigana"])
  return length

embed()
