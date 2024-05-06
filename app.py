from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    # Sample articles
    articles = [
        {
            'title': 'Article 1',
            'content': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.',
            'source_link': 'https://example.com/article1',
            'timestamp': '2024-05-06'
        },
        {
            'title': 'Article 2',
            'content': 'Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.',
            'source_link': 'https://example.com/article2',
            'timestamp': '2024-05-05'
        },
        # Add more sample articles as needed
    ]
    return render_template('index.html', articles=articles)

if __name__ == '__main__':
    app.run(debug=True)
