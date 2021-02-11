from flask import Flask, request
from requests import get, post
from bs4 import BeautifulSoup as bs
from urllib.parse import *
import json, base64, random, re, html_text, math, os

app = Flask(__name__)

@app.route('/')
def home():
    a = {
    'Contoh-Penggunaan':{'search-lirik': 'api/lirik?search=alone', 'random-quotes':'api/random/quotes', 'info-gempa':'api/infogempa', 'random-asmaulhusna':'api/random/asmaulhusna'}
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
	quote = json.loads(open('quotes.json').read())
	result = random.choice(quote)
	print(result)
	return {
		'status': 200,
		'author': result['author'],
		'quotes': result['quotes']
	}

@app.route('/api/random/asmaulhusna', methods=['GET','POST'])
def quotes():
	asmaul = json.loads(open('asmaul.json').read())
	result = random.choice(asmaul)
	print(result)
	return {
		'status': 200,
		'no': result['index'],
		'latin': result['latin'],
                'arabic': result['arabic'],
                'translate_id': result['translation_id'],
                'translate_en': result['translation_en']
	}

@app.route('/api/infogempa', methods=['GET','POST'])
def infogempa():
	be = bs(get('https://www.bmkg.go.id/').text, 'html.parser').find('div', class_="col-md-4 md-margin-bottom-10")
	em = be.findAll('li')
	gambar = be.find('a')['href']
	return {
		'status': 200,
		'map': gambar,
		'waktu': em[0].text,
		'magnitude': em[1].text,
		'kedalaman': em[2].text,
		'koordinat': em[3].text,
		'lokasi': em[4].text,
		'potensi': em[5].text
	}

@app.route('/api/chord', methods=['GET','POST'])
def chord():
	if request.args.get('q'):
		try:
			q = request.args.get('q').replace(' ','+')
			id = get('http://app.chordindonesia.com/?json=get_search_results&exclude=date,modified,attachments,comment_count,comment_status,thumbnail,thumbnail_images,author,excerpt,content,categories,tags,comments,custom_fields&search=%s' % q).json()['posts'][0]['id']
			chord = get('http://app.chordindonesia.com/?json=get_post&id=%s' % id).json()
			result = html_text.parse_html(chord['post']['content']).text_content()
			return {
				'status': 200,
				'result': result
			}
		except Exception as e:
			print(e)
			return {
				'status': False,
				'error': '[❗] Maaf chord yang anda cari tidak dapat saya temukan!'
			}
	else:
		return {
			'status': False,
			'msg': '[!] Masukkan parameter q'
		}

if __name__ == '__main__':
    app.run()
