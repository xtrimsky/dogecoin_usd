__author__ = 'Andrei Pervychine'
import urllib.request
import sys

## returns float value in USD of 1 dogecoin ##
def find_dogecoin_value(dogecoins_amount=10000):

    ## thank you coinmill.com for providing this value to us via an rss feed ##
    response = urllib.request.urlopen("http://coinmill.com/rss/USD_XDG.xml");

    ## converting response to html string ##
    html = ''
    for html_line in response.readlines():
        html += html_line.strip().decode('utf-8')
    response.close()

    ## text between which we find our data ##
    string_to_search = 'XDG ='
    end_search = 'USD'

    ## any way to optimize this ? this is my first python code ever, open to suggestions :)
    pos = html.find(string_to_search)
    if pos == -1:
        return 0

    start = pos + len(string_to_search)
    tmp = html[start:start+21]
    tmp2 = tmp.find(end_search)

    return float(tmp[:tmp2].strip()) / 10000 * float(dogecoins_amount)

## getting arguments passed ##
if len(sys.argv) > 1:
    amount = sys.argv[1]
else:
    amount = 10000

data = find_dogecoin_value(amount)
if data == 0:
    print("no data found")
else:
    print(str(amount)+" dogecoins = "+str(data)+" USD")
