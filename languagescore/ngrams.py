from collections import Counter
from itertools import chain

def word_ngrams(n, s):
    """Returns list of n-length ngrams in string s"""
    return [s[i:i+n].upper() for i in range(len(s)-n+1)]

def file_ngrams(fpath, n):
    with open(fpath, 'r') as f:
        ngrams = [word_ngrams(n, w.strip()) for w in f]
    f.closed
    return list(chain.from_iterable(ngrams))

def ngram_freqs(fpath, n):
    ngrams = file_ngrams(fpath, n)
    total = len(ngrams)
    return {ngram: count/total*100 for ngram, count in Counter(ngrams).most_common()}

def write_outfile(fpath, ngram_freqs):
    with open(fpath, 'w') as outfile:
        for ngram, freq in ngram_freqs.items():
            outfile.write(ngram + '\t' + str(freq) + '\n')
    outfile.closed

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description='Parse ngrams from corpus into list of ngram probabilities')
    parser.add_argument('size', type=int, help='ngram size')
    parser.add_argument('corpus', type=str, help='newline-delimited corpus file')
    parser.add_argument('outfile', type=str, help='output filename')

    args = parser.parse_args()
    ngrams = file_ngrams(args.corpus, args.size)
    freqs = ngram_freqs(ngrams)
    write_outfile(args.outfile, freqs)
