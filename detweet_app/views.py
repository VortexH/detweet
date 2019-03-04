#!/usr/bin/python3
""" Script to start a Flask web application """
from detweet_app import app
from flask_dance.contrib.twitter import twitter
from flask import render_template, url_for, redirect
from . import deTweet

@app.route('/')
def serve_login_page():
    return render_template('login.html')

@app.route('/login')
def index():
    print("alsjdfalisjdfasdf")
    if not twitter.authorized:
        return redirect(url_for('twitter.login'))

    resp = twitter.get("account/verify_credentials.json")
    assert resp.ok
    

    screen_name = resp.json()['screen_name']
    print(screen_name)
    #return "You are @{screen_name} on Twitter".format(screen_name=resp.json()["screen_name"])
    return redirect(url_for('tweet_page', username=screen_name))

@app.route('/tweet_page/<username>')
def tweet_page(username):
    return render_template('index.html', username=username)

@app.route('/get_tweets')
def get_tweets():
    payload = {'screen_name': 'hemant_heer', 'count': 3200}
    resp = twitter.get('statuses/user_timeline.json', params=payload)
    print(resp.json())
    #return render_template('index.html', tweets=deTweet.safety())
    return "success"

if __name__ == '__main__':
    app.run('0.0.0.0', 5000)
