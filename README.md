# Darka bot

## What is Darka bot?

Darka bot is an agent that you can ask it to perform some commands to interactive with other
twitter users.

You can indirectly send text messages to twitter users via Darka bot. You can ask robot to follow
twitter users as well.

More commands will be added future.

## How to use Darka bot?

Darka bot is a twitter user. You can start to interactive with robot by tweeting:

 `@darka_bot #signup`

Darka bot will add you to its list. You can opt out by tweeting:

`@darka_bot #signout`

You can check valid commands by tweeting: `@darka_bot #help` and if you want help text for a command,
please tweet `@darka_bot #help signup`

## Valid commends:

- signup
- signout
- help

    e.g. \#help follow
- follow

    e.g. \#follow BBCWorld 
- mention

    e.g. \#mention BBCWorld Thanks for the news.

## Build your own
1. Required setup
    
    - a twitter developer account
    - a google sheet
    - enable google sheet api

2. Configuration

    - create a file `configs.py` file at root directory
    - create a `Configures` class in `configs.py`
    ```python
    class Configures():
        CONSUMER_KEY = 'YOUR TWITTER CONSUMER KEY'
        CONSUMER_SECRET = 'YOUR TWITTER CONSUMER SECRET'
        ACCESS_KEY = 'YOUR TWITTER ACCESS_KEY'
        ACCESS_SECRET = 'YOUR TWITTER ACCESS_SECRET'
        SPREADSHEET_ID = 'YOUR GOOGLE SPREADSHEET ID'
        USER_SHEET_ID = 'SHEET_ID FOR users '
    ```

3. Google sheets

There are 3 sheets in Google sheet. You can name your spreadsheet with any names. 
However, sheet names have to be the following:
- logs
- history
- users

    3.1 logs

    Records begin from second row. So you can give header row any title.

    Column A is which user @ the robot
    
    Column B is text message in that status

    3.2 history

    A2 is last processed twitter time line id. So Robot won't process the same message twice.

    A1 is free to be named.

    3.3 users

    Column A is used to record signup users. Records starts from second row.