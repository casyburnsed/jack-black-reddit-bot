import praw
import time

# I NEED TO USE .ENV TO PROTECT THESE CREDENTIALS
# Reddit API credentials
client_id = ""  
client_secret = "" 
username = "" 
password = ""  
user_agent = "" 

# Initialize Reddit instance
reddit = praw.Reddit(
    client_id=client_id,
    client_secret=client_secret,
    username=username,
    password=password,
    user_agent=user_agent
)

# Trigger phrase and response
trigger_phrase = "alright"
jack_black_response = "Aaaaalriiiiighhht!!! 🤘🔥🎸"

# Set of comments already replied to
replied_to = set()

# Check access to subreddit stream
subreddit = reddit.subreddit("all")
print("Stream access:", hasattr(subreddit, 'stream'))

# Monitor comments across all subreddits
for comment in subreddit.stream.comments(skip_existing=True):
    # Check for trigger phrase in comment
    if comment.id not in replied_to and trigger_phrase in comment.body.lower():
        try:
            comment.reply(jack_black_response)
            replied_to.add(comment.id)  # Prevent duplicate replies
            print(f"Replied with stylized 'alright' to comment ID: {comment.id}")
            time.sleep(2)  # Delay to avoid rate limiting
        except Exception as e:
            print(f"Error replying to comment ID: {comment.id} - {e}")
