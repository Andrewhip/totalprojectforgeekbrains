import requests
import time
import csv
import html
import re

def take_100_posts():
    token = '////'
    domain = 'insidebmxru'
    version = '5.199'
    count = 100
    offset = 0
    all_posts = []

    while offset < 50:
        response = requests.get('https://api.vk.com/method/wall.get',
                                params={
                                    'access_token': token,
                                    'v': version,
                                    'domain': domain,
                                    'count': count,
                                    'offset': offset,
                                }
                                )

        data = response.json()['response']['items']
        offset += 10
        all_posts.extend(data)

    return all_posts

def file_write(all_posts):
    with open('files4mysite.csv', 'w', newline='', encoding='utf-8') as file:
        a_pen = csv.writer(file)
        a_pen.writerow(('body', 'url', 'video'))

        for post in all_posts:
            img_url = ''
            vid_url = ''
            try:
                if post.get('attachments') and post['attachments'][0].get('type') == 'photo':
                    img_url = post['attachments'][0]['photo']['sizes'][-1]['url']

                if post.get('attachments') and post['attachments'][0].get('type') == 'video':
                    vid_url = post['attachments'][0]['video']['first_frame'][0]['url']
            except:
                pass

            body = html.unescape(post['text'])
            body = re.sub(r'<[^>]*?>', '', body)

            a_pen.writerow((body, img_url, vid_url))

all_posts = take_100_posts()
file_write(all_posts)