import requests


def get_quotes_stock(country="brazil", code="RADL3", start_date ="09/27/2022", end_date="07/18/2023"):
    url="http://api.scraperlink.com/investpy/?email=your@email.com&"+\
        "type=historical_data&" +\
        "product=stocks&" +\
        f"country={country}&" +\
        f"symbol={code}&" +\
        f"from_date={start_date}&" +\
        f"to_date={end_date}"
    response = requests.get(url)
    if response.status_code == 200:
        # The request was successful.
        data = response.json()
    else:
        # The request was not successful.
        raise ValueError("Problema ao consumir API erro: ", response.status_code)
    
    return data