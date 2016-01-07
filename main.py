# -*- coding: utf-8 -*-
import urllib2
import xmltodict

from IPython import embed
from IPython.terminal.embed import InteractiveShellEmbed

def yomilen(string):
  urlstr = urllib2.quote(string.encode("utf-8"))
  response = urllib2.urlopen('http://jlp.yahooapis.jp/FuriganaService/V1/furigana?appid=dj0zaiZpPU1MQ05FZHpYRzBGTiZzPWNvbnN1bWVyc2VjcmV0Jng9YzM-&sentence='+urlstr).read()
  jres = xmltodict.parse(response)
  yomigana = ""
  if isinstance(jres["ResultSet"]["Result"]["WordList"]["Word"], list):
    for result in jres["ResultSet"]["Result"]["WordList"]["Word"]:
      yomigana = yomigana + result["Furigana"]
  else:
    yomigana = jres["ResultSet"]["Result"]["WordList"]["Word"]["Furigana"]
  length = len(yomigana)
  return length

def senryu(string):
  strs = string.split(" ")
  if len(strs) == 3:
    if yomilen(strs[0]) == 5:
      if yomilen(strs[1]) == 7:
        if yomilen(strs[2]) == 5:
          print u"川柳です"
          return True
        else:
          print u"3句目が5ではありません"
          return False
      else:
        print u"2句目が7ではありません"
        return False
    else:
      print u"1句目が5ではありません"
      return False
  else:
    print u"575ではありません"
    return False
embed()
