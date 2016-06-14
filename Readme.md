# Ngram-Score

This is a simple library that scores a word against a language corpus via
simple ngram analysis.

A line-separated corpus is analyzed into a list of ngram probabilities. The
given score is simply the product of the ngram frequencies within the word.
If an ngram from the word is absent from the corpus, it is simply assigned
a frequency of 1e5. If multiple words were given, they will be scored
separately and then the total score is summed together.

This is probably not a very useful library. It was written specifically to
aid in the completion of certain [Cryptopals Challenges](https://cryptopals.com/sets/1/challenges/3)
involving English plaintext analysis. There almost certainly [better approaches](http://www.inf.ufrgs.br/~ceramisch/download_files/courses/Master_FRANCE/ENSIMAG_2008_2/Ingenierie_des_Langues_et_de_la_Parole/Rapport.pdf)
than what I have implemented here, but this is useful enough for my needs.

## Module Use

```python
import languagescore.score as score
import languagescore.ngrams as ngrams

ngram_freq = ngrams.ngram_freqs('examples/english-corpus.txt', 2)
score = score_words('The dog jumped over the moon')
```

## Command-line use

```bash
python languagescore/score.py examples/english-corpus.txt 2 "Hello World"
```
