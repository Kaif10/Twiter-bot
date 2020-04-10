import tweepy
import time

print('This is my twitter bot.')

CONSUMER_KEY ='KdgpcYBVbxsFyxnUI0w0VleUL'

CONSUMER_SECRET = 'MEr2C7nt88jTfgiSrbJw0ErKirhf5TXM2QnPKa1mcr9Se1ThH3'
ACCESS_KEY = '1212764609142067200-9DTn913dz2tLZqAsAHNUnVjoO2ouwV'
ACCESS_SECRET = 'QOYUj9NafAaMPIYOdDjoVMvVrl2oTc1TYnGCPD4UbnMkn'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True)



FILE_NAME = 'last_seen_id.txt'

def retrieve_last_seen_id(file_name):
    f_read = open(file_name, 'r')
    last_seen_id = int(f_read.read().strip())
    f_read.close()
    return last_seen_id

def store_last_seen_id(last_seen_id, file_name):
    f_write = open(file_name, 'w')
    f_write.write(str(last_seen_id))
    f_write.close()
    return

def reply_to_tweets():
    print('retrieving and replying to tweets...', flush=True)
    # DEV NOTE: use 1060651988453654528 for testing.
    last_seen_id = retrieve_last_seen_id(FILE_NAME)
    # NOTE: We need to use tweet_mode='extended' below to show
    # all full tweets (with full_text). Without it, long tweets
    # would be cut off.
    mentions = api.mentions_timeline(
                        last_seen_id,
                        tweet_mode='extended')
    for mention in reversed(mentions):
        print(str(mention.id) + ' - ' + mention.full_text, flush=True)
        last_seen_id = mention.id
        store_last_seen_id(last_seen_id, FILE_NAME)
        if '#rip' in mention.full_text.lower():
            print('found #RIP!', flush=True)
            print('responding back...', flush=True)
            api.update_status('@' + mention.user.screen_name +
                    '#Thank you so much it means a lot.!', mention.id)

while True:
   reply_to_tweets()
   time.sleep(15)