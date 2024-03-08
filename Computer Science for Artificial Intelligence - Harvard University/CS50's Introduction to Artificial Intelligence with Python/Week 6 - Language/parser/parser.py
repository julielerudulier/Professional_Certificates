import nltk
import sys
from nltk.tokenize import word_tokenize

TERMINALS = """
Adj -> "country" | "dreadful" | "enigmatical" | "little" | "moist" | "red"
Adv -> "down" | "here" | "never"
Conj -> "and" | "until"
Det -> "a" | "an" | "his" | "my" | "the"
N -> "armchair" | "companion" | "day" | "door" | "hand" | "he" | "himself"
N -> "holmes" | "home" | "i" | "mess" | "paint" | "palm" | "pipe" | "she"
N -> "smile" | "thursday" | "walk" | "we" | "word"
P -> "at" | "before" | "in" | "of" | "on" | "to"
V -> "arrived" | "came" | "chuckled" | "had" | "lit" | "said" | "sat"
V -> "smiled" | "tell" | "were"
"""

NONTERMINALS = """
S -> NP VP | NP VP Conj VP | NP VP Conj NP VP | NP VP P NP
NP -> N | Det N | Det Adj N | Det N Adv | Det Adj Adj N | Det Adj Adj Adj N | NP P | P NP
VP -> V | V NP | V Adv | Adv VP | V NP NP 
"""

grammar = nltk.CFG.fromstring(NONTERMINALS + TERMINALS)
parser = nltk.ChartParser(grammar)


def main():
    # If filename specified, read sentence from file
    if len(sys.argv) == 2:
        with open(sys.argv[1]) as f:
            s = f.read()

    # Otherwise, get sentence as input
    else:
        s = input("Sentence: ")

    # Convert input into list of words
    s = preprocess(s)

    # Attempt to parse sentence
    try:
        trees = list(parser.parse(s))
    except ValueError as e:
        print(e)
        return
    if not trees:
        print("Could not parse sentence.")
        return

    # Print each tree with noun phrase chunks
    for tree in trees:
        tree.pretty_print()

        print("Noun Phrase Chunks")
        for np in np_chunk(tree):
            print(" ".join(np.flatten()))


def preprocess(sentence):
    """
    Convert `sentence` to a list of its words.
    Pre-process sentence by converting all characters to lowercase
    and removing any word that does not contain at least one alphabetic
    character.
    """
    # Tokenize using nltk's method `word_tokenize`:
    list_words = word_tokenize(sentence.lower())

    # Iterate over every work/token:
    for i in list_words:
        # If token does not contain alphabetic characters, remove from list of tokens:
        if i.isalpha() == False:
            list_words.remove(i)

    return list_words


def np_chunk(tree):
    """
    Return a list of all noun phrase chunks in the sentence tree.
    A noun phrase chunk is defined as any subtree of the sentence
    whose label is "NP" that does not itself contain any other
    noun phrases as subtrees.
    """
    # Initialize an empty list that will contain all NP chunks:
    list_chunks = []

    # Convert the tree to parented tree:
    parentedTree = nltk.tree.ParentedTree.convert(tree)

    # Iterate over every subtree in the tree:
    for subtree in parentedTree.subtrees():
        # If subtree is labelled as a noun ("N"), then we'll consident its parent to be a Noun Phrase chunk:
        if subtree.label() == "N":
            list_chunks.append(subtree.parent())

    return list_chunks


if __name__ == "__main__":
    main()
