# Jonte's FoxBot For Discord
## What's this bot for?
It fetches a random image from the website [randomfox.ca](https://randomfox.ca/) by [xinitrc-dev](https://github.com/xinitrc-dev/randomfox.ca) when somebody writes `pic` or `picbomb` in a discord server where the bot is invited to. 

## How does it work?
Every time somebody sends a message, the bot checks if it matches one of the keywords described above. Then it generates a random number between 1 and 123 which is the amount of images on RandomFox. Then it sends `https://randomfox.ca/?i=`with the number generated above.

## How do I selfhost?
### Instructions
To selfhost, simply create a bot from Discord Dev Portal, get a token. Invite the bot to your server and save the token in a textfile called somewhere on a Linux server. Then run the following command: 
`docker run -v /path/to/foxbot-token.txt:/usr/share/bot/token.txt:ro jonatanholmgren/foxbot:latest`, but change out the `/path/to/foxbot-token.txt` to your actual path to the txt file, like in the example below.

### Example
The example assumes that you have stored your Discord token to `/home/jonte/token.txt`
`docker run -v /path/to/foxbot-token.txt:/usr/share/bot/token.txt:ro jonatanholmgren/foxbot:latest`.

### Legal stuff:
I do not own the images, and can not verify that none of the images have any copyright. This repo and my docker container found [here](https://hub.docker.com/r/jonatanholmgren/foxbot) have only **fetches** the images from randomfox.ca, thus making this their responsibility. The GPL 3.0 license included in this repo only applies for **my** code, not the images.
I also take 0 responsibility for this project existing for the long term, as I do not serve the images, and [xinitrc-dev](https://github.com/xinitrc-dev/randomfox.ca) might at any moment bring the site down.