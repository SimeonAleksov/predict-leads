# Scrape

## Clone the repository

1. Clone the repository
```shell
git clone https://github.com/SimeonAleksov/predict-leads
```

### Install the requirements

1. Change directory 
```shell
cd predict-leads
```
2. Active a virtual environments
```shell
python -m venv venv
source venv/bin/activate
```

3. Install the requirements

```shell
pip install -r requirements.txt
```


# Running the scripts

Running for a single client:
```shell
python main.py --client DEEL
python main.py --client SCALE
python main.py --client WEBFLOW
```

Running for all clients

```shell
python main.py --client ALL
```

## Additional notes

- This repository contains examples of scraped data `examples/...`. 
- When running the script locally data is saved in `data/..`.

# Contributing

- Adding a new scrape client is simple, just add a new package in `scrapers/`.
- Extend the `scrapers.constants.Scraper.NEW_CLIENT` and update the factor.