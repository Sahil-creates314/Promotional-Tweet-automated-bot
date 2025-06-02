import tweepy
import os
import time
import random
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# === Twitter Keys from .env ===
api_key = os.getenv('TWITTER_API_KEY')
api_secret = os.getenv('TWITTER_API_SECRET')
access_token = os.getenv('ACCESS_TOKEN')
access_token_secret = os.getenv('ACCESS_TOKEN_SECRET')

# === Your link ===
LINK = "https://yourlink.com"

# === Hashtags (optional) ===
hashtags = "#promotion #content #marketing #viral"

# === Twitter auth ===
auth = tweepy.OAuth1UserHandler(api_key, api_secret, access_token, access_token_secret)
api = tweepy.API(auth)

# === Load Captions from File ===
def load_captions():
    with open("tweets.txt", "r", encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip()]

# === Tweet Function ===
def tweet_random():
    captions = load_captions()
    if not captions:
        print("No captions found in tweets.txt!")
        return
    tweet = random.choice(captions) + "\n" + LINK + "\n" + hashtags
    try:
        api.update_status(tweet)
        print("Tweeted:", tweet)
    except Exception as e:
        print("Error tweeting:", e)

# === Tweet Loop ===
while True:
    tweet_random()
    time.sleep(3 * 60 * 60)  # Wait 3 hours
