# Files and Functions are Imported

from get_user_post import get_user_post
from get_own_post import get_own_post
from get_user_info import get_user_info
from like_user_post import like_user_post
from comment_user_post import comment_user_post1
from self_info import self_info

from post_a_comment import post_a_comment
from delete_negative_comment import delete_negative_comment
import sys
from termcolor import colored
from trending_hashtag import get_trending_tag_counts

#   <-------------------------InstaBot Application Starts From Here------------------------>

color_text = colored("\n\t\t\t<------------*****Welcome To InstaBot Application*****------------>\n", "blue")
print
color_text

# Ask What you Want to do
choice = "What do you want to do. Select from the below Choices (1-6)" \
               "\n\n\t\t1. Show Own Profile Info " \
               "\n\t\t2. Download Own Post " \
               "\n\t\t3. Get User's Profile Information. " \
               "\n\t\t4. Download User's Recent Post " \
               "\n\t\t5. Like User's Recent Post" \
               " \n\t\t6. Comment on User's Recent Post " \
               " \n\t\t7. Make a comment on the recent post of a user" \
               " \n\t\t8. Delete a comment on user post" \
               " \n\t\t9. Show the trending events" \
               "\n\t\t10. Close Application  "

show_menu = True
while show_menu:  # if user enter valid key
    choice = input(choice)
    choice = int(choice)
    if choice == 1:
        # Control Goes to self_info.py
        self_info()
        print("\n\n")

    elif choice == 2:
        print("\n\t$$$$$ Downloading Your Own Recent Post.....\n")
        # Control Goes to get_own_post.py
        get_own_post()
        print("\n")

    elif choice == 3:
        insta_username = input("\nEnter The Username Who's Information You Want. \n")
        print("\t\tWait ** Information is Downloading...\n")
        # Control Goes to get_user_info.py
        get_user_info(insta_username)
        print("\n")

    elif choice == 4:
        insta_username = input("\nEnter The Username Who's Recent Post You Want To Download. \n")
        print("\t\tWait ** User's Recent Post is Downloading...")
        # Control Goes to get_user_post.py
        get_user_post(insta_username)
        print("\n")

    elif choice == 5:
        insta_username = input("Enter The Username Who's Recent Post You Want To Like. ")
        print("Wait ** Liking The User's Recent Post...")
        # Control Goes to like_user_post.py
        like_user_post(insta_username)
        print("\n")

    elif choice == 6:
        insta_username = input("\nEnter The Username Who's Recent Post You Want To Write Something. \n")
        print("\t\tWait ** Commenting in the User's Recent Post...")
        # Control Goes to comment_user_post.py
        comment_user_post1(insta_username)
        print("\n")


    elif choice == 7:
        insta_username =input("Enter the username of the user: ")
        post_a_comment(insta_username)

    elif choice == 8:
        insta_username =input("Enter the username of the user: ")
        delete_negative_comment(insta_username)

    elif choice == 9:
        tag = input("Enter Tagname.........\n")
        print("Wait counting Ur Tags......\n")
        get_trending_tag_counts(tag)
        print("Style.RESET_ALL\n")
        print("\n")
        print("\n")

    elif choice == 10:
        print(
            "\n\t\t<------------******Thanks To Be With Us*****------------>")
        exit()

    else:
        print(
        "<------------*****Wrong Input*****------------>")
        show_menu = False





#   <-------------------------InstaBot Application Ends Here------------------------>

