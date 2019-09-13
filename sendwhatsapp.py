driverpath='I:\\Installer\\chromedriver_win32\\chromedriver' #dont forget quotes  

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException #raise exceptions when contact not found
from selenium.webdriver.chrome.options import Options
import time
# Options
options = Options()
options.add_argument("user-data-dir=C:\\Users\\xxxx\\AppData\\Local\\Google\\Chrome\\User Data\\Cache")  #search cache folder, update if required

print('\n\nSCAN THE QR CODE AND DO NOT PRESS ANY KEY UNTIL NEXT INSTRUCTION, ignore lines stating errors if any\n\n')
try:
	driver = webdriver.Chrome(chrome_options=options, executable_path='chromedriver')
except:
	driver = webdriver.Chrome(chrome_options=options, executable_path=driverpath)
driver.get('https://web.whatsapp.com/')
input('\n\nPRESS ENTER KEY TO CONTINUE, after Whatsapp Webpage is fully loaded, ignore lines stating errors if any\n\n')
while(1):
	flag=1 # flag to check whether contact is in ur phone or not
	name = input('Enter name of contact or group or q to quit (case sensitive): ')
	if name=='q' or name=='Q': # exit the program
		break
	contactsearchbox=driver.find_element_by_class_name('_2zCfw') #search box class name, update if required
	contactsearchbox.clear() #clear search box
	contactsearchbox.send_keys(name) #enter name to search box
	print('searching.........'+name)
	time.sleep(2) # wating 2 sec
	try:
		recipient = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
	except NoSuchElementException:
		print('No contact or Group found with name: '+name)
		flag=0
	if flag==1:
		choice=input('contact found, send message? Y/N: ')
		if choice=='y' or choice=='Y':
			recipient.click() #select the contact
			msg = input('Enter your message: ')	
			msg_box = driver.find_element_by_class_name('_3u328') #class name may change, update if required
			msg_box.clear()
			msg_box.send_keys(msg)
			try:
				button = driver.find_element_by_class_name('_3M-N-') # class name may change, update if required
			except NoSuchElementException:
				print('no messsage typed or class name changed of send button')
				continue
			button.click()
			print('message send successfully')
input('\n\nPRESS ENTER KEY TO EXIT THE PROGRAM\n\n')
driver.close()
