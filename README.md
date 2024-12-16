# jack-black-reddit-bot
Jack Black Reddit Bot 🤘🔥🎸
Project Summary
The Jack Black Reddit Bot is a Python script that interacts with Reddit using the praw library. The bot monitors comments across all subreddits in real time and listens for the trigger phrase "alright". When it detects the phrase, it responds with a stylized Jack Black-inspired message: "Aaaaalriiiiighhht!!! 🤘🔥🎸". The bot includes safeguards such as tracking replied-to comments to avoid duplicate responses and adhering to Reddit’s API rules.

This project demonstrates practical skills in API integration, real-time data processing, and bot automation while ensuring responsible interaction with the platform.

Skills Demonstrated
1. Python Programming: Developed a functional bot with efficient use of loops, conditionals, and data structures like sets.
2. API Integration: Utilized the praw library to authenticate and interact with Reddit’s API.
3. Secure Credential Management: Encouraged the use of environment variables (via .env) to protect sensitive API credentials.
4. Error Handling: Implemented exception handling to manage API errors and unexpected issues during runtime.
5. Bot Development: Designed a bot to monitor and respond to live user-generated content.
6. Rate-Limiting Compliance: Added delays (time.sleep) to minimize the risk of exceeding Reddit’s API rate limits.
7. Comment Tracking: Used a set to track and prevent duplicate replies during runtime.

How It Works
1. Initialization: The bot connects to Reddit’s API using credentials securely managed in the script.
2. Comment Stream Monitoring: It listens for new comments across all subreddits in real time using the praw stream functionality.
3. Trigger Phrase Detection: When a comment containing the phrase "alright" is detected (case insensitive), the bot replies with the Jack Black-inspired message.
4. Duplicate Reply Prevention: The bot maintains a runtime set of replied-to comment IDs to ensure it doesn’t reply to the same comment more than once.
5. Error Handling: Logs errors and skips problematic comments to maintain smooth operation.
6. Rate Limiting: Introduces a delay between replies to comply with Reddit’s API rate limits.

