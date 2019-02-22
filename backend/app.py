from flask import Flask, jsonify
from scraper import *

app = Flask(__name__)
    
@app.route('/')
def index():
    return '<h1>Welcome to Company Insights API!</h1>Checkout the project on <a href="https://github.com/PeterDulworth/nesh-company-insights">github!</a>'

# e.g. http://localhost:5000/symbol/OXY
@app.route('/symbol/<string:symbol>')
def getSymbol(symbol):
    scrapedData = scrapeNasdaqSymbol(symbol)
    
    if (scrapedData == None):
        response = jsonify(status=404)
        response.headers.add('Access-Control-Allow-Origin', '*')    
        return response
    
    response = jsonify(company=scrapedData, status=200)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

# e.g. http://localhost:5000/symbol/news-headlines/OXY
@app.route('/symbol/headlines/<string:symbol>')
def getSymbolHeadlines(symbol):
    headlines = scrapeNasdaqHeadlines(symbol)
    
    if (headlines == None):
        response = jsonify(status=404)
        response.headers.add('Access-Control-Allow-Origin', '*')    
        return response
    
    response = jsonify(articles=headlines, status=200)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

# e.g. http://localhost:5000/symbol/earnings/calls/OXY
@app.route('/symbol/earnings/calls/<string:symbol>')
def getSymbolEarningsCalls(symbol):
    calls = scrapeSeekingAlphaEarningsCalls(symbol)
    
    if (calls == None):
        response = jsonify(status=404)
        response.headers.add('Access-Control-Allow-Origin', '*')    
        return response
    
    response = jsonify(calls=calls, status=200)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)