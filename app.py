from flask import Flask, render_template, request
import feedparser
from bs4 import BeautifulSoup

app = Flask(__name__)

RSS_FEED = 'https://feeds.npr.org/1126/rss.xml'
ARTICLES_PER_PAGE = 5

@app.route('/')
def home():
    page = request.args.get('page', default=1, type=int)
    feed = feedparser.parse(RSS_FEED)
    total_articles = len(feed.entries)
    total_pages = (total_articles + ARTICLES_PER_PAGE - 1) // ARTICLES_PER_PAGE

    start_index = (page - 1) * ARTICLES_PER_PAGE
    end_index = min(start_index + ARTICLES_PER_PAGE, total_articles)
    articles = []

    for entry in feed.entries[start_index:end_index]:
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

    return render_template('index.html', articles=articles, page=page, total_pages=total_pages)

if __name__ == '__main__':
    app.run(debug=True)


