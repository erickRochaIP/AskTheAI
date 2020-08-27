from os import listdir
from os.path import isfile, join
import nltk
import sys
import string, math


FILE_MATCHES = 1
SENTENCE_MATCHES = 1


def main():

    # Check command-line arguments
    if len(sys.argv) != 2:
        sys.exit("Usage: python questions.py corpus")

    # Calculate IDF values across files
    files = load_files(sys.argv[1])
    file_words = {
        filename: tokenize(files[filename])
        for filename in files
    }
    file_idfs = compute_idfs(file_words)

    # Prompt user for query
    query = set(tokenize(input("Query: ")))

    # Determine top file matches according to TF-IDF
    filenames = top_files(query, file_words, file_idfs, n=FILE_MATCHES)

    # Extract sentences from top files
    sentences = dict()
    for filename in filenames:
        for passage in files[filename].split("\n"):
            for sentence in nltk.sent_tokenize(passage):
                tokens = tokenize(sentence)
                if tokens:
                    sentences[sentence] = tokens

    # Compute IDF values across sentences
    idfs = compute_idfs(sentences)

    # Determine top sentence matches
    matches = top_sentences(query, sentences, idfs, n=SENTENCE_MATCHES)
    for match in matches:
        print(match)


def load_files(directory):
    """
    Given a directory name, return a dictionary mapping the filename of each
    `.txt` file inside that directory to the file's contents as a string.
    """
    onlyfiles = [f for f in listdir(directory) if isfile(join(directory, f))]

    dicArquivos = dict()
    for file in onlyfiles:
        f = open(join(directory,file),"r", encoding='utf8')
        conteudo = f.read()
        dicArquivos[file] = conteudo
        f.close()

    return dicArquivos


def tokenize(document):
    """
    Given a document (represented as a string), return a list of all of the
    words in that document, in order.

    Process document by coverting all words to lowercase, and removing any
    punctuation or English stopwords.
    """
    words = [word.lower() for word in nltk.word_tokenize(document) if word not in string.punctuation and  word not in nltk.corpus.stopwords.words("english") ]

    return sorted(words)

def compute_idfs(documents):
    """
    Given a dictionary of `documents` that maps names of documents to a list
    of words, return a dictionary that maps words to their IDF values.

    Any word that appears in at least one of the documents should be in the
    resulting dictionary.
    """

    frequencias = dict()
    for file_name, word_list in documents.items():
        for word in word_list:
            if word not in frequencias:
                frequencias[word] = {file_name}
            else:
                frequencias[word].add(file_name)

    for key, value in frequencias.items():
        frequencias[key] = math.log(len(documents) / len(value))

    return frequencias


def top_files(query, files, idfs, n):
    """
    Given a `query` (a set of words), `files` (a dictionary mapping names of
    files to a list of their words), and `idfs` (a dictionary mapping words
    to their IDF values), return a list of the filenames of the the `n` top
    files that match the query, ranked according to tf-idf.
    """
    tf_idfs = []
    for filename, filewords in files.items():
        tf_idf = 0

        for word in query:
            if word not in idfs:
                continue
            idf  = idfs[word]
            tf = filewords.count(word)
            tf_idf += idf * tf
        t = (filename, tf_idf)
        tf_idfs.append(t)

    sorted_list = sorted(tf_idfs, key=lambda k: k[1])
    sorted_list.reverse()
    file_list = [item[0] for item in sorted_list]

    return file_list[:n]

def top_sentences(query, sentences, idfs, n):
    """
    Given a `query` (a set of words), `sentences` (a dictionary mapping
    sentences to a list of their words), and `idfs` (a dictionary mapping words
    to their IDF values), return a list of the `n` top sentences that match
    the query, ranked according to idf. If there are ties, preference should
    be given to sentences that have a higher query term density.
    """
    tf_idfs = []
    for sentence, words in sentences.items():
        tf_idf = 0

        for word in query:
            if word not in idfs:
                continue
            idf  = idfs[word]
            tf = (1 if word in words else 0)
            tf_idf += idf * tf
        t = (sentence, tf_idf)
        tf_idfs.append(t)

    sorted_list = sorted(tf_idfs, key=sorter)
    sorted_list.reverse()
    file_list = [item[0] for item in sorted_list]

    return file_list[:n]

def sorter(item):
    return(item[1], 1/len(item[0]))


if __name__ == "__main__":
    main()
