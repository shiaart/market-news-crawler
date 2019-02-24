# Company Insight Utility
#### Built by Peter Dulworth for Nesh

### Submission Video

Explanation video: https://www.youtube.com/watch?v=MOjehyxotzU&feature=youtu.be

### Installation

#### 1. Clone the repo
Clone the repo or download the zip.
#### 2. Install frontend dependencies
```bash
cd frontend
npm install
```
#### 3. Install backend dependencies
```bash
pip install -r requirements.txt
```

Note: I developed this application for Google Chrome. Most testing has been done with Chrome 72.0.3626.109.

Note: This application uses python 3.7.

### Running the app
First start the backend, then start the front end:

#### Back End
```bash
python backend/server.py
```
The API will now be live at http://localhost:5000

To test calls to the backend without the front-end you can open terminal and run.

```
curl -i http://localhost:5000/symbol/oxy
```


#### Front End
```bash
cd frontend
npm start
```
The website will now be live at: http://localhost:3000/

### Important Note
<strong>If at anytime data fails to load, it is likely because your IP has been blocked by seeking alpha by their web scraping watch dog. To accomodate this I created an endpoing on the backend that will generate a proxy for the backend to use which in some cases will be able to get around the watch dog. To use a proxy simply open a new tab and navigate to http://localhost:5000/generate/proxy. You can visit this URL as many times as you would like and it will generate a new proxy each time. </strong>

### Features

- stock overview
    - includes last stock price, net change in price in past day and percent change in price over past day
- company description
    - includes a brief description of the company (pulled from their SEC filing)
- financial numbers
    - includes important financial numbers
- news articles
    - includes recently published news articles relating to the given company
- Analysis of Earnings Call Transcript 
    - when did the call happen
    - who all was on the call
    - who Spoke the Longest

### Ideas for future updates

- handle mobile better
- better error handling for scraper (rn if a website changes will break very easily)
- i had trouble getting access to the full earnings calls
- seeking alpha had too much javascript

Challenges
- parsing the transcripts is hard because there is so little to work with
- dealing with authentication