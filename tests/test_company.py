import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../'))

from web_scraping.company import Company
import pprint
import sys

def test_company_succes1():
    succes_companys_no = ['7211','3231','7601','6850','7552','3269','6752','7182','8411','3877','7270','9021','7816','7203','5201','9997',
    '9404','6800','4204','6506','7261']
    com =   Company()
    test_companys_no = com.company_no_set()
    print("\n")
    print("succes_companys_no")
    pprint.pprint(succes_companys_no,width=100,compact=True)
    print("test_companys_no")
    pprint.pprint(test_companys_no,width=100,compact=True)
    assert succes_companys_no == test_companys_no

