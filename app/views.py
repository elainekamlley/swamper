# -*- coding: utf-8 -*-

from app import app
from flask import render_template
from models import Post

@app.route('/')
def index():
	post_1 = Post('Never gonna get it', 'En Vogue', 'I remember how it used to be, you never were this nice, you cant fool me')
	post_2 = Post('Dancing on my own', 'Robyn', 'Im in the corner watching you kiss her, ohhhh!')
	post_3 = Post('Sittin up in my room', 'Brandi', 'Seems like ever since from the first day we met')
	post_4 = Post('I wanna be down', 'Brandi', 'With what youre going in through, I want to be down ow ow owwwwn')

	return render_template('index.html', posts = [post_1, post_2, post_3, post_4])


