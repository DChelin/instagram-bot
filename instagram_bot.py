#Instagram bot to gain more followers.

from instapy import InstaPy

#Enter Instagram username and password below:
session = InstaPy(username = " ", password = " ")
session.login()

session.set_relationship_bounds(enabled = True, max_followers = 1000)

#Add your like tags and dont like tags below.
session.set_do_follow(True, percentage = 100)
session.like_by_tags([''], amount = 3)
session.set_dont_like([''])

session.end()