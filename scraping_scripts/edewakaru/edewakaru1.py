import util
import json
import copy
import re

from bs4 import BeautifulSoup
from collections import OrderedDict

final_dict = []

for i in range(1,13):
    master_site = ''
    if i == 1:
        #################################################################--------------------------------------
        master_site = r'https://www.edewakaru.com/archives/cat_116866.html' #chuukyuu
    elif i > 1:
        master_site = f'https://www.edewakaru.com/archives/cat_116866.html?p={i}'
    # print(master_site)

    try:
        master_page = util.try_access_site(master_site)
    except Exception as e:
        raise
    master_soup = BeautifulSoup(master_page, features='html.parser')

    article_body = master_soup.find_all('div', attrs={'class': 'article-body'})
    article_headers = master_soup.find_all('header', attrs={'class': 'article-header'})


    # print(len(article_body), len(article_headers))
    # if not len(article_body) == len(article_headers):
    #     print(f'ERROR1, site:{specific_site_link}')
    #     raise IndexError

    for index, article in enumerate(article_body):
        # print(article)
        specific_header : str = article_headers[index].find_all('a')[0].contents[0]
        # print(specific_header)

        specific_site_link = article_headers[index].find_all('a')[0]['href']
        print(specific_site_link)

        raw_grmr_pt = specific_header.split('｜')[0]
        local_tag = copy.deepcopy(raw_grmr_pt)
        print(raw_grmr_pt)

        raw_grmr_pt = re.sub(r'[①②③④⑤⑥⑦]*', '', raw_grmr_pt)
        raw_grmr_pt = re.sub(r'\（[^)]*\）', '', raw_grmr_pt)
        raw_grmr_pt = re.sub(r'\([^)]*\)', '', raw_grmr_pt)

        print(local_tag)

        #################################################################--------------------------------------
        level = '絵でわかる初級文法'
        #################################################################--------------------------------------

        article = str(article)
        article = article.strip()
        article = article.replace('<br>', '')
        article = article.replace('<br/>', '\n')
        # article = article.replace(' ', '')
        # article = re.sub(r'([\n])', '', article)
        article = article.replace('\n\n\n\n', '\n')
        article = article.replace('\n\n\n\n\n', '\n')
        article = article.replace('\n\n\n\n\n\n', '\n')
        article = article.split('【日本語文法リスト】')[0]

        article = re.sub(r'<span style="color: rgb(255, 0, 0);">(.*?)</span>', r'-----\1-----', article)
        # article = re.sub(r'<spanstyle="color: rgb(255, 0, 0);">(.*?)</span>', r'-----\1-----', article)
        article = re.sub(r'<b>(.*?)</b>', r'-----\1-----', article)
        article = re.sub(r'<strong>(.*?)</strong>', r'-----\1-----', article)

        # article = re.sub(r'<iframe frameborder="0" scrolling="no" src="(.*?)"></iframe>', r'\b\b\b', article)

        article = util.strip_tags(article)
        article = specific_header + article

        # TODO: <span style="color: rgb(255, 0, 0);">なろうとも</span>
        # TODO: replace regex @ N++ -----\1-----

        # https://gist.github.com/terrancesnyder/1345094
        article = re.sub(r'\（[ぁ-ゔゞ゛゜ー]{1,6}\）', '', article)
        print(article)

        specific_grmr_pts = raw_grmr_pt.split('・')
        for specific_pt in specific_grmr_pts:
            possible_further_pts = specific_pt.split('〜')
            print(possible_further_pts)

            for final_pt in possible_further_pts:
                if final_pt:
                    final_grammar_pt = final_pt
                    final_reading = util.generate_reading(final_grammar_pt)

                    link_string = {"tag": "a", "href": specific_site_link, "content": "edewakaru link" }

                    better_struct_cont = [ {  "type": "structured-content", "content": [article, "\n\n", link_string, "\n---END---"] }   ]
                    temp_list = [
                        final_grammar_pt,
                        final_reading,
                        local_tag, "", 0,
                        better_struct_cont,
                        0,
                        level
                    ]

                    final_dict.append(temp_list)
        print(i)
        print('-----------------------------------\n')

    # if i == 1:
    #     break

if False:
    #################################################################--------------------------------------
    with open('term_bank_test_3.json', 'w', encoding='UTF8') as fh:
        json.dump(final_dict,
                  fh,
                  indent=4,
                  ensure_ascii=False)
