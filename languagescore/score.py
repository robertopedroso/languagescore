import functools
import operator
import ngrams

def score_word(ngram_freqs, word):
    word_bigrams = ngrams.word_ngrams(2, word)
    bigram_freqs = [(ngram_freqs[ngram] if ngram in ngram_freqs else 1e5) for ngram in word_bigrams]
    return functools.reduce(operator.mul, bigram_freqs)

def score_words(ngram_freqs, words):
    return sum([score_word(ngram_freqs, word) for word in words])

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description='Score word ngram probabilities from language corpus')
    parser.add_argument('corpus', type=str, help='newline-delimited corpus file')
    parser.add_argument('size', type=int, help='ngram size')
    parser.add_argument('text', type=str, help='word or words to score')
    args = parser.parse_args()

    # split given text into individual words, remove words less than ngram size
    words = [word.strip() for word in args.text.split(' ')]
    words = [word for word in words if len(word) >= args.size]

    # compute corpus freqs and score
    ngram_freqs = ngrams.ngram_freqs(args.corpus, args.size)
    score = score_words(ngram_freqs, words)

    print("Given text: " + args.text)
    print("Score: " + str(score))
