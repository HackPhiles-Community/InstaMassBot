#Imports sucessfully
from instabot import bot
import os

#configuring vars
USER = os.environ.get('USERNAME')
PASSWARD = os.environ.get('PASSWARD')
MESSAGE = os.environ.get('MESSAGE')

#running of the bot
bot.login(USER,PASSWARD)   #login by user 
print('login sucessfull')  #sucess message
bot.follwers_list(USER)    #getting followers list
users = bot.users          #asignning users to a value
for user in users:         #loop
    bot.message(user,MESSAGE)       #messaging to user in users
    print('Message send to '+user+' sucessfully!')    #sucess msg 
