# step 1, i.e. this is STEP 1,
# this code only collects the grammar points
# and the specific webpages that explain them

from util import try_access_site

from bs4 import BeautifulSoup

from collections import OrderedDict

import re
import json

# this site provides a reading column
# unfortantely, the correspondence between grammar pt and reading
# isn't always 1:1, so use the reading if the correspondence is 1:1 (e.g. 3 grammar pts separated by /'s)
# otherwise generate the reading

# grammar table master page
master_site = r'https://nihongonosensei.net/?page_id=10246'
master_page = try_access_site(master_site)

master_soup = BeautifulSoup(master_page, features='html.parser')

# fish for everything inside <table style="font-size:15px; line-height:1em;">
# only get the first five matches, because the rest are simply the same grammar points
# except in あいうえお order instead of JLPT order

jlpt_levels = master_soup.find_all('table', style=re.compile(r'font-size:15px.*?line-height:1em;'))


# <tr>
# <td>あ</td> (useless info)
# <td>Ｎ０</td> (use to indicate level)
# <td><a href="https://nihongonosensei.net/?p=3639">～あぐねる</a></td>
# <td>あぐねる</td> (reading)
# </tr>


jlpt_level_points_dict = OrderedDict()

ctr = 1
for level in jlpt_levels:
    # print(level)

    level_rows = level.find_all('tr')
    # print(len(level_rows[2]))

    print(level_rows[1].contents)
    # ['\n', <td>あ</td>, '\n', <td>Ｎ１</td>, '\n',
    # <td><a href="https://nihongonosensei.net/?p=4097">～あっての</a></td>, '\n', <td>あっての</td>, '\n']


    for col in level_rows:
        temp_dict = OrderedDict()
        col = col.contents

        level = col[3].contents[0]
        reading = col[7].contents[0]

        link = col[5].find('a')
        link = str(link)

        grmr_pt = link.split('">')[-1].split('</a>')[0]
        final_link = link.split('">')[0].split('<a href="')[-1]

        temp_dict['link'] = final_link
        temp_dict['level'] = level
        temp_dict['reading'] = reading

        jlpt_level_points_dict[grmr_pt] = temp_dict
        # print(f'reading: {reading}, lvl: {level}, link: {link}, grmr_pt: {grmr_pt}')
        # print(f'link: {link}, grmr_pt: {grmr_pt}')

    print('\n------------------------------------------\n')


with open('scraping_dump_preliminary.json', 'w', encoding='UTF8') as fh:
    json.dump(jlpt_level_points_dict, fh, indent=4, ensure_ascii=False)

