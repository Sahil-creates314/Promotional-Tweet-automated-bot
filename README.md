# Promotional Tweet Automation Bot

This Python project uses the Twitter API to automatically post promotional tweets at set intervals. Tweets are selected randomly from a list of custom-written captions, making each post engaging and unique.

## Features
- Random tweet generation
- Interval-based auto-posting (e.g., every 3 hours)
- Environment-based key management
- Easy customization of captions and hashtags

## Tech Stack
- Python
- Tweepy (Twitter API)
- Scheduler with `time.sleep()`
- Bitly or Netlify links (for traffic redirection)

## Setup Instructions
1. Clone the repository.
2. Create a `.env` file and add your API keys:
   ```
   TWITTER_API_KEY=your_key
   TWITTER_API_SECRET=your_secret
   ACCESS_TOKEN=your_token
   ACCESS_TOKEN_SECRET=your_token_secret
   ```
3. Add your promotional captions in `tweets.txt`
4. Run:
   ```
   python main.py
   ```

## Example Use Cases
- Affiliate marketing
- Product promotion
- Event reminders
- Content teasers




if you have any queries (ik you will defi have lol) contact me on my email: sahilsid314@gmail.com
