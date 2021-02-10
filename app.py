from flask import Flask, request
from requests import get, post
from bs4 import BeautifulSoup as bs
import json, base64, random

app = Flask(__name__)

@app.route('/')
def home():
    a = {
    'Contoh-Penggunaan':{'lirik': 'api/lirik?search=alone', 'random-quotes':'api/random/quotes', 'info-gempa':'api/infogempa'}
    }
    return a

@app.route('/api/lirik')
def lirik():
    par= request.args.get('search')
    from lirik import search
    a = search(par)
    b = {
    'results': a.result()
    }
    return b

@app.route('/api/random/quotes', methods=['GET','POST'])
def quotes():
	quotes_file = json.loads(open('quotes.json').read())
	result = random.choice(quotes_file)
	print(result)
	return {
		'status': 200,
		'author': result['author'],
		'quotes': result['quotes']
	}

@app.route('/api/infogempa', methods=['GET','POST'])
def infogempa():
	be = bs(get('https://www.bmkg.go.id/').text, 'html.parser').find('div', class_="col-md-4 md-margin-bottom-10")
	em = be.findAll('li')
	img = be.find('a')['href']
	return {
		'status': 200,
		'map': img,
		'waktu': em[0].text,
		'magnitude': em[1].text,
		'kedalaman': em[2].text,
		'koordinat': em[3].text,
		'lokasi': em[4].text,
		'potensi': em[5].text
	}

if __name__ == '__main__':
    app.run()
