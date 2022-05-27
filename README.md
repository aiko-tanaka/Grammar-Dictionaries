# Yomichan Grammar Dictionaries

[Link to the Dictionaries](https://drive.google.com/drive/folders/1zLqkD6KTf7c6jHp3gzJQtHYWdLhN72Bq)

[Youtube Demo](https://www.youtube.com/watch?v=EkgBnkupuVQ) **(turn the captions on)**

## The dicts
Website | Yomichan dict name | Deconjugation support | 
:-- | :-- | :-- 
[nihongo no sensei](https://nihongonosensei.net/?page_id=10246) | 毎日のんびり日本語教師 | Y  
[nihongo kyoshi](https://nihongokyoshi-net.com/jlpt-grammars/) | JLPT文法解説まとめ | N  
[donna toki](https://itazuraneko.neocities.org/grammar/donnatoki/mainentries.html) | どんなときどう使う 日本語表現文型辞典 | Y  
[dojg](https://itazuraneko.neocities.org/grammar/dojgmain.html) | 日本語文法辞典(全集) | N  

### **Additional dict info:**   
Only `毎日のんびり日本語教師` and `どんなときどう使う 日本語表現文型辞典` have deconjugation support.  
If some of the dicts fail to import, check that you're using at least Yomichan version `22.4.4.0`.

* **DOJG** - the first dict I made. Its entries aren't complete since I made this dict from the itazuraneko anki deck (as opposed to web scraping, which i used on the other dicts). I manually removed some entries which I thought were too easy and might simply clog your yomichan search results; Incomplete readings; no external links  
* **Donna Toki** - non-clickable external links  
* **Nihongo Kyoushi** - I used a different web scraping script here (as opposed to Nihongo no sensei), as a result some of the entries might have missing examples sentences, but whatever, just click the links; clickable links  
* **Nihongo no sensei** - most complete of the four with the best formatting; clickable links; I also suggest you download a few of shoui's chinese dicts just for this specific dict because its `意味` section is in chinese  


## How to study grammar/how to use the dicts
### Usage   
* (For beginners) Go through a basic grammar guide first, even with these dicts in hand.  
Unless you've had some basic grammar study and a bit of immersion experience, some of the dictionaries might simply confuse you so do that first.
* (For beginners) I recommend going through Tae Kim first, then Cure Dolly. 
* (For beginners) For Cure Dolly in particular I recommend that you at least go through the first 20-30 or so videos just so that when you come across a grammar point, you aren't just blindly memorizing 'rules', instead you realize that most of the time, these 'grammar points' can make sense when you look at their components.  
  
  
* Skim through a list of grammar points to get a feel for what they look like. (i.e. go to one of the sites I listed above and try hovering over those grammar points, then try hovering over the grammar points in the context of the sentence, similar to what I did on my youtube demo).
* Then look up the grammar points you come across in your immersion and create cards as necessary. The more you immerse and look stuff up, the more you'll start to get a feel of what structures look like a grammar point, tbh, you'd probably surprised that what looks like some random string of hiragana scribbles actually turns out to be a grammar point.  
  
* When you common across patterns without an adequate explanation inside the grammar dicts/monolingual dicts, just right click whatever it is that yomichan parsed and do a google search (something like `<grammar_pt> 文法解説`). I use a plugin called [Context Menu Search](https://chrome.google.com/webstore/detail/context-menu-search/ocpcmghnefmdhljkoiapafejjohldoga) to make such searches easier.
* Keep in mind that the main reason that I made these dictionaries is because I dislike the 10 seconds it takes to google a grammar point, which you aren't even sure is a grammar point. Also when googling `<grammar_pt> 文法解説`, they almost always point to the same 2-4 sites anyway, so why not turn those sites into a yomichan dictionary. With that said, do not expect to find a lot of info about grammar inside these dictionaries. Most immersion learners would probably agree anyway that these grammar points aren't even grammar most of the time, instead, they're usually common phrases, expression strategies or even vocabulary.



### Limitations 
* Do note however that these still do not account for every conjugation possible because most of these sites list the conjugations relative to `Ichidan Verbs (v1)` and `suru-verbs (vs)`. For example: https://nihongonosensei.net/?p=18790 `(～されるまま／されるがままに)`, the yomichan entries that can be automatically made from these are `されるまま` and `されるがままに`.  
However, take a look the example sentences. You'll see **言われるがままに**, unfortunately, they only listed `～されるまま／されるがままに` as the entries and not **われるがままに**, which makes sense because otherwise you'll have to list every conjugation for the `godan verbs (v5)`, which is a huge pain in the ass and probably why they didn't do it and also why I won't (just takes too much time for marginal benefit). IMO, immersion would bridge this gap anyway. (but if someone can think of a solution to this, feel free to edit and reupload any of the dicts).  

* For grammar points structured as `なになに～なになに`, e.g. **〜か〜ないかのうちに**, it's usually best to break them apart into their own entry (e.g. one entry for **か** another for **ないかのうちに**). It's obvious though that か is just too vague and common to be an entry so i only made `ないかのうちに` as an entry. Feel free to send a PR though if you think I've made a mistake with some of the entries (probably did), but do note that having too many vague entries can make yomichan hard to navigate (e.g. `なになに～なに`, scanning for **ない** would give you a LOT of entries, most of which you probably already know anyway).

* These dictionaries aren't perfect and yomichan's deconjugation isn't perfect either (particularly for very colloquial expressions), you could try deconjugating(or converting a godan conjugation to an ichidan/suru-verb conjugation) something that looks like a grammar point before looking it up on yomichan (it works sometimes). If you're a bit more advanced, you could try adding regex replacements rules inside yomichan or even editing the [deinflection json file](https://github.com/FooSoft/yomichan/blob/master/ext/data/deinflect.json).
  
  
## Interested in creating your own grammar dict?  
* In case some people might want to scrape other sites to create another dict, I also uploaded the scripts I used just to give you guys an idea. It's a really half-assed script though and I bet you guys can come up with a better one.  

* Btw, when I first tried to scrape Nihongo Sensei and Nihongo Kyoushi, at first I only intended to create a dict containing only the grammar points for yomichan parsing and its only content would be the link, but then I went further for some reason. If you're a bit short on time, just keep in mind that the content isn't even the most important part of grammar dictionaries, it's the **parsing** part (because tbh, you'd be surprised what things count as a grammar point) that's most important. After yomichan has parsed whatever shit that is, you could simply right-click and google the grammar point, or if you have the link then click the link. That'd be the most bare-bones but still very powerful grammar dict.  
Remember to share them though, even if they're just barebones :D

### Here are a few of the sites that I think would be worth looking into:  
* https://www.edewakaru.com/archives/cat_179055.html  
* https://jlptgrammarlist.neocities.org/  
* https://jn1et.com/jlpt/  
* https://nihon5-bunka.net/japanese-grammars/  
* https://japanese-bank.com/jlpt-grammar-all/  
* https://itazuraneko.neocities.org/grammar/masterreference.html#handbook  


## For those interested in the inner workings of the dicts:  
* The [4th entry](https://github.com/aiko-tanaka/Grammar-Dictionaries/blob/main/nihongo_kyoushi/term_bank_1.json#L270) of a dictionary entry represents its `part of speech(p.o.s.)` `(e.g. vs, vk, v1, v5, adj-i, empty=noun)`. It's responsible for yomichan's deconjugation stuff.

## For those interested in completing the DOJG and Nihongo Kyoushi dicts, these are what you'll need to do:  
* (Send me a message first if you plan to edit any of the dicts just to ensure that we aren't doing something redundant, I'm currently editing nihongo kyoushi, might take a few months)

1. Complete the part of speech info (classify according to these: `vs, vk, v1, v5, vz, adj-i`), afaik, only these 6 part of speech markers work with yomichan (according to the [yomichan deinflection rules](https://github.com/FooSoft/yomichan/blob/master/ext/data/deinflect.json) or [the schema](https://github.com/FooSoft/yomichan/blob/master/ext/data/schemas/dictionary-term-bank-v3-schema.json#L304)), if it's a noun or already conjugated, leave it blank
2. There are some entries that would be worth duplicating and deconjugating. For example, let's say there's a grammar point called `をちゅうしんにする`, if you add its p.o.s., i.e. `vs` `(suru-verb)`, yomichan would catch `をちゅうしんにして, をちゅうしんにしました, etc.`   
However, for example the grammar point [ないこともない](https://github.com/aiko-tanaka/Grammar-Dictionaries/blob/main/nihongo_kyoushi/term_bank_2.json#L2423), if you add its p.o.s., `adj-i`, it'd catch `ないこともなくて, ないこともなく, etc.` but it won't catch `ないこともありません` , in order for yomichan to catch that, you'll have to create a fake entry, [ないこともある](https://github.com/aiko-tanaka/Grammar-Dictionaries/blob/main/nihongo_kyoushi/term_bank_2.json#L2445).
3. You might want to check [this](https://github.com/FooSoft/yomichan/blob/master/test/data/dictionaries/valid-dictionary1/term_bank_1.json) and the other grammar dicts for examples on how to format entries.
4. Send a PR I guess

## Corrections / Incomplete Info
For all dictionaries: I used web scraping for all of the dicts except DOJG so there might be a few missing entries and parsing mistakes. For some of the entries, I used a [script](https://github.com/aiko-tanaka/Grammar-Dictionaries/blob/main/scraping_scripts/util.py) to generate the reading when the reading info isn't available, so look out for reading mistakes. 

### DOJG
Incomplete readings(there might be some entries where the dictionary entry is also the reading), incomplete entries (particularly for `基本`), no deconjugation/p.o.s. info
### Nihongo Kyoushi
No deconjugation/p.o.s. info, missing entries (e.g. 〜上で（〜てから）), some entries have the example sentences cut off, some entries might have ads at the end; also, some entries have wildly differing HTML structures (e.g. some use tables, some have more than one 例文 sections), etc.
### Donna Toki
Might have a few entries missing, incomplete kanjification (all of donna toki's entries are in hiragana, I converted some of them into kanji but not all)
### Nihongo no Sensei
Might have a few entries missing?, a few reading mistakes maybe, a few ads at the end of some entries maybe

