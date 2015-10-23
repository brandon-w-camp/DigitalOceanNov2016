from flask import Flask, render_template
import json

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('home.html')


@app.route('/tweets/')
def tweets():
    return render_template('tweets.html')


@app.route('/get_tweets/')
def get_tweets():
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from sqlalchemy import Column, Integer, String
    from sqlalchemy.ext.declarative import declarative_base

    Base = declarative_base()

    class Tweet(Base):
        __tablename__ = 'tweets'

        tweet_id = Column(Integer, primary_key=True)
        tweet = Column(String)

        def __repr__(self):
            return "<tweet(tweet='%s')>" % self.tweet

        def __getitem__(self):
            return self.tweet

    engine = create_engine('sqlite:///C:/Users/Brandon-Camp/PycharmProjects/twittenby/tweets.db')
    Session = sessionmaker(bind=engine)
    session = Session()
    result = session.execute("SELECT tweet FROM tweets ORDER BY tweet_id DESC")

    derp = [{"content": row['tweet']} for row in result]
    return json.dumps(derp)

if __name__ == '__main__':
    app.run(debug=True)
