import configparser
from daftlistings import Daft, Location, SearchType

config = configparser.ConfigParser()
config.read('config.ini')
searchParams = config['SEARCH PARAMS']
loc = Location[searchParams['Location']]
type = SearchType[searchParams['SearchType']]
minBeds = searchParams['MinBeds']
maxPrice = searchParams['MaxPrice']

daft = Daft()
daft.set_location(loc)
daft.set_search_type(type)
daft.set_max_price(maxPrice)
daft.set_min_beds(minBeds)

listings = daft.search()
for listing in listings:
    print(listing.title)
    print(listing.price)
    print(listing.daft_link)