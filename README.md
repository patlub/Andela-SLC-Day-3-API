
## Getting Started

###### You can start by cloning the project:
`git clone https://github.com/patlub/Andel-SLC-Day-3-API.git`


## Prerequisites
#### Python 3
Working installation of python 3. if you don't, you can refer to this
[Intall Python 3](https://www.python.org/downloads/)

#### docopt

if you don't have it, do `pip install docopt`

## Usage
Navigate into the cloned directory and run main.py

`python main.py -i`

And you should see

```
Welcome to THE TECH NEWS APP!
Tech News At Your Finger Tips
 (type help for a list of commands.)
```

Now typing help will show all the commands

```
Documented commands (type help <topic>):
========================================
get_news  help  quit  view_sources
```
You can view the available sources by `view sources` to show

```
techcrunch
techradar
ars-technica
```

Now if you want to get headlines from techcrunch type `get_news techcrunch`

And you should see

```
Fetching News from techcrunch.................

Source:techcrunch

Author: Ingrid Lunden

Title: Worldpay, valued at $10B, confirms JPMorgan and Vantiv are trying to buy it

Article: Some consolidation is underway in the world of payment processing: Worldpay -- the giant company that says it processes 31 million mobile, online and in-store..

=========================================
Author: John Biggs

Title: Internet Stone Soup

Article: I'd wake up my computer and discover, to my dismay, that it had not. I was a full-time blogger, the little brother to the journalist, the digital-ink-stained..

=========================================

```

## Running the Tests

Navigate into the HttpClient directory and type:


`python test_http_client.py`

You should see:

`All test passed`

## Enjoy.