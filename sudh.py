from Tix import _dummyComboBox

import requests

BASE_URL = "https://api.instagram.com/v1"

APP_ACCESS_TOKEN = "398715021.1c98adf.13e3472fd0914d20bcccb1bd9f89a038"

response = ""



# To print my own info
def my_info():

    URL = BASE_URL + "/users/self?access_token=%s" %(APP_ACCESS_TOKEN)

    response = requests.get(URL)



    return response.json()


#to print users id

def get_user_id(user_name):

    URL = BASE_URL + "/users/search?q=%s&access_token=%s" %(user_name,APP_ACCESS_TOKEN)

    response = requests.get(URL)

    user_id = response.json()['data'][0]['id']



    return user_id


#to print posts of users

def get_user_media(User_name):

    user_id = get_user_id(User_name)

    URL = BASE_URL +"/users/%s/media/recent?access_token=%s" %(user_id,APP_ACCESS_TOKEN)

    response = requests.get(URL)

    info = response.json()["data"]

    if info:

        for i in range(len(info)):

            print "Post ID: %s" %(info[i]["id"])

            print "post Link: %s" %(info[i]["link"])

            print "Comment Count : %s" %(info[i]["comments"]["count"])

            print "Like Count : %s" %(info[i]["likes"]['count'])

            if info[i]["caption"]['text']:
                print "Caption:%s" %(info[i]["caption"]['text'])

            else:
                print "Sorry!!! No caption"

    else:
        print "Sorry!! The User has no Posts"







#this function fetches User Id


def get_media_id(User_name):

    user_id = get_user_id(User_name)

    URL = BASE_URL + "/users/%s/media/recent?access_token=%s" % (user_id, APP_ACCESS_TOKEN)

    response = requests.get(URL)

    info = response.json()["data"]

    return info[1]["id"]








# LIKES THE POST OF THE ENTERED USER NAME AND POST ORDER

def like_a_post(user_name):

    i = raw_input("Enter the serial number of post u want to like")

    media_id = get_media_id(user_name)

    URL = BASE_URL + "/media/%s/likes" %(media_id)

    payload = {"access_token": APP_ACCESS_TOKEN}

    response = requests.post(URL,payload).json()

    print response

    if response['meta']['code'] == 200:
        print "Congratulations! The post has been successfully liked"

    else :
        print "OOPS!! Have a look at your code"






# this function comments on the post

def comment_on_a_post(username):

    media_id = get_media_id(username)

    text = raw_input("Enter the comment")


    URL = BASE_URL + "/media/%s/comments" % (media_id)

    payload = {"access_token": APP_ACCESS_TOKEN,"text":text}

    response = requests.post(URL , payload).json()

    print response

    if response["meta"]["code"]==200:
        print "Successfully commented!!"

    else :
        print 'Could not comment!!!, Recheck your comment'
        print response['meta']["error_message"]



 #this function returns the comment id of the comment with the word we are searching for

def get_comment_id(username):

    media_id = get_media_id(username)

    URL = BASE_URL + "/media/%s/comments?access_token=%s" %(media_id,APP_ACCESS_TOKEN)

    word = raw_input("Enter the word you are searching for")

    response = requests.get(URL)

    info = response.json()["data"]

    comment_id = []

    print response.json()

# Storing all the commenrt_id of comments containing word entered by user in a list "comment_id)
    for i in range(len(info)):

        split = info[i]['text'].split()

        if word in split:
            comment_id.append(info[i]['id'])


    return comment_id


 #This function prints the name of the one who commented along with the comments.

def print_all_comments(username):

    media_id = get_media_id(username)

    URL = BASE_URL + "/media/%s/comments?access_token=%s" % (media_id, APP_ACCESS_TOKEN)


    response = requests.get(URL)

    info = response.json()["data"]

    if len(info)==0:
        print "Sorry!!! No Comments!!"
        return None

    for i in range(len(info)):
        print "%s commented %s" % (info[i]["from"]["username"], info[i]['text'])


#deleting all the comments containing particular word by help of the list of comment_id returned by the get_comment_id() function
def delete_comment(username):

    media_id = get_media_id(username)

    comment_id = get_comment_id(username)
    print media_id
    print comment_id

    if len(comment_id)>0:

#deleting all the comments containing particular word by help of the list of comment_id returned by the get_comment_id() function

        for itr in comment_id:

            URL = BASE_URL + "/media/%s/comments/%s?access_token=%s" %(media_id,itr,APP_ACCESS_TOKEN)
            print URL
            response = requests.delete(URL)
            print itr
            print response




delete_comment('piyush')




delete_comment('piyush')








