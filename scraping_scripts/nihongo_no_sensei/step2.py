# part 2 of the code
# reads the output JSON from step1.py

from util import try_access_site, strip_tags, generate_reading

from bs4 import BeautifulSoup

from collections import OrderedDict

import re
import json

# go through each JLPT level 1 by 1 instead of all of the levels (I separated the single output file from step 1 into 5 files by JLPT level)
# to avoid connection scraping errors (i.e. having to start all over again each time)
# NOTE: N4 represents N4 and N5 (as is reflected in the site)

jlp_level = 'N0' # change this from N1, N2, etc. depending on what level you are processing
full_path = r'scraping_dump_preliminary_{}.json'.format(jlp_level)

with open(full_path, 'r', encoding='UTF8') as fh:
    initial_scraping_data : dict = json.load(fh, object_pairs_hook=OrderedDict)

print(len(initial_scraping_data))

final_dict = []

ctr = 0

for raw_grmr_pt, initial_dict_data in initial_scraping_data.items():
    """
    raw grammar point and raw reading here means that the grammar point hasn't been split yet
    along the ~ and /'s e.g. ～いかんで／いかんでは／いかんによっては (as opposed to each of them)
    """
    raw_grmr_pt : str
    initial_dict_data : dict

    link = initial_dict_data['link']
    level = initial_dict_data['level']
    raw_reading = initial_dict_data['reading']

    specific_site = try_access_site(link)
    souuup = BeautifulSoup(specific_site, features='html.parser')


    # just go with clearfix and pick the div with the largest number of chars and contains 意味, 接続, etc
    all_page_clearfix = souuup.find_all('div', attrs={'class': 'clearfix'})
    # print(type(all_page_clearfix[0]))
    all_page_clearfix = [r for r in all_page_clearfix if '意味' in str(r) and '接続' in str(r)]
    all_page_clearfix = str(all_page_clearfix).split('itemprop="headline name">')[-1].replace('説明', '')
    all_page_clearfix = all_page_clearfix.split('(adsbygoogle = window.adsbygoogle || []).push({});')[0]
    all_page_clearfix = re.sub(r'201(.*?)日本語の文法', '', all_page_clearfix).replace('\n\n\n', '').strip()
    all_page_clearfix = re.sub(r'202(.*?)日本語の文法', '', all_page_clearfix).replace('\n\n\n', '').strip()

    # reibun_contents = '\n'.join([r for r in reibun_contents if '<strong>' in r or 'font-weight:bold' in r])
    # apparently, I can use $1 or \1 to reference the nth match? I think
    regx_struct_content = r'", {"type": "structured-content", "content": [ {"tag": "span", "style": {"fontWeight": "bold"}, "content": \1} ] }, "'
    # all_page_clearfix = re.sub(r'<strong>(.*?)</strong>',  regx_struct_content, all_page_clearfix)
    # all_page_clearfix = re.sub(r'<span style=\"font-weight\:bold\">(.*?)</span>', regx_struct_content, all_page_clearfix)

    all_page_clearfix = re.sub(r'<strong>(.*?)</strong>', r'-----\1-----', all_page_clearfix)
    all_page_clearfix = re.sub(r'<span style=\"font-weight\:bold\">(.*?)</span>', r'-----\1-----',
                               all_page_clearfix)

    all_page_clearfix = strip_tags(all_page_clearfix).replace('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n', '')
    print(all_page_clearfix)

    print(link)
    print('\n')


    # raise error if any of the variables is empty
    if not any ([all_page_clearfix]):
        print(f'-------error found at {raw_grmr_pt} @ link: {link}-------------------------------' )
        raise NotImplementedError


    dict_tag = raw_grmr_pt
    global_tag = f'日本語教師―{level}'

    raw_grmr_pt = re.sub(r'\（[^)]*\）', '', raw_grmr_pt) # remove everything bn parenths
    specific_grmr_pts = raw_grmr_pt.split('／')

    raw_reading = re.sub(r'\（[^)]*\）', '', raw_reading)  # remove everything bn parenths
    specific_readings = raw_reading.split('／')

    for specific_pt in specific_grmr_pts:


        final_grmr_pt = specific_pt.replace('～', '')
        if len(specific_grmr_pts) == 1:
            final_reading = specific_readings[0]

        else:
            final_reading = generate_reading(final_grmr_pt)


        # {"type": "structured-content", "content": [ {"tag": "span", "style": {"fontWeight": "bold"}, "content": \1} ] }
        # [all_page_clearfix, f"\n\nlink:{link}\n\n---END---"]
        link_string = f"\n\nlink:{link}\n\n---END---"
        better_struct_cont = [{"type": "structured-content", "content": [ all_page_clearfix, link_string ] }]
        temp_list = [final_grmr_pt,
                     final_reading,
                     raw_grmr_pt, "", 0,
                     better_struct_cont,
                     0,
                     global_tag]

        final_dict.append(temp_list)

    print('\n------------------------------------')

    # ctr += 1
    # if ctr >= 10:
    #     break

######## --------------------------------------------------------

out_file_jlpt_level = 'N0'
out_file = f'nihongo_no_sensei_{out_file_jlpt_level}.json'

with open(out_file, 'w', encoding='UTF8') as fh:
    json.dump(final_dict, fh, indent=4, ensure_ascii=False)
