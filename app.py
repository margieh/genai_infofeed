from flask import Flask, render_template
import feedparser
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/')
def home():
    rss_feed = 'https://feeds.npr.org/1126/rss.xml'
    feed = feedparser.parse(rss_feed)
    articles = []

    for entry in feed.entries:
        soup = BeautifulSoup(entry.content[0].value, 'html.parser')
        img_tag = soup.find('img')
        if img_tag:
            image_url = img_tag['src']
        else:
            image_url = None

        article = {
            'title': entry.title,
            'description': entry.description,
            'image_url': image_url,
            'pubDate': entry.published,
            'link': entry.link
        }
        articles.append(article)

    return render_template('index.html', articles=articles)

if __name__ == '__main__':
    app.run(debug=True)
