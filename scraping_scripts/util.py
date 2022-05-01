# install sudachipy and jaconv first

from sudachipy import tokenizer
from sudachipy import dictionary

import jaconv
import time
import random
import urllib.request

from io import StringIO
from html.parser import HTMLParser


mode = tokenizer.Tokenizer.SplitMode.C
tokenizer_obj = dictionary.Dictionary().create()

def generate_reading(text):
    """
    Generate reading of a particular japanese text
    to import: from sudachi_wrapper import generate_reading
    """
    m = tokenizer_obj.tokenize(text, mode)

    aggr = ''
    for z in m:
        aggr += jaconv.kata2hira(z.reading_form())

    return aggr

def try_access_site(site, sleep_time=0.08, num_retries=3, wait_time=15.0, timeout=5):

    initial_time = time.time()
    time_margin = 0.02

    response = None
    try:
        response = urllib.request.urlopen(site, timeout=timeout)

    except:
        for i in range(num_retries):
            lapsed_time = time.time()
            if lapsed_time - initial_time > wait_time: return None

            try:
                response = urllib.request.urlopen(site, timeout=timeout)
            except:
                # does something like random.uniform(0.06, 0.10)
                sleep_time = random.uniform(sleep_time - time_margin,
                                            sleep_time + time_margin)
                time.sleep(sleep_time)
    finally:
        return response

class MLStripper(HTMLParser):
    def __init__(self):
        super().__init__()
        self.reset()
        self.strict = False
        self.convert_charrefs= True
        self.text = StringIO()
    def handle_data(self, d):
        self.text.write(d)
    def get_data(self):
        return self.text.getvalue()

def strip_tags(html):
    s = MLStripper()
    s.feed(html)
    return s.get_data()

if __name__ == '__main__':
    # に忍びない
    print(generate_reading("と相まって"))
    print(generate_reading("に忍びない"))
    print(generate_reading("に即して"))
    print(generate_reading("に限ったことではない"))
    print(generate_reading("ないではおかない"))

