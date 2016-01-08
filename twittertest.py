# -*- coding: utf-8 -*-
import twitter
import twitkey
import json

from IPython import embed
from IPython.terminal.embed import InteractiveShellEmbed

#特定のツイートへのmentionを取得
#target = tweet id
def GetMentionToTweet(target):
  returns = []
  mentions = Api.GetMentions()
  for a in mentions:
    if a.in_reply_to_status_id == target:
      returns.append(a)
  return returns



CONSUMER_KEY = twitkey.twkey['cons_key']
CONSUMER_SECRET = twitkey.twkey['cons_sec']
ACCESS_TOKEN_KEY = twitkey.twkey['accto_key']
ACCESS_TOKEN_SECRET = twitkey.twkey['accto_sec']


Api = twitter.Api(consumer_key = CONSUMER_KEY,
    consumer_secret = CONSUMER_SECRET,
    access_token_key = ACCESS_TOKEN_KEY,
    access_token_secret = ACCESS_TOKEN_SECRET)



embed()
