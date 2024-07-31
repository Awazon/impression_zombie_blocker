
import asyncio, os, time
import langdetect
from twikit import Client

USERNAME = ''
EMAIL = ''
PASSWORD = ''

COOKIE_PATH = os.path.expanduser("./cookies.json")

# Initialize client
client = Client('ja-JP')

async def main():
    if os.path.isfile(COOKIE_PATH):
        client.load_cookies(COOKIE_PATH)
        print("cookieからログイン")
    else:
        await client.login(
            auth_info_1=USERNAME ,
            auth_info_2=EMAIL,
            password=PASSWORD
        )
        print("通常ログイン")
        client.save_cookies("cookies.json")
    
    time.sleep(1)
    timeline = await client.get_timeline()
    tweet_lang = ""
    for tweet in timeline:
        try:
            tweet_lang = langdetect.detect(tweet.text)
        except:
            print("不明な言語のツイート")
            print(tweet)
            print("------------------------------")
        if tweet.reply_count > 50 and tweet.reply_count < 1000:
            if tweet_lang == 'ja':
                tweet = await client.get_tweet_by_id(tweet.id)
                print(tweet_lang)
                print(tweet)
                for reply in tweet.replies:
                    print(reply.text)
                    print(reply.reply_to)

                print("------------------------------")

asyncio.run(main())