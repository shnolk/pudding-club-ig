from bing_image_downloader import downloader
import randomWords
import os

searchWord = randomWords.generateWord()
downloader.download(searchWord, 
	limit=1,  
	output_dir='dataset', 
	adult_filter_off=True, 
	force_replace=True)

for files in os.walk("./dataset/" + searchWord):
    for filename in files:
        print(filename)