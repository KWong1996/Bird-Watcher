# How to use

### When ran, the script will search through your home timeline for certain tweets matching your search criteria. Once all relevant tweets are found, they are then exported to a JSON file named after the date and time the script was executed. Within the script, you can customize how many tweets to read from your timeline at a time through the 'count' variable within 'watch.py'. Twitter limits users to 15 requests per hour. The script will sleep and wait if the limit is reached and try to run until the limit is reset again.

## secrets.json

### On your local directory create a file called "secrets.json" with the following format containing your twitter API access keys

```shell
{
    "CONSUMER_KEY": "9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08",
    "CONSUMER_SECRET": "7d6fd7774f0d87624da6dcf16d0d3d104c3191e771fbe2f39c86aed4b2bf1a0f",
    "ACCESS_TOKEN": "ab03c34f1ece08211fe2a8039fd6424199b3f5d7b55ff13b1134b364776c45c5",
    "ACCESS_TOKEN_SECRET": "63d6ff853569a0aadec5f247bba51786bb73494d1a06bdc036ebac5034a2920b"
}
```

## criteria.json

### Within the 'criteria.json' file, input any specific tweets that you would like to search for. Currently, the script can search your timeline for tweets with certain keywords, tweets linking to specific domains, or if the tweet contains any media

### Example:
```shell
{
    "keywords": ["python","tweepy"],
    "websites": ["twitter.com","youtube.com"],
    "media": true
}
```

