from instabot import Bot 

# rename to PostOnIg.py
# & add in instagram USERNAME and PASSWORD

def upload(fileName, fileCaption):
	bot = Bot() 
  
	bot.login(username = "USERNAME",  
          password = "PASSWORD")

	bot.upload_photo(fileName,fileCaption) 
