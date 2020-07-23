from instabot import Bot 

def upload(fileName, fileCaption):
	bot = Bot() 
  
	bot.login(username = "USERNAME",  
          password = "PASSWORD")

	bot.upload_photo(fileName,fileCaption) 