# Benford_Scraper

## _A program created to verify first hand that the counter intuitive nature of the Benford's law applies to a random set of numbers, in this particular case stock prices._

## Usage
Scrapper.py grabs recent stock prices of top 500 companies from all pages of markets.businessinsider.com/index/s&p_500 and stores them in a csv. <br>
Benford.py then plots them on a graph comparing it to what would be expected if they followed Benford's Law.
Due to the volatile nature of scrapping from a website I don't control slight changes might be necessary to the code to keep it working but so far that hasen't happened.
 
## Running it
The required libraries are: ```requests```, ```bs4```, ```lxml```, ```numpy``` and ```matplotlib```. <br>
Run first Scrapper.py in order to update the data according to the website, folowed by Benford.py.

## Images

![alt text](https://github.com/gugajazz/Benford_Scraper/blob/main/Graph.png?raw=true)
