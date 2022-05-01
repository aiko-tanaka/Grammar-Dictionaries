## Grammar-Dictionaries

Dictionaries: https://drive.google.com/drive/folders/1zLqkD6KTf7c6jHp3gzJQtHYWdLhN72Bq

Demo: https://www.youtube.com/watch?v=EkgBnkupuVQ **(turn the captions on)**

## The dicts:  
website | Yomichan dict name | nickname | With or w/o deconjugation support   
https://nihongonosensei.net/?page_id=10246 | 毎日のんびり日本語教師 | Nihongo no sensei | Y  
https://nihongokyoshi-net.com/jlpt-grammars/ | JLPT文法解説まとめ | Nihongo Kyoushi | N  
https://itazuraneko.neocities.org/grammar/donnatoki/mainentries.html | どんなときどう使う 日本語表現文型辞典 | Donna Toki | Y  
https://itazuraneko.neocities.org/grammar/dojgmain.html | 日本語文法辞典(全集) | DOJG | N  

**Additional dict info:**   
Only 毎日のんびり日本語教師 and どんなときどう使う 日本語表現文型辞典 have deconjugation support.  

**DOJG** - the first dict I made. Its entries aren't complete since I made this dict from the itazuraneko anki deck (as opposed to web scraping, which i used on the other dicts). I manually removed some entries which I thought were too easy and might simply clog your yomichan search results; Incomplete readings; no external links  
**Donna Toki** - non-clickable external links  
**Nihongo Kyoushi** - I used a different web scraping script here (as opposed to Nihongo no sensei), as a result some of the entries might have missing examples sentences, but whatever, just click the links; clickable links  
**Nihongo no sensei** - most complete of the four with the best formatting; clickable links; I also suggest you download a few of shoui's chinese dicts just for this specific dict because its 意味 section is in chinese  


## How to study grammar/how to use the dicts:  
I'd still recommend you go through a basic grammar guide first, even with these dicts in hand.  
After that, i'd recommend that you at least skim through a list of grammar points to get a feel for what they look like. Then look up the grammar points you come across in your immersion and create cards as necessary. I've found that I rarely need to google grammar points now after using these dicts.
  
  

In case some people might want to scrape other sites to create another dict, I also upload the scripts I used just to give you guys an idea. It's a really half-assed script though and I bet you guys can come up with a better one.

## For those interested in the inner workings of the dicts:  
The 4th entry of a dictionary entry represents its 'part of speech' (e.g. vs, vk, v1, v5, adj-i, etc., empty=noun). It's responsible for yomichan's deconjugation stuff.

## For those interested in completing the DOJG and Nihongo Kyoushi dicts, these are what you'll need to do:  
1. Complete the part of speech info (classify according to these: vs, vk, v1, v5, adj-i), afaik, only these 5 part of speech markers work with yomichan, if it's a noun or already conjugated, leave it blank
2. There are some entries that would be worth duplicating and deconjugating. For example, let's say there's a grammar point called をちゅうしんにする, if you add its p.o.s., i.e. `vs` (suru-verb), yomichan would catch をちゅうしんにして, をちゅうしんにしました, etc.   
However, for example the grammar point `ないこともない`, if you add its p.o.s., `adj-i`, it'd catch ないこともなくて, ないこともなく, etc. but it won't catch `ないこともありません` , in order for yomichan to catch that, you'll have to create a fake entry, `ないこともある`.
