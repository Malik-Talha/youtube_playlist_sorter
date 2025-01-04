import os
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

def getResponse(driver, url):
	print("Getting response. Please wait.......")
	driver.get(url)
	driver.implicitly_wait(20)
	return driver

def sort_videos(driver, path):
	directory_list = os.listdir(path)

	# this has been deprecated
	# names = driver.find_elements_by_id("video-title")
	####################

	names = driver.find_elements(By.ID, "video-title") 

	print("Sorting. Please wait.......")
	for i, new_name in enumerate(names):
		# if new_name.text in directory_list:
		for index, item in enumerate(directory_list):
			#if the file is already sorted
			if item[0] == i:
				break 
			# replacing all other characters into '_'
			translation_table = str.maketrans("&\",/\\?|#$%'", "___________")
			if new_name.text.strip().translate(translation_table) in item:
				new_file_name = os.path.join(path, str(1+i) + ' ' + str(new_name.text.strip().translate(translation_table)) + '.mp4')
				os.rename(os.path.join(path, directory_list[index]), new_file_name)
				break


def main():
	#setting the new path for webdriver
	# new_directory = input("Enter the path of webdriver folder: ").replace('\\','/')
	new_directory = "E:\\T\\Programs_27\\Python_Projects\Projects\\Youtube Playlist Sorter\\chromedriver-win64\\"
	current_path = os.environ["PATH"]
	os.environ["PATH"] = new_directory + ";" + current_path

	#making chrome headless
	options = webdriver.ChromeOptions()
	options.add_argument('--headless')
	# options.add_argument('excludeswitches','[enable-automation]')
	
	driver = webdriver.Chrome(options=options)

	# getting playlist url from the user
	# url = input("Enter the url of Youtube Playlist: ")
	url = "https://www.youtube.com/playlist?list=PLo2EIpI_JMQvWfQndUesu0nPBAtZ9gP1o"

	driver = getResponse(driver,url)

	# getting folder path of the folder to be sorted in
	# path = input("Enter the path of folder: ").replace('\\','/')
	path = "E:\\T\\HuggingFace Courses\\"
	sort_videos(driver, path)
	driver.quit()
	print("Success!")

if __name__ == "__main__":
	main()


        