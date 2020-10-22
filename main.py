import datetime
import time

import tweepy
from tweepy import OAuthHandler
from plyer import notification

import settings

auth = OAuthHandler(settings.CONSUMER_KEY, settings.CONSUMER_SECRET)
auth.set_access_token(settings.ACCESS_TOKEN, settings.ACCESS_SECRET)

api = tweepy.API(auth)

words = ["GitHub", "AWS", "Slack", "障害"]
lower_words = list(map(str.lower, words))

print("Start monitoring trends")

while True:

    now = datetime.datetime.now().strftime("%Y/%m/%d %H:%M")

    trends = api.trends_place(23424856)[0]["trends"]

    for i, trend in enumerate(trends):

        rank = i + 1
        lower_name = str.lower(trend["name"])

        if lower_name in lower_words:
            print(f"{now} [{rank}位] {trend['name']}")

            notification.notify(
                title=f"{trend['name']}",
                message=f"{rank}位",
            )

    time.sleep(60)
