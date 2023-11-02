import requests
from bs4 import BeautifulSoup
from plyer import notification
import time

def scrape_manga_data(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    page.close()
    titles = soup.find_all('h3', {'class': 'film-name'})
    title_list = [title.find('a')['title'] for title in titles]
    print(title_list)
    return title_list



def check_for_new_anime(url, prev_titles):
    new_titles = scrape_manga_data(url)
    added_titles = [title for title in new_titles if title not in prev_titles]
    
    if added_titles:
        notification_title = "New Anime Added"
        notification_text = "\n".join(added_titles)
        notification.notify(
            title=notification_title,
            message=notification_text,
            timeout=10
        )
        
    return new_titles

page_url = "https://9animetv.to/recently-added"
previous_titles = scrape_manga_data(page_url)

while True:
    time.sleep(6 * 30 * 24 * 60 * 60)  # Sleep for six months
    previous_titles = check_for_new_anime(page_url, previous_titles)
