
from urllib import request

def get_cik():
    url='https://www.sec.gov/include/ticker.txt'
    surl = request.urlopen(url).read()
    cik = dict()
    for i in str(surl).replace("b'",'').split('\\n'):
        cik[i.split('\\t')[0].upper()] = i.split('\\t')[1]
    return(cik)