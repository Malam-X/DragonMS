
"""
 SCRAPPER
 By DR4G0N5
"""

import urllib.request
import instaloader
import getpass
import twint
import pandas as pd
from pytube import YouTube
from collections import Counter
from bs4 import BeautifulSoup
from etc.set import *
from etc.set import clear
from etc.banner import banner_drgn
bot = instaloader.Instaloader()

class Scraper:
    def __init__(self, site):
        self.site = site

    def scrape(self):
        r = urllib.request.urlopen(self.site)
        html = r.read()
        parser = "html.parser"
        sp = BeautifulSoup(html,parser)
        for tag in sp.find_all("a"):
            url = tag.get("href")
            if url is None:
                continue
            if "articles" in url:
                print("\n" + url)
def mainscrap(scr):
    Scraper(scr).scrape()

def ig_info(users):
    try:
        profile = instaloader.Profile.from_username(bot.context, f'{users}')
        x = (f"""
        [+] Username   : {profile.username}
        [+] User ID    : {profile.userid}
        [+] Followers  : {profile.followers}
        [+] Followees  : {profile.followees}
        [+] Bio        : {profile.biography,profile.external_url}
        [+] Total Post : {profile.mediacount}
            """)
        NAME_PATH = 'result/ig_scrap.txt'
        with open(f'{NAME_PATH}', 'w') as wr:
            wr.write(x)
        print(f'{SUCES_SYM} Logs saved at [ {NAME_PATH} ]')
    except:
        sys.exit(f'{ERROR_SYM} Username not found!')

def ig_login():
    try:
        us = input(f'{PULS} Username: ')
        pw = getpass.getpass(f'{PULS} Password: ')
        bot.login(user=f"{us}",passwd=f"{pw}")
        bot.interactive_login(f"{us}")
    except:
        sys.exit(f'{ERROR_SYM} Wrong Password / Username.')

def scrap_foll():
    clear()
    banner_drgn()
    res = input(f'{PULS} Instagram Name: ')
    print(f'''
\u001b[1m[\u001b[32;1m1\u001b[0m\u001b[1m]\u001b[0m Scraping Followers ... {SUCES_SYM}
\u001b[1m[\u001b[32;1m2\u001b[0m\u001b[1m]\u001b[0m Scraping Followees ... {SUCES_SYM}''')
    try:
        profile = instaloader.Profile.from_username(bot.context, f'{res}')
        followers = [follower.username for follower in profile.get_followers()]
        followees = [followee.username for followee in profile.get_followees()]
        x = input(promt_choice)
        if x == '1':
            print(followers)
        elif x == '2':
            print(followees)
        else:
            raise ValueError(f'{ERRORS} INVALID VALUE.')
    except:
        sys.exit(f'{ERRORS} Login Needed.')

def ig_downloader(users):
    profile = instaloader.Profile.from_username(bot.context, 'users')
    posts = profile.get_posts()
    for index, post in enumerate(posts, 1):
        bot.download_post(post, target=f"{profile.username}_{index}")

def ghost_follow(users):
    USER = users
    PROFILE = USER

    bot.load_session_from_file(USER)

    profile = instaloader.Profile.from_username(bot.context, PROFILE)

    likes = set()
    print("Fetching likes of all posts of profile {}.".format(profile.username))
    for post in profile.get_posts():
        print(post)
        likes = likes | set(post.get_likes())

    print("Fetching followers of profile {}.".format(profile.username))
    followers = set(profile.get_followers())

    ghosts = followers - likes

    print("Storing ghosts into file.")
    with open("result/inactive-users.txt", 'w') as f:
        for ghost in ghosts:
            print(ghost.username, file=f)
def main_scraper():
    import time
    clear()
    banner_drgn()
    print(f'''
\u001b[1m[\u001b[32;1m1\u001b[0m\u001b[1m]\u001b[0m Account Info ..... {SUCES_SYM}
\u001b[1m[\u001b[32;1m2\u001b[0m\u001b[1m]\u001b[0m Instagram Login .. {SUCES_SYM}
\u001b[1m[\u001b[32;1m3\u001b[0m\u001b[1m]\u001b[0m Scrap Follow ..... {SUCES_SYM}
\u001b[1m[\u001b[32;1m4\u001b[0m\u001b[1m]\u001b[0m Download Post .... {SUCES_SYM}
\u001b[1m[\u001b[32;1m5\u001b[0m\u001b[1m]\u001b[0m Ghost Followers .. {SUCES_SYM}
''')
    try:
        x = input(promt_choice)
        if x == '1':
            clear()
            banner_drgn()
            try:
                res = input(f'{PULS} Instagram Name: ')
                try:
                    if res == '' or len(res) == '2':
                        print(f'{ERRORS} try again.')
                        time.sleep(2)
                        main_scraper()
                    ig_info(res)
                except:
                    sys.exit(f'{ERROR_SYM} Username not found!')
            except KeyboardInterrupt:
                sys.exit(f'{Aborted}')
        elif x == '2':
            ig_login()
        elif x == '3':
            scrap_foll()
        elif x == '4':
            clear()
            banner_drgn()
            try:
                res = input(f'{PULS} Instagram Name: ')

                if res == '' or len(res) == '2':
                    print(f'{ERRORS} try again.')
                    time.sleep(2)
                    main_scraper()
                ig_downloader(res)
            except KeyboardInterrupt:
                sys.exit(f'{Aborted}')
        elif x == '5':
            clear()
            banner_drgn()
            try:
                res = input(f'{PULS} Instagram Name: ')
                try:
                    if res == '' or len(res) == '2':
                        print(f'{ERRORS} try again.')
                        time.sleep(2)
                        main_scraper()
                    ghost_follow(res)
                except Exception as e:
                    sys.exit(f'{ERROR_SYM} {e}')
            except KeyboardInterrupt:
                sys.exit(f'{Aborted}')
    except KeyboardInterrupt:
        sys.exit(f'{Aborted}')
    except ValueError:
        sys.exit(f'{NFound}')

def get_followings(username):

    c = twint.Config()
    c.Username = username
    c.Pandas = True

    twint.run.Following(c)
    list_of_followings = twint.storage.panda.Follow_df

    return list_of_followings['following'][username]

def stat(named):
    clear()
    banner_drgn()
    try:
        users = [f'{named}']
        followings = {}
        following_list = []
        for person in users:
            print(f'{PULS} Starting : {person}')
            try:
                followings[person] = get_followings(person)
                following_list = following_list + followings[person]
            except KeyError:
                print(f'{ERRORS} IndexError')

        Counter(following_list).most_common(10)

        follow_relations ={}
        for following_user in followings.keys():
            follow_relation_list = []
            for followed_user in followings.keys():
                if followed_user in followings[following_user]:
                    follow_relation_list.append(True)
                else:
                    follow_relation_list.append(False)
            follow_relations[following_user] = follow_relation_list

        following_df = pd.DataFrame.from_dict(follow_relations,
                                              orient='index', columns=followings.keys())
        following_df
    except KeyboardInterrupt:

        sys.exit(Aborted)
def youtube_scr(url):
    don = YouTube(url)
    print(f"""
[+] Title       : {don.title}
[+] Views       : {don.views}
[+] Duration    : {don.length}
[+] Description : {don.description}
[+] Ratings     : {don.rating}
        """)
    stream = don.streams.get_highest_resolution()
    stream.download()
    print(f"{PULS} Download completed!!")
