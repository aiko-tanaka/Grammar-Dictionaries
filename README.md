# Grammar-Dictionaries

Dictionaries: https://drive.google.com/drive/folders/1zLqkD6KTf7c6jHp3gzJQtHYWdLhN72Bq

Demo: https://www.youtube.com/watch?v=EkgBnkupuVQ

# The dicts:  
website | Yomichan dict name | nickname  
https://nihongonosensei.net/?page_id=... | 毎日のんびり日本語教師 | Nihongo no sensei  
https://nihongokyoshi-net.com/jlpt-gr... | JLPT文法解説まとめ | Nihongo Kyoushi  
https://itazuraneko.neocities.org/gra... | どんなときどう使う 日本語表現文型辞典 | Donna Toki  
https://itazuraneko.neocities.org/gra... | 日本語文法辞典(全集) | DOJG  

# How to study grammar/how to use the dicts:  
I'd still recommend you go through a basic grammar guide first, even with these dicts in hand.  
After that, i'd recommend that you at least skim through a list of grammar points to get a feel for what they look like.  



In case some people might want to scrape other sites to create another dict, I also upload the scripts I used just to give you guys an idea. It's a really half-assed script though and I bet you guys can come up with a better one.

# For those interesting in the inner workings of the dicts:  
The 4th entry of a dictionary entry represents its 'part of speech' (e.g. vs, vk, v1, v5, adj-i, etc., empty=noun). It's responsible for yomichan's deconjugation stuff.

# For those interested in completing the DOJG and Nihongo Kyoushi dicts, these are what you'll need to do:  
1. Complete the part of speech info (classify according to these: vs, vk, v1, v5, adj-i), afaik, only these 5 part of speech markers work with yomichan, if it's a noun or already conjugated, leave it blank
2. There are some entries that would be worth duplicating and deconjugating. For example, let's say there's a grammar point called をちゅうしんにする, if you add its p.o.s., i.e. `vs` (suru-verb), yomichan would catch をちゅうしんにして, をちゅうしんにしました, etc.   
However, for example the grammar point `ないこともない`, if you add its p.o.s., `adj-i`, it'd catch ないこともなくて, ないこともなく, etc. but it won't catch `ないこともありません` , in order for yomichan to catch that, you'll have to create a fake entry, `ないこともある`.
