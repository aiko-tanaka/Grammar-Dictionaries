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

**Limitations**  
Do note however that these still do not account for every conjugation possible because most of these sites list the conjugations relative to Ichidan Verbs (v1). For example: https://nihongonosensei.net/?p=18790 (～されるまま／されるがままに), the yomichan entries that can be automatically made from these are されるまま and されるがままに.  
However, take a look the example sentences. You'll see **言われるがままに**, unfortunately, they only listed ～されるまま／されるがままに as the entries and not **われるがままに**, which makes sense because otherwise you'll have to list every conjugation for the godan verbs (v5), which is a huge pain in the ass and probably why they didn't do it and also why I won't (just takes too much time for marginal benefit). IMO, immersion would bridge this gap anyway. (but if someone can think of a solution to this, feel free to edit and reupload any of the dicts).

Again, since these dictionaries aren't perfect and yomichan's deconjugation isn't perfect either (particularly for very colloquial expressions), you could try deconjugating(or converting a godan conjugation to an ichidan/suru-verb conjugation) something that looks like a grammar point before looking it up on yomichan (it works sometimes).
  
  
## Interested in creating your own grammar dict?  
In case some people might want to scrape other sites to create another dict, I also uploaded the scripts I used just to give you guys an idea. It's a really half-assed script though and I bet you guys can come up with a better one.  

Btw, when I first tried to scrape Nihongo Sensei and Nihongo Kyoushi, at first I only intended to create a dict containing only the grammar points for yomichan parsing and its only content would be the link, but then I went further for some reason. If you're a bit short on time, just keep in mind that the content isn't even the most important part of grammar dictionaries, it's the **parsing** part (because tbh, you'd be surprised what things count as a grammar point) that's most important. After yomichan has parsed whatever shit that is, you could simply right-click and google the grammar point, or if you have the link then click the link. That'd be the most bare-bones but still very powerful grammar dict.  
Remember to share them though, even if they're just barebones :D

## For those interested in the inner workings of the dicts:  
The 4th entry of a dictionary entry represents its 'part of speech' (e.g. vs, vk, v1, v5, adj-i, etc., empty=noun). It's responsible for yomichan's deconjugation stuff.

## For those interested in completing the DOJG and Nihongo Kyoushi dicts, these are what you'll need to do:  
1. Complete the part of speech info (classify according to these: vs, vk, v1, v5, adj-i), afaik, only these 5 part of speech markers work with yomichan, if it's a noun or already conjugated, leave it blank
2. There are some entries that would be worth duplicating and deconjugating. For example, let's say there's a grammar point called をちゅうしんにする, if you add its p.o.s., i.e. `vs` (suru-verb), yomichan would catch をちゅうしんにして, をちゅうしんにしました, etc.   
However, for example the grammar point `ないこともない`, if you add its p.o.s., `adj-i`, it'd catch ないこともなくて, ないこともなく, etc. but it won't catch `ないこともありません` , in order for yomichan to catch that, you'll have to create a fake entry, `ないこともある`.
