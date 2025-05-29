# 🤖📚 Book Bot

_“To read or not to read? That is the question. But first, let’s count the words.”_

Welcome to **Book Bot** – your friendly, slightly nerdy Python assistant that munches through novels and spits out juicy statistics about word and character usage. Think of it as Grammarly’s introverted cousin who lives in the library and loves numbers a bit *too much*.

## 📖 What Does It Do?

Book Bot takes a novel (plain text only, please), analyzes it, and gives you a detailed statistical report so thorough even Sherlock Holmes would say, “Whoa, calm down.”

Here's what it reports:

- Total word count 📊  
- Top 10 most frequent words 🏆  
- Character usage stats 🔠 (including special characters, if any)  
- (Optional) Exposes your favorite author’s overuse of the word “very” 👀  

## 🚀 How to Run It

1. Clone this repo like it’s 1999:

   ```bash
   git clone https://github.com/yourusername/book-bot.git
   cd book-bot
   ```

2. Make sure you have Python 3 installed. If you don’t, go download it. We’ll wait. 🕰️

3. Drop your `.txt` file of the novel into the project folder. (We recommend starting with something public domain, like from [Project Gutenberg](https://www.gutenberg.org/).)

4. Run the bot:

   ```bash
   python book_bot.py /path/to/your/book.txt
   ```

5. Marvel at the statistical wonderland generated just for you. It will look something like this:

```
============ BOOKBOT ============
Analyzing book found at /books/frankenstein.txt...
----------- Word Count ----------
Found 75767 total words
----------- Top 10 Words ----------
the: 4192
and: 2832
i: 2655
of: 2627
to: 2038
my: 1660
a: 1357
in: 1120
that: 997
was: 960
--------- Character Count -------
e: 44538
t: 29493
a: 25894
o: 24494
i: 23927
n: 23643
s: 20360
r: 20079
h: 19176
d: 16318
l: 12306
m: 10206
u: 10111
c: 9011
f: 8451
y: 7756
w: 7450
p: 5952
g: 5795
b: 4868
v: 3737
k: 1661
x: 691
j: 497
q: 325
z: 235
æ: 28
â: 8
ê: 7
ë: 2
ô: 1
============= END ===============
```

## 📦 Requirements

- Python 3.7+
- No external dependencies (yet). We like to keep things simple, like a haiku:

  ```
  Pure Python, it runs  
  Clean, without pip install pain  
  Just you and your book
  ```

## 🧠 Why?

Because we were tired of just **reading** books. We wanted to **interrogate** them.  
_"Why do you use ‘suddenly’ 274 times, Charles? Are you okay?"_

Also, data is cool. And books are cool. So... Book Bot.

## 🤓 Coming Soon

- Support for multiple files  
- Stop-word filtering  
- Nicer output formats (JSON, CSV, maybe even interpretive dance)  
- Integration with your favorite e-reader? (We dream big.)

## 🧙‍♂️ Contributing

Contributions welcome! If you want to help make Book Bot smarter, faster, or just funnier, fork away and send us a pull request. Bonus points for puns in your commit messages.

## 📜 License

MIT License – because books are meant to be shared, and so is code.

---

Made with 🧠 + ❤️ by book lovers, for data nerds.
