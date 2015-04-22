The Pitch: My bot will check for annoying grammatical errors that people should have learned in elementary school. In particular, it will target users who erroneously use "different than" instead of "different from." The bot will report on how often said user has incorrectly used this construction in the recent past. 

The Steps: 
1. The bot should check the search/tweets endpoint of the Twitter API.

2. For each tweet, I want to save the screen name or the user ID.

3. Analyze past tweets; for a given user the bot will check the statuses/user_timeline endpoint. For each tweet, check if the tweet contains "different than". Accumulate a count of the number of times it was used. 

4. The bot should respond by sending out a tweet via twitter's statuses/update endpoint.

5. The bot will tweet a link to a website explaining the correct grammar usage and will mention how often said user has used "different than" in the past thousand tweets. 