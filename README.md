# Rare Sats Scraper and Fusion Preview Gallery

This project contains a Python script that scrapes the Rare Sats listings from Magic Eden's Ordinals marketplace. The script uses Selenium to interact with the webpage, collect SAT numbers from visible listings, and save them to a file. Additionally, it includes a simple web application to preview the SAT numbers using HTML, CSS, and JavaScript.

The preview gallery showcases the previews for those Sats as Fusions from the ordinals collection **[Fusion](https://magiceden.io/ordinals/marketplace/fusion-art)** by **Billy Restey**. It collects rare SATs listing from Magic Eden through a Python script and saves them to a local text file, which can be used to display them in a modified version of the Fusion Preview (**[ord.io](https://www.ord.io/71122895)**).

The app should eventually use the Magic Eden Ordinals API and is currently applying for an API key.


## Features

- Scrapes SAT numbers from Magic Eden's Ordinals marketplace.
- Uses Selenium for web scraping and dynamic content handling.
- Collects SAT numbers in real-time as you manually scroll the page.
- Saves the collected data to a file in a Python list format.
- Includes a web application to preview the collected SAT numbers.
- Showcases the Fusion collection by Billy Restey.
- Plans to integrate with Magic Eden Ordinals API (API key application in progress).

## Requirements

- Python 3.x
- Google Chrome browser
- ChromeDriver