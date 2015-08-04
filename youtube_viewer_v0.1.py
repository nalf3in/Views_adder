import webbrowser    # Import statements
import time
import os
import requests

print  ('''
.  .                    .  .           .   .
\ /* _ .    , __   _. _| _| _ ._.   _.|._ |_  _.
\/ |(/, \/\/ _)   (_](_](_](/,[    (_]|[_)[ )(_]
                                       |
made by nalf3in
          ''')



def open_webpage(number_of_the_visit,number_of_views_wanted,refresh):        # main function, access a webpage
    for temporary_proxie in proxies:

     if number_of_the_visit <= number_of_views_wanted:
      print ('Number of the visit: ', number_of_the_visit)
      number_of_the_visit +=1
      try:
         r = requests.get(url,proxies={'http':'http://{}'.format(temporary_proxie)})
         print ('page visited')
         print('')
         time.sleep(refresh)

      except:
         print ('error, page not visited...')
         time.sleep(refresh)
         print('')
         continue
     else:
          break
def verify_int(user_input):             # It's the function that verify if the input of the user is a number
    try:
        user_input = int(user_input)
        return True
    except ValueError:                  # If the user does not enter a number
        print('')
        print ('This is not a valid input please retry ')

proxies = open('proxies.txt','r')     # open the proxy list
number_of_the_visit = 1               # set the number of the visit to 0
url = input("Enter your url: ")       # Specify the url




while True:
 number_of_views = input ('How many views do you want ? : ')    # specify the number of views the user want with error handling from verify_int()
 if verify_int(number_of_views):
     number_of_views = int(number_of_views)    # Transform the str in a int
     break

while True:
    refresh = input("Enter refresh rate(seconds) : ")          # specify the refresh rate of the request
    if verify_int(refresh):
        refresh = float(refresh)     # transform the refresh rate with float()
        break



open_webpage(number_of_the_visit,number_of_views,refresh)

print ('Finished !')
