BOT_ACTIVE = True

import twitter
import time
from time import strftime

api = twitter.Api(consumer_key='Vw40KJ9aySFTNq95NRG13w',
		  consumer_secret='cnbiT2cShL7wkiujrYLvEHAEn8Lfy0IXNxy7pHTGn8',
		  access_token_key='1056768690-xqA5qtD87an4GsAzA8KEjqWstKgTAEljApP5fD7',
		  access_token_secret='TfIzXJoSVEeypAa2vu0UDxiZQdg8W6aN6LFa0cZmE')

# Get current time and format
current_time = strftime("%a, %d %b %Y %X")

# Tweet BOT active with timestamp
status = 'Hello, I was activated @ ' + current_time
print status
api.PostUpdates(status)

print "Press CTRL-C to interrupt and see options"

while BOT_ACTIVE:
	try: time.sleep(1)

	except KeyboardInterrupt:
		KINT = True
		while KINT:
			input = raw_input("Exit? (Y/N) ")
			if input == 'Y' or input == 'y':
				BOT_ACTIVE = False
				KINT = False
			else:
				print "ERROR Invalid Entry"

# Get current time and format
current_time = strftime("%a, %d %b %Y %X")

#Tweet BOT disabled with timestamp
status = 'Hello, I was disabled @ ' + current_time
print status
api.PostUpdates(status)

